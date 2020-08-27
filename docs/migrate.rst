Migrate from Flask-Bootstrap
=============================

If you come from Flask-Bootstrap, looking for an alternative that supports Bootstrap 4, well, then you
are in the right place.

Bootstrap-Flask originated as a fork of Flask-Bootstrap, but some APIs were changed, deleted and improved,
some bugs were fixed, and on top of all that, some new macros were added. This tutorial will go through all the
steps to migrate from Flask-Bootstrap.

Uninstall and Install
----------------------
Flask-Bootstrap and Bootstrap-Flask can't live together, so you have to uninstall
Flask-Bootstrap first and then install Bootstrap-Flask:

.. code-block:: bash

    $ pip uninstall flask-bootstrap
    $ pip install bootstrap-flask

if you accidentally installed both of them, you will need to uninstall them both first:

.. code-block:: bash

    $ pip uninstall flask-bootstrap bootstrap-flask
    $ pip install bootstrap-flask

If you want to use both Flask-Bootstrap and Bootstrap-Flask for different projects, you can use virtual environment.

Initialize the Extension
------------------------

The initialization of this extension is the same as with Flask-Bootstrap. The package's name is still ``flask_bootstrap``,
in order to follow the rule of Flask extension development and easy the pain of migration.

.. code-block:: python

    from flask_bootstrap import Bootstrap
    from flask import Flask

    app = Flask(__name__)

    bootstrap = Bootstrap(app)

Create Base Template
---------------------

In Flask-Bootstrap, there is a built-in base template called ``bootstrap/base.html``. This extension does not provide one. You have to create it
by yourself; an example starter is given here:

.. code-block:: html

    <!doctype html>
    <html lang="en">
        <head>
            {% block head %}
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

            {% block styles %}
                <!-- Bootstrap CSS -->
                {{ bootstrap.load_css() }}
            {% endblock %}

            <title>Your page title</title>
            {% endblock %}
        </head>
        <body>
            <!-- Your page content -->
            {% block content %}{% endblock %}

            {% block scripts %}
                <!-- Optional JavaScript -->
                {{ bootstrap.load_js() }}
            {% endblock %}
        </body>
    </html>

Just create a file called ``base.html`` inside your ``templates`` folder, copy the contents above into it. There
are two resource helper methods used in the example template above (i.e. ``bootstrap.load_css()`` and ``bootstrap.load_js()``).
They will generate ``<href></href>`` and ``<script></script>`` codes to include Bootstrap's CSS and JavaScript files. These default
to load the resources from CDN (provided by jsDelivr). If you set the configuration variable ``BOOTSTRAP_SERVE_LOCAL`` to ``True`` the local resources inside the package folder will be used instead.

It's optional to use these resources methods, you can write the codes by yourself to load Bootstrap resources in your application's
static folder, or from a different CDN provider that you want to use.

Change Template and Macro Name
-------------------------------

The template ``bootstrap/wtf.html`` changed to ``bootstrap/form.html``, some macro's name was changed too:

+---------------------------+--------------------------------+
| Old Name                  | New Name                       |
+===========================+================================+
| bootstrap/wtf.html        | bootstrap/form.html            |
+---------------------------+--------------------------------+
| quick_form()              | render_form()                  |
+---------------------------+--------------------------------+
| form_field()              | render_field()                 |
+---------------------------+--------------------------------+
| flashed_messages()        | render_messages()               |
+---------------------------+--------------------------------+

For example, you will need to change the import statement:

.. code-block:: jinja

    {% from 'bootstrap/wtf.html' import quick_form, form_field %}

to:

.. code-block:: jinja

    {% from 'bootstrap/form.html' import render_form, render_field %}

The macros below were removed (or not supported yet):

- ie8()
- icon()
- form_button()
- analytics()
- uanalytics()

There are also some new macros were introduced, check them out at :ref:`macros_list` section.
