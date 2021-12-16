from flask import flash, render_template_string


def test_render_messages(app, client):
    @app.route('/messages')
    def test_messages():
        flash('test message', 'danger')
        return render_template_string('''
                        {% from 'bootstrap5/utils.html' import render_messages %}
                        {{ render_messages(dismissible=True) }}
                        ''')

    response = client.get('/messages')
    data = response.get_data(as_text=True)
    assert 'class="btn-close" data-bs-dismiss="alert" aria-label="Close">' in data
