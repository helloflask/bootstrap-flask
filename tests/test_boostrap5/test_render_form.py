from flask import render_template_string
from flask_wtf import FlaskForm
from flask_bootstrap import SwitchField


def test_form_description_for_switchfield(app, client):

    class TestForm(FlaskForm):
        remember = SwitchField('Remember me', description='Just check this')

    @app.route('/description')
    def description():
        form = TestForm()
        return render_template_string('''
        {% from 'bootstrap5/form.html' import render_form %}
        {{ render_form(form) }}
        ''', form=form)

    response = client.get('/description')
    data = response.get_data(as_text=True)
    assert 'Remember me' in data
    assert 'custom-control custom-switch' not in data
    assert 'form-check form-switch' in data
    assert '<small class="form-text text-muted">Just check this</small>' in data
