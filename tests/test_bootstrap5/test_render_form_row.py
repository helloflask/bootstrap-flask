from flask import render_template_string


def test_render_form_row(app, client, hello_form):
    @app.route('/form')
    def test():
        form = hello_form()
        return render_template_string('''
                {% from 'bootstrap5/form.html' import render_form_row %}
                {{ render_form_row([form.username, form.password]) }}
                ''', form=form)
    response = client.get('/form')
    data = response.get_data(as_text=True)
    assert '<div class="form-row">' not in data
    assert '<div class="row">' in data
    assert '<div class="col">' in data
