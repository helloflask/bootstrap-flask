from flask import render_template_string


def test_render_nav_item_active(app, client):
    @app.route('/active')
    def foo():
        return render_template_string('''
                {% from 'bootstrap4/nav.html' import render_nav_item %}
                {{ render_nav_item('foo', 'Foo') }}
                ''')

    @app.route('/not_active')
    def bar():
        return render_template_string('''
                {% from 'bootstrap4/nav.html' import render_nav_item %}
                {{ render_nav_item('foo', 'Foo') }}
                ''')

    response = client.get('/active')
    data = response.get_data(as_text=True)
    assert '<a class="nav-item nav-link active"' in data

    response = client.get('/not_active')
    data = response.get_data(as_text=True)
    assert '<a class="nav-item nav-link"' in data
