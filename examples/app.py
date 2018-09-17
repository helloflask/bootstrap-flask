# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, InputRequired
from wtforms.fields import *
from wtforms.fields import html5

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'dev'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

choices = list({"choice_0": "First Choice", "choice_1": "Second choice", "choice_3": "Third choice"}.items())


class CoreForm(FlaskForm):
    boolean = BooleanField("Boolean", validators=[InputRequired()])
    decimal = DecimalField("Decimal", description="Some Description!")
    date = DateField("Date")
    date_time = DateTimeField("DateTime", render_kw={"placeholder": "Test"})
    fieldlist = FieldList(StringField("FieldList (String)"), label="FieldList", min_entries=3)
    float = FloatField("Float")
    integer = IntegerField("Integer", validators=[DataRequired()])
    radio = RadioField("Radio", choices=choices)
    select = SelectField("Select", choices=choices, validators=[InputRequired()])
    select_multiple = SelectMultipleField("SelectMultiple", choices=choices)
    string = StringField("String")
    time = TimeField("Time")


class SimpleForm(FlaskForm):
    text_area = TextAreaField("TextAreaField")
    password = PasswordField("Password", validators=[DataRequired()])
    file = FileField("File")
    multiple_file = MultipleFileField("MultipleFile")
    hidden = HiddenField("Hidden")
    submit = SubmitField("Submit")


class HTML5Form(FlaskForm):
    html5_date = html5.DateField("DateField")
    html5_date_time = html5.DateTimeField("DateTimeField")
    html5_date_time_local = html5.DateTimeLocalField("DateTimeLocalField")
    html5_decimal = html5.DecimalField("DecimalField")
    html5_decimal_range = html5.DecimalRangeField("DecimalRangeField")
    html5_email = html5.EmailField("EmailField")
    html5_integer = html5.IntegerField("IntegerField")
    html5_integer_range = html5.IntegerRangeField("IntegerRangeField")
    html5_search = html5.SearchField("SearchField")
    html5_tel = html5.TelField("TelField")
    html5_time = html5.TimeField("TimeField")
    html5_url = html5.URLField("URLField")

class RecaptchaForm(FlaskForm):
    # RECAPTCHA_PUBLIC_KEY and RECAPTCHA_PRIVATE_KEY must be set in the config
    # flask_wtf_recaptcha = RecaptchaField("RecaptchaField")
    pass

class InnerForm(FlaskForm):
    email = html5.EmailField("Email")
    password = PasswordField("Password")
    boolean = BooleanField("Remember me?")

class HelloForm(CoreForm, SimpleForm, HTML5Form):
    formfield = FormField(InnerForm, label="FormField")
    fieldlist = FieldList(FormField(InnerForm), label="FormField inside FieldList", min_entries=2)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def test_form():
    form = HelloForm()
    return render_template('form.html', form=form)


@app.route('/nav', methods=['GET', 'POST'])
def test_nav():
    return render_template('nav.html')


@app.route('/pagination', methods=['GET', 'POST'])
def test_pagination():
    db.drop_all()
    db.create_all()
    for i in range(100):
        m = Message()
        db.session.add(m)
    db.session.commit()
    page = request.args.get('page', 1, type=int)
    pagination = Message.query.paginate(page, per_page=10)
    messages = pagination.items
    return render_template('pagination.html', pagination=pagination, messages=messages)


@app.route('/utils', methods=['GET', 'POST'])
def test_utils():
    return render_template('utils.html')
