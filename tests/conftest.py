import pytest
from flask import Flask, render_template_string
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(8, 150)])
    remember = BooleanField('Remember me')
    submit = SubmitField()


@pytest.fixture
def hello_form():
    return HelloForm


@pytest.fixture
def bootswatch_themes():
    themes = [
        'cerulean', 'cosmo', 'cyborg', 'darkly', 'default', 'flatly',
        'journal', 'litera', 'lumen', 'lux', 'materia', 'minty', 'pulse',
        'sandstone', 'simplex', 'sketchy', 'slate', 'solar', 'spacelab',
        'superhero', 'united', 'yeti'
    ]
    return themes


@pytest.fixture(autouse=True)
def app():
    app = Flask(__name__)
    app.testing = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'for test'

    @app.route('/')
    def index():
        return render_template_string('{{ bootstrap.load_css() }}'
                                      '{{ bootstrap.load_js() }}')

    yield app


@pytest.fixture(autouse=True)
def bootstrap(app):
    yield Bootstrap(app)


@pytest.fixture
def client(app):
    context = app.test_request_context()
    context.push()

    with app.test_client() as client:
        yield client

    context.pop()