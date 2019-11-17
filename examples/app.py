# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash, Markup

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, IntegerField, TextField, FormField, SelectField, FieldList
from wtforms.validators import DataRequired, Length

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'dev'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


class HelloForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 150)])
    remember = BooleanField('Remember me')
    submit = SubmitField()


class TelephoneForm(FlaskForm):
    country_code = IntegerField('Country Code')
    area_code    = IntegerField('Area Code/Exchange')
    number       = TextField('Number')


class IMForm(FlaskForm):
    protocol = SelectField(choices=[('aim', 'AIM'), ('msn', 'MSN')])
    username = TextField()


class ContactForm(FlaskForm):
    first_name   = TextField()
    last_name    = TextField()
    mobile_phone = FormField(TelephoneForm)
    office_phone = FormField(TelephoneForm)
    emails = FieldList(TextField("Email"), min_entries=3)
    im_accounts = FieldList(FormField(IMForm), min_entries=2)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def test_form():
    form = HelloForm()
    return render_template('form.html', form=form, telephone_form=TelephoneForm(), contact_form=ContactForm(), im_form=IMForm())


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


@app.route('/static', methods=['GET', 'POST'])
def test_static():
    return render_template('static.html')

@app.route('/flash', methods=['GET', 'POST'])
def test_flash():
    flash('A simple primary alert—check it out!', 'primary')
    flash('A simple secondary alert—check it out!', 'secondary')
    flash('A simple success alert—check it out!', 'success')
    flash('A simple danger alert—check it out!', 'danger')
    flash('A simple warning alert—check it out!', 'warning')
    flash('A simple info alert—check it out!', 'info')
    flash('A simple light alert—check it out!', 'light')
    flash('A simple dark alert—check it out!', 'dark')
    flash(Markup('A simple success alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.'), 'success')
    return render_template('flash.html')


if __name__ == '__main__':
    app.run(debug=True)
