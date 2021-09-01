from flask import render_template_string, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect


class TestPagination:
    def test_render_simple_table(self, app, client):
        db = SQLAlchemy(app)

        class Message(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            text = db.Column(db.Text)

        @app.route('/table')
        def test():
            db.drop_all()
            db.create_all()
            for i in range(10):
                m = Message(text='Test message {}'.format(i+1))
                db.session.add(m)
            db.session.commit()
            page = request.args.get('page', 1, type=int)
            pagination = Message.query.paginate(page, per_page=10)
            messages = pagination.items
            titles = [('id', '#'), ('text', 'Message')]
            return render_template_string('''
                                    {% from 'bootstrap/table.html' import render_table %}
                                    {{ render_table(messages, titles) }}
                                    ''', titles=titles, messages=messages)

        response = client.get('/table')
        data = response.get_data(as_text=True)
        assert '<table class="table">' in data
        assert '<th scope="col">#</th>' in data
        assert '<th scope="col">Message</th>' in data
        assert '<th scope="col">Message</th>' in data
        assert '<th scope="row">1</th>' in data
        assert '<td>Test message 1</td>' in data

    def test_render_customized_table(self, app, client):
        db = SQLAlchemy(app)

        class Message(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            text = db.Column(db.Text)

        @app.route('/table')
        def test():
            db.drop_all()
            db.create_all()
            for i in range(10):
                m = Message(text='Test message {}'.format(i+1))
                db.session.add(m)
            db.session.commit()
            page = request.args.get('page', 1, type=int)
            pagination = Message.query.paginate(page, per_page=10)
            messages = pagination.items
            titles = [('id', '#'), ('text', 'Message')]
            return render_template_string('''
                                    {% from 'bootstrap/table.html' import render_table %}
                                    {{ render_table(messages, titles, table_classes='table-striped',
                                    header_classes='thead-dark', caption='Messages') }}
                                    ''', titles=titles, messages=messages)

        response = client.get('/table')
        data = response.get_data(as_text=True)
        assert '<table class="table table-striped">' in data
        assert '<thead class="thead-dark">' in data
        assert '<caption>Messages</caption>' in data

    def test_render_responsive_table(self, app, client):
        db = SQLAlchemy(app)

        class Message(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            text = db.Column(db.Text)

        @app.route('/table')
        def test():
            db.drop_all()
            db.create_all()
            for i in range(10):
                m = Message(text='Test message {}'.format(i+1))
                db.session.add(m)
            db.session.commit()
            page = request.args.get('page', 1, type=int)
            pagination = Message.query.paginate(page, per_page=10)
            messages = pagination.items
            titles = [('id', '#'), ('text', 'Message')]
            return render_template_string('''
                                    {% from 'bootstrap/table.html' import render_table %}
                                    {{ render_table(messages, titles, responsive=True,
                                    responsive_class='table-responsive-sm') }}
                                    ''', titles=titles, messages=messages)

        response = client.get('/table')
        data = response.get_data(as_text=True)
        assert '<div class="table-responsive-sm">' in data

    def test_build_table_titles(self, app, client):
        db = SQLAlchemy(app)

        class Message(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            text = db.Column(db.Text)

        @app.route('/table')
        def test():
            db.drop_all()
            db.create_all()
            for i in range(10):
                m = Message(text='Test message {}'.format(i+1))
                db.session.add(m)
            db.session.commit()
            page = request.args.get('page', 1, type=int)
            pagination = Message.query.paginate(page, per_page=10)
            messages = pagination.items
            return render_template_string('''
                                    {% from 'bootstrap/table.html' import render_table %}
                                    {{ render_table(messages) }}
                                    ''', messages=messages)

        response = client.get('/table')
        data = response.get_data(as_text=True)
        assert '<table class="table">' in data
        assert '<th scope="col">#</th>' in data
        assert '<th scope="col">Text</th>' in data
        assert '<th scope="col">Text</th>' in data
        assert '<th scope="row">1</th>' in data
        assert '<td>Test message 1</td>' in data

    def test_build_table_titles_with_empty_data(self, app, client):

        @app.route('/table')
        def test():
            messages = []
            return render_template_string('''
                                    {% from 'bootstrap/table.html' import render_table %}
                                    {{ render_table(messages) }}
                                    ''', messages=messages)

        response = client.get('/table')
        assert response.status_code == 200

    def test_render_table_with_actions(self, app, client):
        db = SQLAlchemy(app)

        class Message(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            sender = db.Column(db.String(20))
            recipient = db.Column(db.String(20))
            text = db.Column(db.Text)

        @app.route('/table/<string:recipient>/<int:message_id>/resend')
        def test_resend_message(recipient, message_id):
            return 'Re-sending {} to {}'.format(message_id, recipient)

        @app.route('/table/<string:sender>/<int:message_id>/view')
        def test_view_message(sender, message_id):
            return 'Viewing {} from {}'.format(message_id, sender)

        @app.route('/table/new-message')
        def test_create_message():
            return 'New message'

        @app.route('/table')
        def test():
            db.drop_all()
            db.create_all()
            for i in range(10):
                m = Message(
                    text='Test message {}'.format(i+1),
                    sender='me',
                    recipient='john_doe'
                )
                db.session.add(m)
            db.session.commit()
            page = request.args.get('page', 1, type=int)
            pagination = Message.query.paginate(page, per_page=10)
            messages = pagination.items
            titles = [('id', '#'), ('text', 'Message')]
            return render_template_string('''
                {% from 'bootstrap/table.html' import render_table %}
                {{ render_table(messages, titles, model=model, show_actions=True,
                custom_actions=[
                    (
                        'Resend',
                        'bootstrap-reboot',
                        ('test_resend_message', [('recipient', ':recipient'), ('message_id', ':id')])
                    )
                ],
                view_url=('test_view_message', [('sender', ':sender'), ('message_id', ':id')]),
                new_url=url_for('test_create_message')) }}
            ''', titles=titles, model=Message, messages=messages)

        response = client.get('/table')
        data = response.get_data(as_text=True)
        assert 'icons/bootstrap-icons.svg#bootstrap-reboot' in data
        assert 'href="/table/john_doe/1/resend"' in data
        assert 'title="Resend">' in data
        assert 'href="/table/me/1/view"' in data
        assert 'href="/table/new-message"' in data

    def test_customize_icon_title_of_table_actions(self, app, client):

        app.config['BOOTSTRAP_TABLE_VIEW_TITLE'] = 'Read'
        app.config['BOOTSTRAP_TABLE_EDIT_TITLE'] = 'Update'
        app.config['BOOTSTRAP_TABLE_DELETE_TITLE'] = 'Remove'
        app.config['BOOTSTRAP_TABLE_NEW_TITLE'] = 'Create'

        db = SQLAlchemy(app)
        CSRFProtect(app)

        class Message(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            text = db.Column(db.Text)

        @app.route('/table')
        def test():
            db.drop_all()
            db.create_all()
            for i in range(10):
                m = Message(text='Test message {}'.format(i+1))
                db.session.add(m)
            db.session.commit()
            page = request.args.get('page', 1, type=int)
            pagination = Message.query.paginate(page, per_page=10)
            messages = pagination.items
            return render_template_string('''
                {% from 'bootstrap/table.html' import render_table %}
                {{ render_table(messages, model=model, show_actions=True,
                view_url='/view',
                edit_url='/edit',
                delete_url='/delete',
                new_url='/new') }}
                ''', model=Message, messages=messages)

        response = client.get('/table')
        data = response.get_data(as_text=True)
        assert 'title="Read">' in data
        assert 'title="Update">' in data
        assert 'title="Remove">' in data
        assert 'title="Create">' in data
