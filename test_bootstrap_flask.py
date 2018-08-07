import unittest

from flask import Flask, render_template_string, current_app, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
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

    def test_local_resources_when_dev(self):
        current_app.config['ENV'] = 'development'

        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertNotIn('https://cdn.jsdelivr.net/npm/bootstrap', data)
        self.assertIn('bootstrap.min.js', data)
        self.assertIn('bootstrap.min.css', data)

        css_response = self.client.get('/bootstrap/static/css/bootstrap.min.css')
        js_response = self.client.get('/bootstrap/static/js/bootstrap.min.js')
        self.assertNotEqual(css_response.status_code, 404)
        self.assertNotEqual(js_response.status_code, 404)

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
