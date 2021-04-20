from flask import render_template_string, request
from flask_sqlalchemy import SQLAlchemy


def test_render_pagination(app, client):
    db = SQLAlchemy(app)

    class Message(db.Model):
        id = db.Column(db.Integer, primary_key=True)

    @app.route('/pagination')
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
                                {% from 'bootstrap/pagination.html' import render_pagination %}
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
