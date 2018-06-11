# -*- coding: utf-8 -*-
from flask import Flask, render_template

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length

from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'dev'

bootstrap = Bootstrap(app)


class HelloForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 150)])
    remember = BooleanField('Remember me')
    submit = SubmitField()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    return render_template('index.html', form=form)


@app.route('/form', methods=['GET', 'POST'])
def test_form():
    form = HelloForm()
    return render_template('form.html', form=form)


@app.route('/nav', methods=['GET', 'POST'])
def test_nav():
    form = HelloForm()
    return render_template('nav.html', form=form)


@app.route('/pagination', methods=['GET', 'POST'])
def test_pagination():
    form = HelloForm()
    return render_template('pagination.html', form=form)


@app.route('/utils', methods=['GET', 'POST'])
def test_utils():
    form = HelloForm()
    return render_template('utils.html', form=form)
