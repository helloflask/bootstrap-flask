from flask import render_template_string


def test_render_field(app, client, hello_form):
    @app.route('/field')
    def test():
        form = hello_form()
        return render_template_string('''
        {% from 'bootstrap/form.html' import render_field %}
        {{ render_field(form.csrf_token) }}
        {{ render_field(form.hidden) }}
        {{ render_field(form.username) }}
        {{ render_field(form.password) }}
        ''', form=form)

    response = client.get('/field')
    data = response.get_data(as_text=True)
    assert '<label class="form-control-label" for="csrf_token">CSRF Token</label>' not in data
    assert '<label class="form-control-label" for="hidden">Hidden</label>' not in data
    assert '<input class="form-control" id="username" name="username"' in data
    assert '<input class="form-control" id="password" name="password"' in data
