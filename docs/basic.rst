Basic Usage
===========

Installation
------------

.. code-block:: bash

    $ pip install bootstrap-flask

This project can't work with Flask-Bootstrap at the same time. If you have already installed Flask-Bootstrap in the same Python enviroment, you have to uninstall it and then reinstall this project:

.. code-block:: bash

    $ pip uninstall flask-bootstrap bootstrap-flask
    $ pip install bootstrap-flask

.. tip:: See :doc:`migrate` to learn how to migrate from Flask-Bootstrap.

Initialization
--------------

.. code-block:: python

    from flask_bootstrap import Bootstrap
    from flask import Flask

    app = Flask(__name__)

    bootstrap = Bootstrap(app)

Resources helpers
-----------------

Bootstrap-Flask provides two helper functions to load Bootstrap resources in the template:
``bootstrap.load_css()`` and ``bootstrap.load_js()``.

Call it in your base template, for example:

.. code-block:: jinja

    <head>
    ....
    {{ bootstrap.load_css() }}
    </head>
    <body>
    ...
    {{ bootstrap.load_js() }}
    </body>

You can pass ``version`` to pin the Bootstrap 4 version you want to use. It defaults to load files from CDN. Set ``BOOTSTRAP_SERVE_LOCAL``
to ``True`` to use built-in local files. However, these methods are optional, you can also write ``<href></href>``
and ``<script></script>`` tags to include Bootstrap resources (from your ``static`` folder or CDN) manually by yourself.

Starter template
----------------

For reasons of flexibility, Bootstrap-Flask doesn't include built-in base templates (this may change in the future). For now,  you have to create a base template yourself. Be sure to use an HTML5 doctype and include a viewport meta tag for proper responsive behaviors. Here's an example base template:

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

Use this in your templates folder (suggested names are ``base.html`` or ``layout.html`` etc.), and inherit it in child templates. See `Template Inheritance <http://flask.pocoo.org/docs/1.0/patterns/templateinheritance/>`_ for more details on inheritance.

.. _macros_list:

Macros
------

+---------------------------+--------------------------------+--------------------------------------------------------------------+
| Macro                     | Templates Path                 | Description                                                        |
+===========================+================================+====================================================================+
| render_field()            | bootstrap/form.html            | Render a WTForms form field                                        |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_form()             | bootstrap/form.html            | Render a WTForms form                                              |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_form_row()         | bootstrap/form.html            | Render a row of a grid form                                        |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_hidden_errors()    | bootstrap/form.html            | Render error messages for hidden form field                        |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_pager()            | bootstrap/pagination.html      | Render a basic Flask-SQLAlchemy pagniantion                        |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_pagination()       | bootstrap/pagination.html      | Render a standard Flask-SQLAlchemy pagination                      |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_nav_item()         | bootstrap/nav.html             | Render a navigation item                                           |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_breadcrumb_item()  | bootstrap/nav.html             | Render a breadcrumb item                                           |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_static()           | bootstrap/utils.html           | Render a resource reference code (i.e. ``<link>``, ``<script>``)   |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_messages()         | bootstrap/utils.html           | Render flashed messages send by flash() function                   |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_icon()             | bootstrap/utils.html           | Render a Bootstrap icon                                            |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_table()            | bootstrap/table.html           | Render a table with given data                                     |
+---------------------------+--------------------------------+--------------------------------------------------------------------+

How to use these macros? It's quite simple, just import them from the
corresponding path and call them like any other macro:

.. code-block:: jinja

    {% from 'bootstrap/form.html' import render_form %}

    {{ render_form(form) }}

Go to the :doc:`macros` page to see the detailed usage for these macros.

Configurations
--------------

+-----------------------------+--------------------------------+----------------------------------------------------------------------------------------------+
| Configuration Variable      | Default Value                  | Description                                                                                  |
+=============================+================================+==============================================================================================+
| BOOTSTRAP_SERVE_LOCAL       | ``False``                      | If set to ``True``, local resources will be used for ``load_*`` methods.                     |
+-----------------------------+--------------------------------+----------------------------------------------------------------------------------------------+
| BOOTSTRAP_BTN_STYLE         | ``'primary'``                  | Default form button style, will change to ``primary`` in next major release                  |
+-----------------------------+--------------------------------+----------------------------------------------------------------------------------------------+
| BOOTSTRAP_BTN_SIZE          | ``'md'``                       | Default form button size                                                                     |
+-----------------------------+--------------------------------+----------------------------------------------------------------------------------------------+
| BOOTSTRAP_ICON_SIZE         | ``'1em'``                      | Default icon size                                                                            |
+-----------------------------+--------------------------------+----------------------------------------------------------------------------------------------+
| BOOTSTRAP_ICON_COLOR        | ``None``                       | Default icon color, follow the context with ``currentColor`` if not set                      |
+-----------------------------+--------------------------------+----------------------------------------------------------------------------------------------+
| BOOTSTRAP_BOOTSWATCH_THEME  | ``None``                       | Bootswatch theme to use, see available themes at :ref:`bootswatch_theme`                     |
+-----------------------------+--------------------------------+----------------------------------------------------------------------------------------------+
| BOOTSTRAP_MSG_CATEGORY      | ``'primary'``                  | Default flash message category                                                               |
+-----------------------------+--------------------------------+----------------------------------------------------------------------------------------------+
| BOOTSTRAP_TABLE_VIEW_TITLE  | ``'View'``                     | Default title for view icon of table actions                                                 |
+-----------------------------+--------------------------------+----------------------------------------------------------------------------------------------+
| BOOTSTRAP_TABLE_EDIT_TITLE  | ``'Edit'``                     | Default title for edit icon of table actions                                                 |
+-----------------------------+--------------------------------+----------------------------------------------------------------------------------------------+
| BOOTSTRAP_TABLE_DELETE_TITLE| ``'Delete'``                   | Default title for delete icon of table actions                                               |
+-----------------------------+--------------------------------+----------------------------------------------------------------------------------------------+
| BOOTSTRAP_TABLE_NEW_TITLE   | ``'New'``                      | Default title for new icon of table actions                                                  |
+-----------------------------+--------------------------------+----------------------------------------------------------------------------------------------+

.. tip:: See :ref:`button_customizatoin` to learn how to customize form buttons.
