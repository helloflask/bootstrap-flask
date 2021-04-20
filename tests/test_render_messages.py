from flask import flash, render_template_string


class TestMessages:
    def test_render_messages(self, app, client):
        @app.route('/messages')
        def test_messages():
            flash('test message', 'danger')
            return render_template_string('''
                            {% from 'bootstrap/utils.html' import render_messages %}
                            {{ render_messages() }}
                            ''')

        @app.route('/container')
        def test_container():
            flash('test message', 'danger')
            return render_template_string('''
                            {% from 'bootstrap/utils.html' import render_messages %}
                            {{ render_messages(container=True) }}
                            ''')

        @app.route('/dismissible')
        def test_dismissible():
            flash('test message', 'danger')
            return render_template_string('''
                            {% from 'bootstrap/utils.html' import render_messages %}
                            {{ render_messages(dismissible=True) }}
                            ''')

        @app.route('/dismiss_animate')
        def test_dismiss_animate():
            flash('test message', 'danger')
            return render_template_string('''
                            {% from 'bootstrap/utils.html' import render_messages %}
                            {{ render_messages(dismissible=True, dismiss_animate=True) }}
                            ''')

        response = client.get('/messages')
        data = response.get_data(as_text=True)
        assert '<div class="alert alert-danger"' in data

        response = client.get('/container')
        data = response.get_data(as_text=True)
        assert '<div class="container flashed-messages">' in data

        response = client.get('/dismissible')
        data = response.get_data(as_text=True)
        assert 'alert-dismissible' in data
        assert '<button type="button" class="close" data-dismiss="alert"' in data
        assert 'fade show' not in data

        response = client.get('/dismiss_animate')
        data = response.get_data(as_text=True)
        assert 'alert-dismissible', data
        assert '<button type="button" class="close" data-dismiss="alert"' in data
        assert 'fade show' in data
