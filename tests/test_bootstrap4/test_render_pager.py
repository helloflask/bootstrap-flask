from flask import render_template_string, request
from flask_sqlalchemy import SQLAlchemy


def test_render_pager(app, client):
    db = SQLAlchemy(app)

    class Message(db.Model):
        id = db.Column(db.Integer, primary_key=True)

    @app.route('/pager')
    def test():
        db.drop_all()
        db.create_all()
        for i in range(100):
            m = Message()
            db.session.add(m)
        db.session.commit()
        page = request.args.get('page', 1, type=int)
        pagination = Message.query.paginate(page, per_page=10)
        messages = pagination.items
        return render_template_string('''
                        {% from 'bootstrap/pagination.html' import render_pager %}
                        {{ render_pager(pagination) }}
                        ''', pagination=pagination, messages=messages)

    response = client.get('/pager')
    data = response.get_data(as_text=True)
    assert '<nav aria-label="Page navigation">' in data
    assert 'Previous' in data
    assert 'Next' in data
    assert '<li class="page-item disabled">' in data

    response = client.get('/pager?page=2')
    data = response.get_data(as_text=True)
    assert '<nav aria-label="Page navigation">' in data
    assert 'Previous' in data
    assert 'Next' in data
    assert '<li class="page-item disabled">' not in data
