import unittest

from flask import Flask, render_template_string, current_app, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, FileField, MultipleFileField
from wtforms.validators import DataRequired, Length

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


class HelloForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 150)])
    remember = BooleanField('Remember me')
    submit = SubmitField()


class BootstrapTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.testing = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.secret_key = 'for test'
        self.bootstrap = Bootstrap(self.app)  # noqa

        @self.app.route('/')
        def index():
            return render_template_string('{{ bootstrap.load_css() }}{{ bootstrap.load_js() }}')

        self.context = self.app.test_request_context()
        self.context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.context.pop()

    def test_extension_init(self):
        self.assertIn('bootstrap', current_app.extensions)

    def test_load_css(self):
        rv = self.bootstrap.load_css()
        self.assertIn('bootstrap.min.css', rv)

    def test_load_js(self):
        rv = self.bootstrap.load_js()
        self.assertIn('bootstrap.min.js', rv)

    def test_local_resources(self):
        current_app.config['BOOTSTRAP_SERVE_LOCAL'] = True

        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertNotIn('https://cdn.jsdelivr.net/npm/bootstrap', data)
        self.assertIn('bootstrap.min.js', data)
        self.assertIn('bootstrap.min.css', data)
        self.assertIn('jquery.min.js', data)

        css_response = self.client.get('/bootstrap/static/css/bootstrap.min.css')
        js_response = self.client.get('/bootstrap/static/js/bootstrap.min.js')
        jquery_response = self.client.get('/bootstrap/static/jquery.min.js')
        self.assertNotEqual(css_response.status_code, 404)
        self.assertNotEqual(js_response.status_code, 404)
        self.assertNotEqual(jquery_response.status_code, 404)

        css_rv = self.bootstrap.load_css()
        js_rv = self.bootstrap.load_js()
        self.assertIn('/bootstrap/static/css/bootstrap.min.css', css_rv)
        self.assertIn('/bootstrap/static/js/bootstrap.min.js', js_rv)
        self.assertNotIn('https://cdn.jsdelivr.net/npm/bootstrap', css_rv)
        self.assertNotIn('https://cdn.jsdelivr.net/npm/bootstrap', js_rv)

    def test_cdn_resources(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertIn('https://cdn.jsdelivr.net/npm/bootstrap', data)
        self.assertIn('bootstrap.min.js', data)
        self.assertIn('bootstrap.min.css', data)

        css_rv = self.bootstrap.load_css()
        js_rv = self.bootstrap.load_js()
        self.assertNotIn('/bootstrap/static/css/bootstrap.min.css', css_rv)
        self.assertNotIn('/bootstrap/static/js/bootstrap.min.js', js_rv)
        self.assertIn('https://cdn.jsdelivr.net/npm/bootstrap', css_rv)
        self.assertIn('https://cdn.jsdelivr.net/npm/bootstrap', js_rv)

    def test_render_field(self):
        @self.app.route('/field')
        def test():
            form = HelloForm()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_field %}
            {{ render_field(form.username) }}
            {{ render_field(form.password) }}
            ''', form=form)

        response = self.client.get('/field')
        data = response.get_data(as_text=True)
        self.assertIn('<input class="form-control" id="username" name="username"', data)
        self.assertIn('<input class="form-control" id="password" name="password"', data)

    def test_render_form(self):
        @self.app.route('/form')
        def test():
            form = HelloForm()
            return render_template_string('''
                    {% from 'bootstrap/form.html' import render_form %}
                    {{ render_form(form) }}
                    ''', form=form)

        response = self.client.get('/form')
        data = response.get_data(as_text=True)
        self.assertIn('<input class="form-control" id="username" name="username"', data)
        self.assertIn('<input class="form-control" id="password" name="password"', data)

    def test_render_form_row(self):
        @self.app.route('/form')
        def test():
            form = HelloForm()
            return render_template_string('''
                    {% from 'bootstrap/form.html' import render_form_row %}
                    {{ render_form_row([form.username, form.password]) }}
                    ''', form=form)
        response = self.client.get('/form')
        data = response.get_data(as_text=True)
        self.assertIn('<div class="form-row">', data)
        self.assertIn('<div class="col">', data)

    def test_render_form_row_row_class(self):
        @self.app.route('/form')
        def test():
            form = HelloForm()
            return render_template_string('''
                    {% from 'bootstrap/form.html' import render_form_row %}
                    {{ render_form_row([form.username, form.password], row_class='row') }}
                    ''', form=form)
        response = self.client.get('/form')
        data = response.get_data(as_text=True)
        self.assertIn('<div class="row">', data)

    def test_render_form_row_col_class_default(self):
        @self.app.route('/form')
        def test():
            form = HelloForm()
            return render_template_string('''
                    {% from 'bootstrap/form.html' import render_form_row %}
                    {{ render_form_row([form.username, form.password], col_class_default='col-md-6') }}
                    ''', form=form)
        response = self.client.get('/form')
        data = response.get_data(as_text=True)
        self.assertIn('<div class="col-md-6">', data)

    def test_render_form_row_col_map(self):
        @self.app.route('/form')
        def test():
            form = HelloForm()
            return render_template_string('''
                    {% from 'bootstrap/form.html' import render_form_row %}
                    {{ render_form_row([form.username, form.password], col_map={'username': 'col-md-6'}) }}
                    ''', form=form)
        response = self.client.get('/form')
        data = response.get_data(as_text=True)
        self.assertIn('<div class="col">', data)
        self.assertIn('<div class="col-md-6">', data)

    def test_render_pager(self):
        db = SQLAlchemy(self.app)

        class Message(db.Model):
            id = db.Column(db.Integer, primary_key=True)

        @self.app.route('/pager')
        def test():
            db.drop_all()
            db.create_all()
            for i in range(100):
                m = Message()
                db.session.add(m)
            db.session.commit()
            page = request.args.get('page', 1, type=int)
            pagination = Message.query.paginate(page, per_page=10)
            messages = pagination.items
            return render_template_string('''
                            {% from 'bootstrap/pagination.html' import render_pager %}
                            {{ render_pager(pagination) }}
                            ''', pagination=pagination, messages=messages)

        response = self.client.get('/pager')
        data = response.get_data(as_text=True)
        self.assertIn('<nav aria-label="Page navigation">', data)
        self.assertIn('Previous', data)
        self.assertIn('Next', data)
        self.assertIn('<li class="page-item disabled">', data)

        response = self.client.get('/pager?page=2')
        data = response.get_data(as_text=True)
        self.assertIn('<nav aria-label="Page navigation">', data)
        self.assertIn('Previous', data)
        self.assertIn('Next', data)
        self.assertNotIn('<li class="page-item disabled">', data)

    def test_render_pagination(self):
        db = SQLAlchemy(self.app)

        class Message(db.Model):
            id = db.Column(db.Integer, primary_key=True)

        @self.app.route('/pagination')
        def test():
            db.drop_all()
            db.create_all()
            for i in range(100):
                m = Message()
                db.session.add(m)
            db.session.commit()
            page = request.args.get('page', 1, type=int)
            pagination = Message.query.paginate(page, per_page=10)
            messages = pagination.items
            return render_template_string('''
                                    {% from 'bootstrap/pagination.html' import render_pagination %}
                                    {{ render_pagination(pagination) }}
                                    ''', pagination=pagination, messages=messages)

        response = self.client.get('/pagination')
        data = response.get_data(as_text=True)
        self.assertIn('<nav aria-label="Page navigation">', data)
        self.assertIn('<a class="page-link" href="#">1 <span class="sr-only">(current)</span></a>', data)
        self.assertIn('10</a>', data)

        response = self.client.get('/pagination?page=2')
        data = response.get_data(as_text=True)
        self.assertIn('<nav aria-label="Page navigation">', data)
        self.assertIn('1</a>', data)
        self.assertIn('<a class="page-link" href="#">2 <span class="sr-only">(current)</span></a>', data)
        self.assertIn('10</a>', data)

    def test_render_nav_item(self):
        @self.app.route('/nav_item')
        def test():
            return render_template_string('''
                    {% from 'bootstrap/nav.html' import render_nav_item %}
                    {{ render_nav_item('test', 'Home') }}
                    ''')

        response = self.client.get('/nav_item')
        data = response.get_data(as_text=True)
        self.assertIn('<a class="nav-item nav-link active"', data)

    def test_render_breadcrumb_item(self):
        @self.app.route('/breadcrumb_item')
        def test():
            return render_template_string('''
                    {% from 'bootstrap/nav.html' import render_breadcrumb_item %}
                    {{ render_breadcrumb_item('test', 'Home') }}
                    ''')

        response = self.client.get('/breadcrumb_item')
        data = response.get_data(as_text=True)
        self.assertIn('<li class="breadcrumb-item active"  aria-current="page">', data)

    def test_render_static(self):
        @self.app.route('/test_static')
        def test():
            return render_template_string('''
                            {% from 'bootstrap/utils.html' import render_static %}
                            {{ render_static('css', 'test.css') }}
                            {{ render_static('js', 'test.js') }}
                            {{ render_static('icon', 'test.ico') }}
                            ''')

        response = self.client.get('/test_static')
        data = response.get_data(as_text=True)
        self.assertIn('<link rel="stylesheet" href="/static/test.css" type="text/css">', data)
        self.assertIn('<script type="text/javascript" src="/static/test.js"></script>', data)
        self.assertIn('<link rel="icon" href="/static/test.ico">', data)

    def test_render_messages(self):
        @self.app.route('/messages')
        def test_messages():
            flash('test message', 'danger')
            return render_template_string('''
                            {% from 'bootstrap/utils.html' import render_messages %}
                            {{ render_messages() }}
                            ''')

        @self.app.route('/container')
        def test_container():
            flash('test message', 'danger')
            return render_template_string('''
                            {% from 'bootstrap/utils.html' import render_messages %}
                            {{ render_messages(container=True) }}
                            ''')

        @self.app.route('/dismissible')
        def test_dismissible():
            flash('test message', 'danger')
            return render_template_string('''
                            {% from 'bootstrap/utils.html' import render_messages %}
                            {{ render_messages(dismissible=True) }}
                            ''')

        @self.app.route('/dismiss_animate')
        def test_dismiss_animate():
            flash('test message', 'danger')
            return render_template_string('''
                            {% from 'bootstrap/utils.html' import render_messages %}
                            {{ render_messages(dismissible=True, dismiss_animate=True) }}
                            ''')

        response = self.client.get('/messages')
        data = response.get_data(as_text=True)
        self.assertIn('<div class="alert alert-danger"', data)

        response = self.client.get('/container')
        data = response.get_data(as_text=True)
        self.assertIn('<div class="container flashed-messages">', data)

        response = self.client.get('/dismissible')
        data = response.get_data(as_text=True)
        self.assertIn('alert-dismissible', data)
        self.assertIn('<button type="button" class="close" data-dismiss="alert"', data)
        self.assertNotIn('fade show', data)

        response = self.client.get('/dismiss_animate')
        data = response.get_data(as_text=True)
        self.assertIn('alert-dismissible', data)
        self.assertIn('<button type="button" class="close" data-dismiss="alert"', data)
        self.assertIn('fade show', data)

    # test WTForm fields for render_form and render_field
    def test_render_form_enctype(self):
        class SingleUploadForm(FlaskForm):
            avatar = FileField('Avatar')

        class MultiUploadForm(FlaskForm):
            photos = MultipleFileField('Multiple photos')

        @self.app.route('/single')
        def single():
            form = SingleUploadForm()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form) }}
            ''', form=form)

        @self.app.route('/multi')
        def multi():
            form = SingleUploadForm()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form) }}
            ''', form=form)

        response = self.client.get('/single')
        data = response.get_data(as_text=True)
        self.assertIn('multipart/form-data', data)

        response = self.client.get('/multi')
        data = response.get_data(as_text=True)
        self.assertIn('multipart/form-data', data)

    # test render_kw class for WTForms field
    def test_form_render_kw_class(self):

        class TestForm(FlaskForm):
            username = StringField('Username')
            password = PasswordField('Password', render_kw={'class': 'my-password-class'})
            submit = SubmitField(render_kw={'class': 'my-awesome-class'})

        @self.app.route('/render_kw')
        def render_kw():
            form = TestForm()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form) }}
            ''', form=form)

        response = self.client.get('/render_kw')
        data = response.get_data(as_text=True)
        self.assertIn('class="form-control"', data)
        self.assertNotIn('class="form-control "', data)
        self.assertIn('class="form-control my-password-class"', data)
        self.assertIn('my-awesome-class', data)
        self.assertIn('btn', data)

    # test WTForm field description for BooleanField
    def test_form_description_for_booleanfield(self):

        class TestForm(FlaskForm):
            remember = BooleanField('Remember me', description='Just check this')

        @self.app.route('/description')
        def description():
            form = TestForm()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form) }}
            ''', form=form)

        response = self.client.get('/description')
        data = response.get_data(as_text=True)
        self.assertIn('Remember me', data)
        self.assertIn('<small class="form-text text-muted">Just check this</small>', data)

    def test_button_size(self):
        self.assertEqual(current_app.config['BOOTSTRAP_BTN_SIZE'], 'md')
        current_app.config['BOOTSTRAP_BTN_SIZE'] = 'lg'

        @self.app.route('/form')
        def test():
            form = HelloForm()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form) }}
            ''', form=form)

        response = self.client.get('/form')
        data = response.get_data(as_text=True)
        self.assertIn('btn-lg', data)

        @self.app.route('/form2')
        def test_overwrite():
            form = HelloForm()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form, button_size='sm') }}
            ''', form=form)

        response = self.client.get('/form2')
        data = response.get_data(as_text=True)
        self.assertNotIn('btn-lg', data)
        self.assertIn('btn-sm', data)

    def test_button_style(self):
        self.assertEqual(current_app.config['BOOTSTRAP_BTN_STYLE'], 'secondary')
        current_app.config['BOOTSTRAP_BTN_STYLE'] = 'primary'

        @self.app.route('/form')
        def test():
            form = HelloForm()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form) }}
            ''', form=form)

        response = self.client.get('/form')
        data = response.get_data(as_text=True)
        self.assertIn('btn-primary', data)

        @self.app.route('/form2')
        def test_overwrite():
            form = HelloForm()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form, button_style='success') }}
            ''', form=form)

        response = self.client.get('/form2')
        data = response.get_data(as_text=True)
        self.assertNotIn('btn-primary', data)
        self.assertIn('btn-success', data)

        @self.app.route('/form3')
        def test_button_map():
            form = HelloForm()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form, button_map={'submit': 'warning'}) }}
            ''', form=form)

        response = self.client.get('/form3')
        data = response.get_data(as_text=True)
        self.assertNotIn('btn-primary', data)
        self.assertIn('btn-warning', data)
