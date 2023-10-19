from flask import render_template_string
from flask_wtf import FlaskForm
from flask_bootstrap import SwitchField
from wtforms import IntegerRangeField, DecimalRangeField


def test_switch_field(app, client):

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
    assert '<small class="form-text text-body-secondary">Just check this</small>' in data


# test render IntegerRangeField and DecimalRangeField
def test_range_fields(app, client):

    class TestForm(FlaskForm):
        decimal_slider = DecimalRangeField()
        integer_slider = IntegerRangeField(render_kw={'min': '0', 'max': '4'})

    @app.route('/range')
    def test_range():
        form = TestForm()
        return render_template_string('''
        {% from 'bootstrap5/form.html' import render_form %}
        {{ render_form(form) }}
        ''', form=form)

    response = client.get('/range')
    data = response.get_data(as_text=True)
    assert 'Decimal Slider' in data
    assert 'Integer Slider' in data
    assert 'form-range' in data


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
                    {{ render_form(form, form_group_classes='mb-2') }}
                    ''', form=form)

    response = client.get('/default')
    data = response.get_data(as_text=True)
    assert '<div class="mb-3' in data
    response = client.get('/custom')
    data = response.get_data(as_text=True)
    assert '<div class="mb-3' not in data
    assert '<div class="mb-2' in data


def test_form_group_class_config(app, client, hello_form):
    app.config['BOOTSTRAP_FORM_GROUP_CLASSES'] = 'mb-4'

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


def test_form_inline_classes(app, client, hello_form):
    @app.route('/default')
    def test_default():
        form = hello_form()
        return render_template_string('''
                    {% from 'bootstrap5/form.html' import render_form %}
                    {{ render_form(form, form_type='inline') }}
                    ''', form=form)

    @app.route('/custom')
    def test_custom():
        form = hello_form()
        return render_template_string('''
                    {% from 'bootstrap5/form.html' import render_form %}
                    {{ render_form(form, form_type='inline', form_inline_classes='custom-inline-classes') }}
                    ''', form=form)

    response = client.get('/default')
    data = response.get_data(as_text=True)
    assert '<div class="mb-3' not in data
    assert '<div class="col-12' in data
    assert 'row row-cols-lg-auto g-3 align-items-center' in data
    assert '<label class="sr-only' not in data
    assert '<label class="visually-hidden' in data
    response = client.get('/custom')
    data = response.get_data(as_text=True)
    assert 'row row-cols-lg-auto g-3 align-items-center' not in data
    assert 'custom-inline-classes' in data


def test_form_inline_classes_config(app, client, hello_form):
    app.config['BOOTSTRAP_FORM_INLINE_CLASSES'] = 'custom-inline-classes'

    @app.route('/config')
    def test_config():
        form = hello_form()
        return render_template_string('''
                        {% from 'bootstrap5/form.html' import render_form %}
                        {{ render_form(form, form_type='inline') }}
                        ''', form=form)

    response = client.get('/config')
    data = response.get_data(as_text=True)
    assert 'row row-cols-lg-auto g-3 align-items-center' not in data
    assert 'custom-inline-classes' in data
