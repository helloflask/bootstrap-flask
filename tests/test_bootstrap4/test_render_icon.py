from flask import render_template_string


def test_render_icon(app, client):
    @app.route('/icon')
    def icon():
        return render_template_string('''
        {% from 'bootstrap4/utils.html' import render_icon %}
            {{ render_icon('heart') }}
        ''')

    @app.route('/icon-size')
    def icon_size():
        return render_template_string('''
        {% from 'bootstrap4/utils.html' import render_icon %}
            {{ render_icon('heart', 32) }}
        ''')

    @app.route('/icon-style')
    def icon_style():
        return render_template_string('''
        {% from 'bootstrap4/utils.html' import render_icon %}
            {{ render_icon('heart', color='primary') }}
        ''')

    @app.route('/icon-color')
    def icon_color():
        return render_template_string('''
        {% from 'bootstrap4/utils.html' import render_icon %}
            {{ render_icon('heart', color='green') }}
        ''')

    @app.route('/icon-title')
    def icon_title():
        return render_template_string('''
        {% from 'bootstrap4/utils.html' import render_icon %}
            {{ render_icon('heart', title='Heart') }}
        ''')

    @app.route('/icon-desc-classes')
    def icon_desc_classes():
        return render_template_string('''
        {% from 'bootstrap4/utils.html' import render_icon %}
            {{ render_icon('heart', desc='A heart.', classes='text-success bg-light') }}
        ''')

    response = client.get('/icon')
    data = response.get_data(as_text=True)
    assert 'bootstrap-icons.svg#heart' in data
    assert 'width="1em"' in data
    assert 'height="1em"' in data

    response = client.get('/icon-size')
    data = response.get_data(as_text=True)
    assert 'bootstrap-icons.svg#heart' in data
    assert 'width="32"' in data
    assert 'height="32"' in data

    response = client.get('/icon-style')
    data = response.get_data(as_text=True)
    assert 'bootstrap-icons.svg#heart' in data
    assert 'text-primary' in data

    response = client.get('/icon-color')
    data = response.get_data(as_text=True)
    assert 'bootstrap-icons.svg#heart' in data
    assert 'style="color: green"' in data

    response = client.get('/icon-title')
    data = response.get_data(as_text=True)
    assert 'bootstrap-icons.svg#heart' in data
    assert '<title>Heart</title>' in data

    response = client.get('/icon-desc-classes')
    data = response.get_data(as_text=True)
    assert 'bootstrap-icons.svg#heart' in data
    assert '<desc>A heart.</desc>' in data
    assert 'class="bi text-success bg-light"' in data


def test_render_icon_config(app, client):
    app.config['BOOTSTRAP_ICON_SIZE'] = 100
    app.config['BOOTSTRAP_ICON_COLOR'] = 'success'

    @app.route('/icon')
    def icon():
        return render_template_string('''
        {% from 'bootstrap4/utils.html' import render_icon %}
            {{ render_icon('heart') }}
        ''')

    response = client.get('/icon')
    data = response.get_data(as_text=True)
    assert 'width="100"' in data
    assert 'height="100"' in data
    assert 'text-success' in data
