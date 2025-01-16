from flask import render_template_string


def test_render_icon_font(app, client):
    @app.route('/icon')
    def icon():
        return render_template_string('''
        {% from 'bootstrap4/utils.html' import render_icon_font %}
            {{ render_icon_font('heart') }}
        ''')

    @app.route('/icon-size')
    def icon_size():
        return render_template_string('''
        {% from 'bootstrap4/utils.html' import render_icon_font %}
            {{ render_icon_font('heart', 32) }}
        ''')

    @app.route('/icon-style')
    def icon_style():
        return render_template_string('''
        {% from 'bootstrap4/utils.html' import render_icon_font %}
            {{ render_icon_font('heart', color='primary') }}
        ''')

    @app.route('/icon-color')
    def icon_color():
        return render_template_string('''
        {% from 'bootstrap4/utils.html' import render_icon_font %}
            {{ render_icon_font('heart', color='green') }}
        ''')

    response = client.get('/icon')
    data = response.get_data(as_text=True)
    assert '<i class="bi-heart' in data
    assert 'size: 1em;' in data

    response = client.get('/icon-size')
    data = response.get_data(as_text=True)
    assert '<i class="bi-heart' in data
    assert 'size: 32;' in data

    response = client.get('/icon-style')
    data = response.get_data(as_text=True)
    assert '<i class="bi-heart' in data
    assert ' text-primary' in data

    response = client.get('/icon-color')
    data = response.get_data(as_text=True)
    assert '<i class="bi-heart' in data
    assert 'color: green;' in data


def test_render_icon_font_config(app, client):
    app.config['BOOTSTRAP_ICON_SIZE'] = 100
    app.config['BOOTSTRAP_ICON_COLOR'] = 'success'

    @app.route('/icon')
    def icon():
        return render_template_string('''
        {% from 'bootstrap4/utils.html' import render_icon_font %}
            {{ render_icon_font('heart') }}
        ''')

    response = client.get('/icon')
    data = response.get_data(as_text=True)
    assert 'size: 100;' in data
    assert 'text-success' in data
