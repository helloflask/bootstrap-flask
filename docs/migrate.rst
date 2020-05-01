Migrate from Flask-Bootstrap
=============================

If you come from Flask-Bootstrap, looking for an alternative that support Bootstrap 4, well, then you
are in the right palce.

Bootstrap-Flask was origined as a fork of Flask-Bootstrap, but some APIs was changed, deleted and improved,
some bugs was fixed, on top of all that, some new macros was added. This tutorial will go through all the 
work you have to do for the migration.

Uninstall and Install
----------------------
Flask-Bootstrap and Bootstrap-Flask can't live together, so you have to unisntall
Flask-Bootstrap first, then install Bootstra-Flask:

.. code-block:: bash

    $ pip uninstall flask-bootstrap
    $ pip install bootstap-flask

if you accidently installed both of them, you will need to uninstall them first:

.. code-block:: bash

    $ pip uninstall flask-bootstrap bootstrap-flask
    $ pip install bootstap-flask

if you want to use both Flask-Bootstrap and Bootstrap-Flask for different project, you can use virtual envrioment.

Initilize the Extension
------------------------

The initilization of this extension is the same with Flask-Bootstrap, the package name still be ``flask_boostrap``,
in order to follow the rule of Flask extension development and easy the pain of migration.

.. code-block:: python

    from flask_bootstrap import Bootstrap
    from flask import Flask

    app = Flask(__name__)

    bootstrap = Bootstrap(app)

Create Base Template
---------------------

In Flask-Bootstrap, there is a built-in base template called ``bootstrap/base.html``. Now you have to create it
by yourself, here is a starter example for you:

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

Just create a file called ``base.html`` inside your ``templates`` folder, copy the content above into it. There
are two resource hepler method used in the example template above (i.e. ``bootstrap.load_css()`` and ``bootstrap.load_js()``).
They will generate ``<href></href>`` and ``<script></script>`` codes to include Bootstrap's CSS and JavaScript files. Default
to load the resources from CDN (provide by jsDelivr), if you set configuration variable ``BOOTSTRAP_SERVE_LOCAL`` to ``True``,
then the local resources inside the package folder will be used.

It's optional to use these resources methods, you can write these codes by yourself to load Boostrap resoures in your application's
staic folder, or from a different CDN provider that you want to use.

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
| flashed_messages()        | render_message()               |
+---------------------------+--------------------------------+

For example, you will need to change the import statement:

.. code-block:: jinja

    {% from 'bootstrap/wtf.html' import quick_form, form_field %}

to:

.. code-block:: jinja

    {% from 'bootstrap/form.html' import render_form, render_field %}

The macros below was removed (or not supported yet):

- ie8()
- icon()
- form_button()
- analytics()
- uanalytics()
