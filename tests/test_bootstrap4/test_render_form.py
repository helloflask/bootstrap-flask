from flask import current_app, render_template_string
from flask_wtf import FlaskForm
from wtforms import BooleanField, FileField, MultipleFileField, \
    PasswordField, RadioField, StringField, SubmitField, IntegerRangeField, \
    DecimalRangeField
from wtforms.validators import DataRequired
from flask_bootstrap import SwitchField


def test_render_form(app, client, hello_form):
    @app.route('/form')
    def test():
        form = hello_form()
        return render_template_string('''
                {% from 'bootstrap4/form.html' import render_form %}
                {{ render_form(form) }}
                ''', form=form)

    response = client.get('/form')
    data = response.get_data(as_text=True)
    assert '<input class="form-control" id="username"' in data
    assert '<input class="form-control" id="password"' in data


# test WTForm field description for BooleanField
def test_form_description_for_booleanfield(app, client):

    class TestForm(FlaskForm):
        remember = BooleanField('Remember me', description='Just check this')

    @app.route('/description')
    def description():
        form = TestForm()
        return render_template_string('''
        {% from 'bootstrap4/form.html' import render_form %}
        {{ render_form(form) }}
        ''', form=form)

    response = client.get('/description')
    data = response.get_data(as_text=True)
    assert 'Remember me' in data
    assert '<small class="form-text text-muted">Just check this</small>' in data


# test render SwitchField
def test_switch_field(app, client):

    class TestForm(FlaskForm):
        remember = SwitchField('Remember me', description='Just check this')

    @app.route('/switch')
    def test_switch():
        form = TestForm()
        return render_template_string('''
        {% from 'bootstrap4/form.html' import render_form %}
        {{ render_form(form) }}
        ''', form=form)

    response = client.get('/switch')
    data = response.get_data(as_text=True)
    assert 'Remember me' in data
    assert 'custom-switch' in data
    assert '<small class="form-text text-muted">Just check this</small>' in data


# test render IntegerRangeField and DecimalRangeField
def test_range_fields(app, client):

    class TestForm(FlaskForm):
        decimal_slider = DecimalRangeField()
        integer_slider = IntegerRangeField(render_kw={'min': '0', 'max': '4'})

    @app.route('/range')
    def test_range():
        form = TestForm()
        return render_template_string('''
        {% from 'bootstrap4/form.html' import render_form %}
        {{ render_form(form) }}
        ''', form=form)

    response = client.get('/range')
    data = response.get_data(as_text=True)
    assert 'Decimal Slider' in data
    assert 'Integer Slider' in data
    assert 'form-control-range' in data


# test WTForm fields for render_form and render_field
def test_render_form_enctype(app, client):
    class SingleUploadForm(FlaskForm):
        avatar = FileField('Avatar')

    class MultiUploadForm(FlaskForm):
        photos = MultipleFileField('Multiple photos')

    @app.route('/single')
    def single():
        form = SingleUploadForm()
        return render_template_string('''
        {% from 'bootstrap4/form.html' import render_form %}
        {{ render_form(form) }}
        ''', form=form)

    @app.route('/multi')
    def multi():
        form = SingleUploadForm()
        return render_template_string('''
        {% from 'bootstrap4/form.html' import render_form %}
        {{ render_form(form) }}
        ''', form=form)

    response = client.get('/single')
    data = response.get_data(as_text=True)
    assert 'multipart/form-data' in data

    response = client.get('/multi')
    data = response.get_data(as_text=True)
    assert 'multipart/form-data' in data


# test render_kw class for WTForms field
def test_form_render_kw_class(app, client):

    class TestForm(FlaskForm):
        username = StringField('Username')
        password = PasswordField('Password', render_kw={'class': 'my-password-class'})
        submit = SubmitField(render_kw={'class': 'my-awesome-class'})

    @app.route('/render_kw')
    def render_kw():
        form = TestForm()
        return render_template_string('''
        {% from 'bootstrap4/form.html' import render_form %}
        {{ render_form(form) }}
        ''', form=form)

    response = client.get('/render_kw')
    data = response.get_data(as_text=True)
    assert 'class="form-control"' in data
    assert 'class="form-control "' not in data
    assert 'class="form-control my-password-class"' in data
    assert 'my-awesome-class' in data
    assert 'btn' in data


def test_button_size(app, client, hello_form):
    assert current_app.config['BOOTSTRAP_BTN_SIZE'] == 'md'
    current_app.config['BOOTSTRAP_BTN_SIZE'] = 'lg'

    @app.route('/form')
    def test():
        form = hello_form()
        return render_template_string('''
        {% from 'bootstrap4/form.html' import render_form %}
        {{ render_form(form) }}
        ''', form=form)

    @app.route('/form2')
    def test_overwrite():
        form = hello_form()
        return render_template_string('''
        {% from 'bootstrap4/form.html' import render_form %}
        {{ render_form(form, button_size='sm') }}
        ''', form=form)

    response = client.get('/form')
    data = response.get_data(as_text=True)
    assert 'btn-lg' in data

    response = client.get('/form2')
    data = response.get_data(as_text=True)
    assert 'btn-lg' not in data
    assert 'btn-sm' in data


def test_button_style(app, client, hello_form):
    assert current_app.config['BOOTSTRAP_BTN_STYLE'] == 'primary'
    current_app.config['BOOTSTRAP_BTN_STYLE'] = 'secondary'

    @app.route('/form')
    def test():
        form = hello_form()
        return render_template_string('''
        {% from 'bootstrap4/form.html' import render_form %}
        {{ render_form(form) }}
        ''', form=form)

    @app.route('/form2')
    def test_overwrite():
        form = hello_form()
        return render_template_string('''
        {% from 'bootstrap4/form.html' import render_form %}
        {{ render_form(form, button_style='success') }}
        ''', form=form)

    @app.route('/form3')
    def test_button_map():
        form = hello_form()
        return render_template_string('''
        {% from 'bootstrap4/form.html' import render_form %}
        {{ render_form(form, button_map={'submit': 'warning'}) }}
        ''', form=form)

    response = client.get('/form')
    data = response.get_data(as_text=True)
    assert 'btn-secondary' in data

    response = client.get('/form2')
    data = response.get_data(as_text=True)
    assert 'btn-primary' not in data
    assert 'btn-success' in data

    response = client.get('/form3')
    data = response.get_data(as_text=True)
    assert 'btn-primary' not in data
    assert 'btn-warning' in data


def test_error_message_for_radiofield_and_booleanfield(app, client):
    class TestForm(FlaskForm):
        remember = BooleanField('Remember me', validators=[DataRequired()])
        option = RadioField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('bird', 'Bird'), ('alien', 'Alien')],
                            validators=[DataRequired()])

    @app.route('/error', methods=['GET', 'POST'])
    def error():
        form = TestForm()
        if form.validate_on_submit():
            pass
        return render_template_string('''
        {% from 'bootstrap4/form.html' import render_form %}
        {{ render_form(form) }}
        ''', form=form)

    response = client.post('/error', follow_redirects=True)
    data = response.get_data(as_text=True)
    assert 'This field is required' in data
