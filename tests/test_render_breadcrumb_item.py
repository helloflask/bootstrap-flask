from flask import render_template_string


def test_render_breadcrumb_item(app, client):
    @app.route('/breadcrumb_item')
    def test():
        return render_template_string('''
                {% from 'bootstrap/nav.html' import render_breadcrumb_item %}
                {{ render_breadcrumb_item('test', 'Home') }}
                ''')

    response = client.get('/breadcrumb_item')
    data = response.get_data(as_text=True)
    assert '<li class="breadcrumb-item active"  aria-current="page">' in data
