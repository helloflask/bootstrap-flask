# Bootstrap-Flask

![PyPI - License](https://img.shields.io/pypi/l/bootstrap-flask)
[![Current version on PyPI](https://img.shields.io/pypi/v/bootstrap-flask)](https://pypi.org/project/bootstrap-flask/)
[![Build status](https://github.com/helloflask/bootstrap-flask/workflows/build/badge.svg)](https://github.com/helloflask/bootstrap-flask/actions)
[![Coverage Status](https://coveralls.io/repos/github/helloflask/bootstrap-flask/badge.svg?branch=master)](https://coveralls.io/github/helloflask/bootstrap-flask?branch=master)
[![Open Collective](https://img.shields.io/opencollective/all/bootstrap-flask)](https://opencollective.com/bootstrap-flask)

Bootstrap-Flask is a collection of Jinja macros for Bootstrap 4 & 5 and Flask. It helps you to
render Flask-related data and objects to Bootstrap markup HTML more easily:

- Render Flask-WTF/WTForms form object to Bootstrap Form.
- Render data objects (dict or class objects) to Bootstrap Table.
- Render Flask-SQLAlchemy `Pagination` object to Bootstrap Pagination.
- etc.


## Installation

```
$ pip install -U bootstrap-flask
```

## Example

Register the extension:

```python
from flask import Flask
# To follow the naming rule of Flask extension, although
# this project's name is Bootstrap-Flask, the actual package
# installed is named `flask_bootstrap`.
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)
```

Assuming you have a Flask-WTF form like this:

```python
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 150)])
    remember = BooleanField('Remember me')
    submit = SubmitField()
```

Now with the `render_form` macro:

```html
{% from 'bootstrap5/form.html' import render_form %}
<html>
<head>
<!-- Bootstrap CSS -->
</head>
<body>

<h2>Login</h2>
{{ render_form(form) }}

<!-- Bootstrap JS -->
</body>
</html>
```

You will get a form like this with only one line code (i.e. `{{ render_form(form) }}`):

![form rendering](./docs/_static/form-example.png)

When the validation fails, the error messages will be rendered with proper style:

![error form rendering](./docs/_static/error-form-example.png)

Read the [Basic Usage](https://bootstrap-flask.readthedocs.io/en/stable/basic) 
docs for more details.


## Live demo

https://bootstrap-flask-example.azurewebsites.net/


## Donate

If you find Bootstrap-Flask useful, please consider
[donating today](https://opencollective.com/bootstrap-flask/donate). Your donation keeps
Bootstrap-Flask maintained and updated with Bootstrap.


## Links

- [Documentation](https://bootstrap-flask.readthedocs.io)
- [Example Application](https://github.com/helloflask/bootstrap-flask/tree/master/examples)
- [PyPI Releases](https://pypi.org/project/Bootstrap-Flask/)
- [Changelog](https://github.com/helloflask/bootstrap-flask/blob/master/CHANGES.rst)
- [Discussions](https://github.com/helloflask/bootstrap-flask/discussions)


## Notes for Bootstrap 4 & 5 support

The Bootstrap 5 support is added in Bootstrap-Flask 2.0 version. Now you can use
the separate extension class for different Bootstrap major versions.

For Bootstrap 4, use the `Bootstrap4` class:

```python
from flask_bootstrap import Bootstrap4

# ...
bootstrap = Bootstrap4(app)
```

and import macros from the template path `bootstrap4/`:

```html
{% from 'bootstrap4/form.html' import render_form %}
```

For Bootstrap 5, use the `Bootstrap5` class:

```python
from flask_bootstrap import Bootstrap5

# ...
bootstrap = Bootstrap5(app)
```

and import macros from the template path `bootstrap5/`:

```html
{% from 'bootstrap5/form.html' import render_form %}
```

The `Bootstrap` class and `bootstrap/` template path are deprecated since 2.0
and will be removed in 3.0.


## Migration from Flask-Bootstrap

If you come from Flask-Bootstrap, check out
[this tutorial](https://bootstrap-flask.readthedocs.io/en/stable/migrate/) on how to
migrate to this extension.


## Contributing

For guidance on setting up a development environment and how to make a
contribution to Bootstrap-Flask, see the
[development documentation](https://bootstrap-flask.readthedocs.io/en/stable/#development)
and Flask's
[contributing guidelines](https://github.com/pallets/flask/blob/main/CONTRIBUTING.rst).


## License

This project is licensed under the MIT License (see the `LICENSE` file for
details). Some macros were part of Flask-Bootstrap and were modified under
the terms of its BSD License.
