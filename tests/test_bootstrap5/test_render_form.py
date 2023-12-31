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


# test render label_class, radio_class and descr_class
def test_class(app, client, class_form):

    @app.route('/class')
    def test_class():
        form = class_form()
        return render_template_string('''
        {% from 'bootstrap5/form.html' import render_form %}
        {{ render_form(form) }}
        ''', form=form)

    response = client.get('/class')
    data = response.get_data(as_text=True)

    # render_field form.html line 88
    assert '<label class="form-check-label text-decoration-underline" for="boolean">Bool label</label>' in data
    # render_field form.html line 95
    assert '<small class="form-text text-body-secondary text-decoration-line-through">Bool descr</small>' in data

    # render_field form.html line 223
    assert '<label class="form-label text-decoration-underline" for="integer">Int label</label>' in data
    # render_field form.html line 248
    assert '<small class="form-text text-body-secondary text-decoration-line-through">Int descr</small>' in data

    # render_field form.html line 111
    assert '<label class="form-label text-uppercase" for="option">Rad label</label>' in data
    # render_field form.html line 120
    assert '<label class="form-check-label text-decoration-line-through" for="option-1">Two</label>' in data
    # render_field form.html line 132
    assert '<small class="form-text text-body-secondary text-decoration-underline">Rad descr</small>' in data


def test_class_inline(app, client, class_form):

    @app.route('/class_inline')
    def test_class_inline():
        form = class_form()
        return render_template_string('''
        {% from 'bootstrap5/form.html' import render_form %}
        {{ render_form(form, form_type='inline') }}
        ''', form=form)

    response = client.get('/class_inline')
    data = response.get_data(as_text=True)

    # render_field form.html line 88, repeat from other test
    assert '<label class="form-check-label text-decoration-underline" for="boolean">Bool label</label>' in data
    # render_field form.html line 95, repeat from other test
    assert '<small class="form-text text-body-secondary text-decoration-line-through">Bool descr</small>' in data

    # render_field form.html line 166, probably not displayed
    assert '<label class="visually-hidden text-decoration-underline" for="integer">Int label</label>' in data
    # render_field form.html not rendered description
    assert '">Int descr</small>' not in data

    # render_field form.html line 105, probabaly not displayed
    assert '<label class="visually-hidden text-uppercase" for="option">Rad label</label>' in data
    # render_field form.html line 120, repeat from other test
    assert '<label class="form-check-label text-decoration-line-through" for="option-1">Two</label>' in data
    # render_field form.html line 132, repeat from other test
    assert '<small class="form-text text-body-secondary text-decoration-underline">Rad descr</small>' in data


def test_class_horizontal(app, client, class_form):

    @app.route('/class_horizontal')
    def test_class_horizontal():
        form = class_form()
        return render_template_string('''
        {% from 'bootstrap5/form.html' import render_form %}
        {{ render_form(form, form_type='horizontal') }}
        ''', form=form)

    response = client.get('/class_horizontal')
    data = response.get_data(as_text=True)

    # render_field form.html line 88, repeat from other test
    assert '<label class="form-check-label text-decoration-underline" for="boolean">Bool label</label>' in data
    # render_field form.html line 95, repeat from other test
    assert '<small class="form-text text-body-secondary text-decoration-line-through">Bool descr</small>' in data

    # render_field form.html line 189
    assert '<label class="col-form-label col-lg-2 text-decoration-underline" for="integer">Int label</label>' in data
    # render_field form.html line 219
    assert '<small class="form-text text-body-secondary text-decoration-line-through">Int descr</small>' in data

    # render_field form.html line 109
    assert '<label class="col-form-label col-lg-2 text-uppercase" for="option">Rad label</label>' in data
    # render_field form.html line 120, repeat from other test
    assert '<label class="form-check-label text-decoration-line-through" for="option-1">Two</label>' in data
    # render_field form.html line 132, repeat from other test
    assert '<small class="form-text text-body-secondary text-decoration-underline">Rad descr</small>' in data
