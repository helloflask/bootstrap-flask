from flask import render_template_string, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


def test_render_pagination(app, client):
    db = SQLAlchemy(app)

    class Message(db.Model):
        id = db.Column(db.Integer, primary_key=True)

    @app.route('/pagination')
    def test():
        db.drop_all()
        db.create_all()
        for _ in range(100):
            msg = Message()
            db.session.add(msg)
        db.session.commit()
        page = request.args.get('page', 1, type=int)
        pagination = Message.query.paginate(page=page, per_page=10)
        messages = pagination.items
        return render_template_string('''
                                {% from 'bootstrap4/pagination.html' import render_pagination %}
                                {{ render_pagination(pagination) }}
                                ''', pagination=pagination, messages=messages)

    response = client.get('/pagination')
    data = response.get_data(as_text=True)
    assert '<nav aria-label="Page navigation">' in data
    assert '<a class="page-link" href="#">1 <span class="sr-only">(current)</span></a>' in data
    assert '10</a>' in data

    response = client.get('/pagination?page=2')
    data = response.get_data(as_text=True)
    assert '<nav aria-label="Page navigation">' in data
    assert '1</a>' in data
    assert '<a class="page-link" href="#">2 <span class="sr-only">(current)</span></a>' in data
    assert '10</a>' in data


def test_pagination_after_delete(app, client):
    """Test that pagination works correctly after deleting items."""
    db = SQLAlchemy(app)

    class Message(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        text = db.Column(db.String(100))

    @app.route('/table')
    def test_table():
        page = request.args.get('page', 1, type=int)
        pagination = Message.query.paginate(page=page, per_page=10)
        messages = pagination.items
        return render_template_string('''
            Page {{ pagination.page }} of {{ pagination.pages }}
            Total: {{ pagination.total }}
            Messages: {{ messages|length }}
        ''', pagination=pagination, messages=messages)

    @app.route('/table/<int:message_id>/delete', methods=['POST'])
    def delete_message(message_id):
        message = Message.query.get(message_id)
        if message:
            # Get current page from request args or referrer
            current_page = request.args.get('page', 1, type=int)
            if request.referrer and 'page=' in request.referrer:
                import re
                page_match = re.search(r'[?&]page=(\d+)', request.referrer)
                if page_match:
                    current_page = int(page_match.group(1))

            # Delete the message
            db.session.delete(message)
            db.session.commit()

            # Calculate total remaining messages and pages
            total_messages = Message.query.count()
            per_page = 10
            total_pages = (total_messages + per_page - 1) // per_page if total_messages > 0 else 1

            # Determine which page to redirect to
            redirect_page = current_page
            if total_pages == 0 or total_messages == 0:
                redirect_page = 1
            elif current_page > total_pages:
                redirect_page = total_pages

            flash(f'Message {message_id} has been deleted.', 'success')
            return redirect(url_for('test_table', page=redirect_page))
        else:
            flash(f'Message {message_id} did not exist.', 'warning')
            return redirect(url_for('test_table'))

    _test_delete_from_middle_page(app, db, Message, client)
    _test_delete_from_last_page(app, db, Message, client)
    _test_delete_all_messages(app, db, Message, client)


def _test_delete_from_middle_page(app, db, Message, client):
    """Test Case 1: Delete from middle page - should stay on same page."""
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Create 25 messages (3 pages of 10 each, 5 on last page)
        for i in range(25):
            msg = Message(text=f'Message {i+1}')
            db.session.add(msg)
        db.session.commit()

        # Go to page 2 and delete a message
        response = client.get('/table?page=2')
        assert 'Page 2 of 3' in response.get_data(as_text=True)

        # Delete message ID 15 (should be on page 2)
        response = client.post('/table/15/delete?page=2', follow_redirects=True)
        data = response.get_data(as_text=True)
        assert 'Page 2 of 3' in data  # Should still be on page 2
        assert 'Total: 24' in data     # One less message


def _test_delete_from_last_page(app, db, Message, client):
    """Test Case 2: Delete all items from last page - should redirect to previous page."""
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Create 21 messages (3 pages: 10, 10, 1)
        for i in range(21):
            msg = Message(text=f'Message {i+1}')
            db.session.add(msg)
        db.session.commit()

        # Go to page 3 (last page with 1 item)
        response = client.get('/table?page=3')
        data = response.get_data(as_text=True)
        assert 'Page 3 of 3' in data
        assert 'Total: 21' in data

        # Delete the only message on page 3
        response = client.post('/table/21/delete?page=3', follow_redirects=True)
        data = response.get_data(as_text=True)
        assert 'Page 2 of 2' in data  # Should redirect to page 2
        assert 'Total: 20' in data     # One less message


def _test_delete_all_messages(app, db, Message, client):
    """Test Case 3: Delete all messages - should go to page 1."""
    with app.app_context():
        db.drop_all()
        db.create_all()
        msg = Message(text='Last message')
        db.session.add(msg)
        db.session.commit()

        response = client.post('/table/1/delete', follow_redirects=True)
        data = response.get_data(as_text=True)
        assert 'Page 1 of' in data  # Should be on page 1 (could be "Page 1 of 0" or "Page 1 of 1")
        assert 'Total: 0' in data     # No messages left
