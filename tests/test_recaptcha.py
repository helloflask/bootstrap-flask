import pytest
from bs4 import BeautifulSoup
from flask import render_template_string
from flask_wtf import FlaskForm, RecaptchaField

from flask_bootstrap import Bootstrap4, Bootstrap5


@pytest.fixture(params=[Bootstrap4, Bootstrap5])
def bootstrap(app, request):
    return request.param(app)


@pytest.mark.parametrize('form_type', ['basic', 'inline', 'horizontal'])
@pytest.mark.parametrize('div_class', [None, 'h-captcha'])
@pytest.mark.parametrize('macro', ['render_field', 'render_form', 'render_form_row'])
def test_recaptcha_class(app, client, bootstrap, form_type, div_class, macro):
    app.config['RECAPTCHA_PUBLIC_KEY'] = 'test-public-key'
    if div_class is not None:
        app.config['RECAPTCHA_DIV_CLASS'] = div_class

    class CaptchaForm(FlaskForm):
        captcha = RecaptchaField('Captcha')

    argument = {'render_field': 'form.captcha', 'render_form': 'form',
                'render_form_row': '[form.captcha]'}[macro]
    template = (
        '{% from "bootstrap' + bootstrap.bootstrap_version[0] + '/form.html" import ' + macro + ' %}'
        '{{ ' + macro + '(' + argument + ', form_type=form_type) }}'
    )
    data = render_template_string(template, form=CaptchaForm(), form_type=form_type)
    captcha = BeautifulSoup(data, 'html.parser').find('div', attrs={'data-sitekey': 'test-public-key'})

    assert captcha['class'] == [div_class or 'g-recaptcha']
    assert captcha['data-sitekey'] == 'test-public-key'


@pytest.mark.parametrize('class_source', ['render_kw', 'class', 'class_'])
def test_recaptcha_explicit_class(app, client, bootstrap, class_source):
    app.config['RECAPTCHA_PUBLIC_KEY'] = 'test-public-key'
    app.config['RECAPTCHA_DIV_CLASS'] = 'configured-captcha'

    class CaptchaForm(FlaskForm):
        captcha = RecaptchaField(render_kw={'class': 'field-captcha'})

    kwargs = {} if class_source == 'render_kw' else {class_source: 'custom-captcha'}
    template = (
        '{% from "bootstrap' + bootstrap.bootstrap_version[0] + '/form.html" import render_field %}'
        '{{ render_field(form.captcha, data_theme="dark", **kwargs) }}'
    )
    form = CaptchaForm()
    data = render_template_string(template, form=form, kwargs=kwargs)
    captcha = BeautifulSoup(data, 'html.parser').find('div', attrs={'data-sitekey': 'test-public-key'})

    # Older Flask-WTF widgets ignore render kwargs; preserve their behavior too.
    expected_kwargs = {} if class_source == 'render_kw' else {'class': 'custom-captcha'}
    expected = BeautifulSoup(str(form.captcha(data_theme='dark', **expected_kwargs)), 'html.parser').find('div')
    assert captcha.attrs == expected.attrs


@pytest.mark.parametrize('form_type', ['basic', 'inline', 'horizontal'])
def test_recaptcha_error_feedback(app, client, bootstrap, form_type):
    app.config['RECAPTCHA_PUBLIC_KEY'] = 'test-public-key'

    class CaptchaForm(FlaskForm):
        captcha = RecaptchaField('Captcha', description='Complete the challenge')

    form = CaptchaForm()
    form.captcha.errors = ['Captcha failed']
    template = (
        '{% from "bootstrap' + bootstrap.bootstrap_version[0] + '/form.html" import render_field %}'
        '{{ render_field(form.captcha, form_type=form_type) }}'
    )
    data = render_template_string(template, form=form, form_type=form_type)
    html = BeautifulSoup(data, 'html.parser')

    assert html.find('div', attrs={'data-sitekey': 'test-public-key'})['class'] == ['g-recaptcha']
    assert html.find('label', attrs={'for': 'captcha'}).get_text() == 'Captcha'
    if form_type != 'inline':
        assert html.find(class_='invalid-feedback').get_text() == 'Captcha failed'
