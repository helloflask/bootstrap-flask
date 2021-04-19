from flask import render_template_string
from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField
from wtforms.validators import DataRequired


def test_render_hidden_errors(app, client):
    class TestForm(FlaskForm):
        hide = HiddenField('Hide', validators=[DataRequired('Hide field is empty.')])
        submit = SubmitField()

    @app.route('/error', methods=['GET', 'POST'])
    def error():
        form = TestForm()
        if form.validate_on_submit():
            pass
        return render_template_string('''
        {% from 'bootstrap/form.html' import render_field, render_hidden_errors %}
        <form method="post">
            {{ form.hidden_tag() }}
            {{ render_hidden_errors(form) }}
            {{ render_field(form.submit) }}
        </form>
        ''', form=form)

    response = client.post('/error', follow_redirects=True)
    data = response.get_data(as_text=True)
    assert 'Hide field is empty.' in data
