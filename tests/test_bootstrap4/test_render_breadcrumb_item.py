from flask import render_template_string


def test_render_breadcrumb_item_active(app, client):
    @app.route('/not_active_item')
    def item_foo():
        return render_template_string('''
                {% from 'bootstrap4/nav.html' import render_breadcrumb_item %}
                {{ render_breadcrumb_item('item_bar', 'Bar') }}
                ''')

    @app.route('/active_item')
    def item_bar():
        return render_template_string('''
                {% from 'bootstrap4/nav.html' import render_breadcrumb_item %}
                {{ render_breadcrumb_item('item_bar', 'Bar') }}
                ''')

    response = client.get('/not_active_item')
    data = response.get_data(as_text=True)
    assert '<li class="breadcrumb-item">' in data

    response = client.get('/active_item')
    data = response.get_data(as_text=True)
    assert '<li class="breadcrumb-item active" aria-current="page">' in data
