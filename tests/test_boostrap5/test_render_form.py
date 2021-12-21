from flask import render_template_string
from flask_wtf import FlaskForm
from flask_bootstrap import SwitchField


def test_switchfield(app, client):

    class TestForm(FlaskForm):
        remember = SwitchField('Remember me', description='Just check this')

    @app.route('/switch')
    def test_switch():
        form = TestForm()
        return render_template_string('''
        {% from 'bootstrap5/form.html' import render_form %}
        {{ render_form(form) }}
        ''', form=form)

    response = client.get('/switch')
    data = response.get_data(as_text=True)
    assert 'Remember me' in data
    assert 'custom-control custom-switch' not in data
    assert 'form-check form-switch' in data
    assert 'role="switch"' in data
    assert '<small class="form-text text-muted">Just check this</small>' in data


def test_form_group_class(app, client, hello_form):
    @app.route('/default')
    def test_default():
        form = hello_form()
        return render_template_string('''
                    {% from 'bootstrap5/form.html' import render_form %}
                    {{ render_form(form) }}
                    ''', form=form)

    @app.route('/custom')
    def test_custom():
        form = hello_form()
        return render_template_string('''
                    {% from 'bootstrap5/form.html' import render_form %}
                    {{ render_form(form, form_group_class='mb-2') }}
                    ''', form=form)

    response = client.get('/default')
    data = response.get_data(as_text=True)
    assert '<div class="mb-3' in data
    response = client.get('/custom')
    data = response.get_data(as_text=True)
    assert '<div class="mb-3' not in data
    assert '<div class="mb-2' in data

    app.config['BOOTSTRAP_FORM_GROUP_CLASS'] = 'mb-4'

    @app.route('/config')
    def test_config():
        form = hello_form()
        return render_template_string('''
                        {% from 'bootstrap5/form.html' import render_form %}
                        {{ render_form(form) }}
                        ''', form=form)

    response = client.get('/config')
    data = response.get_data(as_text=True)
    assert '<div class="mb-3' not in data
    assert '<div class="mb-4' in data
