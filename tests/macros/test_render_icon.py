from flask import render_template_string


class TestIcon:
    def test_render_icon(self, app, client):
        @app.route('/icon')
        def icon():
            return render_template_string('''
            {% from 'bootstrap/utils.html' import render_icon %}
                {{ render_icon('heart') }}
            ''')

        @app.route('/icon-size')
        def icon_size():
            return render_template_string('''
            {% from 'bootstrap/utils.html' import render_icon %}
                {{ render_icon('heart', 32) }}
            ''')

        @app.route('/icon-style')
        def icon_style():
            return render_template_string('''
            {% from 'bootstrap/utils.html' import render_icon %}
                {{ render_icon('heart', color='primary') }}
            ''')

        @app.route('/icon-color')
        def icon_color():
            return render_template_string('''
            {% from 'bootstrap/utils.html' import render_icon %}
                {{ render_icon('heart', color='green') }}
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

    def test_render_icon_config(self, app, client):
        app.config['BOOTSTRAP_ICON_SIZE'] = 100
        app.config['BOOTSTRAP_ICON_COLOR'] = 'success'

        @app.route('/icon')
        def icon():
            return render_template_string('''
            {% from 'bootstrap/utils.html' import render_icon %}
                {{ render_icon('heart') }}
            ''')

        response = client.get('/icon')
        data = response.get_data(as_text=True)
        assert 'width="100"' in data
        assert 'height="100"' in data
        assert 'text-success' in data
