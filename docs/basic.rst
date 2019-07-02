Basic Usage
=============

Installation
------------

.. code-block:: bash

    $ pip install bootstrap-flask

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

You can pass ``version`` to pin the Bootstrap 4 version you want to use. Default to load files from CDN, set ``BOOTSTRAP_SERVE_LOCAL``
to ``True`` to use built-in local files. However, it's recommended to manage Bootstrap resources by yourself.

Starter template
-----------------

For reasons of flexibility, Bootstrap-Flask doesn't include built-in base templates (this may change in the future). For now,  you must create it yourself. Be sure to use an HTML5 doctype and include a viewport meta tag for proper responsive behaviors. Here's an example base template:

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

Use this in your templates folder (name it as ``base.html`` or ``layout.html`` etc.), and inherit it in child templates. See `Template Inheritance <http://flask.pocoo.org/docs/1.0/patterns/templateinheritance/>`_ for more details.

Macros
------

+---------------------------+--------------------------------+--------------------------------------------------------------------+
| Macro                     | Templates Path                 | Description                                                        |
+===========================+================================+====================================================================+
| render_field()            | bootstrap/form.html            | Render a WTForms form field                                        |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_form()             | bootstrap/form.html            | Render a WTForms form                                              |
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

How to use these macros? It's quite simple, just import them from the
corresponding path and call them like any other macro:

.. code-block:: jinja

    {% from 'bootstrap/form.html' import render_form %}

    {{ render_form(form) }}

Go to the :doc:`macros` page to see the detailed usage for these macros.
