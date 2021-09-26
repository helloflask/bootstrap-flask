from flask import render_template_string


def test_render_form_row(app, client, hello_form):
    @app.route('/form')
    def test():
        form = hello_form()
        return render_template_string('''
                {% from 'bootstrap4/form.html' import render_form_row %}
                {{ render_form_row([form.username, form.password]) }}
                ''', form=form)
    response = client.get('/form')
    data = response.get_data(as_text=True)
    assert '<div class="form-row">' in data
    assert '<div class="col">' in data


def test_render_form_row_row_class(app, client, hello_form):
    @app.route('/form')
    def test():
        form = hello_form()
        return render_template_string('''
                {% from 'bootstrap4/form.html' import render_form_row %}
                {{ render_form_row([form.username, form.password], row_class='row') }}
                ''', form=form)
    response = client.get('/form')
    data = response.get_data(as_text=True)
    assert '<div class="row">' in data


def test_render_form_row_col_class_default(app, client, hello_form):
    @app.route('/form')
    def test():
        form = hello_form()
        return render_template_string('''
                {% from 'bootstrap4/form.html' import render_form_row %}
                {{ render_form_row([form.username, form.password], col_class_default='col-md-6') }}
                ''', form=form)
    response = client.get('/form')
    data = response.get_data(as_text=True)
    assert '<div class="col-md-6">' in data


def test_render_form_row_col_map(app, client, hello_form):
    @app.route('/form')
    def test():
        form = hello_form()
        return render_template_string('''
                {% from 'bootstrap4/form.html' import render_form_row %}
                {{ render_form_row([form.username, form.password], col_map={'username': 'col-md-6'}) }}
                ''', form=form)
    response = client.get('/form')
    data = response.get_data(as_text=True)
    assert '<div class="col">' in data
    assert '<div class="col-md-6">' in data
