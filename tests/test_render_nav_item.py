from flask import render_template_string


def test_render_nav_item_active(bootstrap, app, client):
    @app.route('/active')
    def foo():
        return render_template_string('''
                {% from 'bootstrap/nav.html' import render_nav_item %}
                {{ render_nav_item('foo', 'Foo') }}
                ''')

    response = client.get('/active')
    data = response.get_data(as_text=True)
    assert '<a class="nav-item nav-link active"' in data

    @app.route('/not_active')
    def bar():
        return render_template_string('''
                {% from 'bootstrap/nav.html' import render_nav_item %}
                {{ render_nav_item('foo', 'Foo') }}
                ''')

    response = client.get('/not_active')
    data = response.get_data(as_text=True)
    assert '<a class="nav-item nav-link"' in data
