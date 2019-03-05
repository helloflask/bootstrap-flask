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

When development, Bootstrap-Flask provides two helper functions that can
be used to generate resources load code in template:
``bootstrap.load_css()`` and ``bootstrap.load_js()``

Call it at your template, for example:

.. code-block:: jinja

    <head>
    ....
    {{ bootstrap.load_css() }}
    </head>
    <body>
    ...
    {{ bootstrap.load_js() }}
    </body>

Starter template
-----------------

Considering for flexibility, Bootstrap-Flask did't include a built-in base templates (maybe change in future), 
for now you have to create it by yourself. Be sure to using an HTML5 doctype and including a viewport meta tag 
for proper responsive behaviors, your base template should like this:

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
        <!-- Your page contont -->
        {% block content %}{% endblock%}
        
        {% block scripts %}
        <!-- Optional JavaScript -->
        {{ bootstrap.load_js() }}
        {% endblock %}
      </body>
    </html>

You can copy it to your base template (name it as ``base.html`` or ``layout.html`` etc.), then you can inherite it
in chlid templates, see `Template Inheritance <http://flask.pocoo.org/docs/1.0/patterns/templateinheritance/>`_ for
more details.

Macros
------

+---------------------------+--------------------------------+--------------------------------------------------------------------+
| Macro                     | Templates Path                 | Description                                                        |
+===========================+================================+====================================================================+
| render_field()            | bootstrap/form.html            | Render a WTForms form field                                        |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_form()             | bootstrap/form.html            | Render a WTForms form                                              |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_pager()            | bootstrap/pagination.html      | Render a basic pagination, only include previous and next button.  |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_pagination()       | bootstrap/pagination.html      | Render a standard pagination                                       |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_nav_item()         | bootstrap/nav.html             | Render a navigation item                                           |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_breadcrumb_item()  | bootstrap/nav.html             | Render a breadcrumb item                                           |
+---------------------------+--------------------------------+--------------------------------------------------------------------+
| render_static()           | bootstrap/utils.html           | Render a resource reference code (i.e. ``<link>``, ``<script>``)   |
+---------------------------+--------------------------------+--------------------------------------------------------------------+

How to use these macros? It's quite simple, just import them from the
correspond path and then call them like any other macro:

.. code-block:: jinja

    {% from 'bootstrap/form.html' import render_form %}

    {{ render_form(form) }}

Go to :doc:`macros` page to see the detailed usage for these macros.
