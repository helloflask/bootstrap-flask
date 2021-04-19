from flask import render_template_string


def test_render_nav_item(app, client):
    @app.route('/nav_item')
    def test():
        return render_template_string('''
                {% from 'bootstrap/nav.html' import render_nav_item %}
                {{ render_nav_item('test', 'Home') }}
                ''')

    response = client.get('/nav_item')
    data = response.get_data(as_text=True)
    assert '<a class="nav-item nav-link active"' in data
