# -*- coding: utf-8 -*-
from flask import Flask, render_template

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length

from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'dev'

bootstrap = Bootstrap(app)


class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(1, 200)])
    remember = BooleanField('Remember me')
    submit = SubmitField()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    return render_template('index.html', form=form)
