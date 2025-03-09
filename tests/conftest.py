import pytest
from flask import Flask, render_template_string
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, HiddenField, IntegerField, RadioField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = StringField('Name')
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 150)])
    remember = BooleanField('Remember me')
    hidden = HiddenField()
    submit = SubmitField()


class ClassForm(FlaskForm):
    boolean = BooleanField('Bool label', description="Bool descr",
                           render_kw={'label_class': 'text-decoration-underline',
                                      'description_class': 'text-decoration-line-through'})
    integer = IntegerField('Int label', description="Int descr",
                           render_kw={'label_class': 'text-decoration-underline',
                                      'description_class': 'text-decoration-line-through'})
    option = RadioField('Rad label',
                        description='Rad descr',
                        choices=[('one', 'One'), ('two', 'Two')],
                        render_kw={'label_class': 'text-uppercase',
                                   'radio_class': 'text-decoration-line-through',
                                   'description_class': 'text-decoration-underline'})


@pytest.fixture
def hello_form():
    return HelloForm


@pytest.fixture
def class_form():
    return ClassForm


@pytest.fixture(autouse=True)
def app():
    app = Flask(__name__)
    app.testing = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'for test'

    @app.route('/')
    def index():
        return render_template_string('{{ bootstrap.load_css() }}{{ bootstrap.load_js() }}')

    yield app


@pytest.fixture
def client(app):
    context = app.test_request_context()
    context.push()

    with app.test_client() as client:
        yield client

    context.pop()
