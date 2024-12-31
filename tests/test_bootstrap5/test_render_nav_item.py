from flask import render_template_string


def test_render_nav_item(app, client):
    @app.route('/hello')
    def hello():
        return 'Hello'

    @app.route('/nav_item/4')
    def test_bootstrap4():
        return render_template_string('''
                        {% from 'bootstrap4/nav.html' import render_nav_item %}
                        {{ render_nav_item('hello', 'Hello Nav', _badge='beta') }}
                        ''')

    @app.route('/nav_item/5')
    def test_bootstrap5():
        return render_template_string('''
                        {% from 'bootstrap5/nav.html' import render_nav_item %}
                        {{ render_nav_item('hello', 'Hello Nav', _badge='beta', _use_li=True) }}
                        ''')

    response = client.get('/nav_item/4')
    data = response.get_data(as_text=True)
    assert 'href="/hello">' in data
    assert 'span class="badge badge-light"' in data
    assert 'beta' in data
    assert '<li class="nav-item">' not in data
    assert '</li>' not in data

    response = client.get('/nav_item/5')
    data = response.get_data(as_text=True)
    assert 'href="/hello">' in data
    assert 'span class="badge text-bg-light"' in data
    assert 'beta' in data
    assert '<li class="nav-item">' in data
    assert '</li>' in data
