Use Macros
==========

These macros will help you to generate Bootstrap-markup codes quickly and easily.

{{ render_nav_item() }}
------------------------
Render a Bootstrap nav item.

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'bootstrap/nav.html' import render_nav_item %}

    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="navbar-nav mr-auto">
            {{ render_nav_item('index', 'Home') }}
            {{ render_nav_item('explore', 'Explore') }}
            {{ render_nav_item('about', 'About') }}
        </div>
    </nav>

API
~~~~

.. py:function:: render_nav_item(endpoint, text, badge='', use_li=False, **kwargs)

    Render a Bootstrap nav item.

    :param endpoint: The endpoint used to generate URL.
    :param text: The text that will displayed on the item.
    :param badge: Badge text.
    :param use_li: Default to generate ``<a></a>``, if set to ``True``, it will generate ``<li><a></a></li>``.
    :param kwargs: Additional keyword arguments pass to ``url_for()``.


{{ render_breadcrumb_item() }}
---------------------------------
Render a Bootstrap breadcrumb item.

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'bootstrap/nav.html' import render_breadcrumb_item %}

    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            {{ render_breadcrumb_item('home', 'Home') }}
            {{ render_breadcrumb_item('users', 'Users') }}
            {{ render_breadcrumb_item('posts', 'Posts') }}
            {{ render_breadcrumb_item('comments', 'Comments') }}
        </ol>
    </nav>

API
~~~~

.. py:function:: render_breadcrumb_item(endpoint, text, **kwargs)

    Render a Bootstrap breadcrumb item.

    :param endpoint: The endpoint used to generate URL.
    :param text: The text that will displayed on the item.
    :param kwargs: Additional keyword arguments pass to ``url_for()``.


{{ render_form() }}
---------------------
Render a form object create by Flask-WTF/WTForms.

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'bootstrap/form.html' import render_form %}

    {{ render_form(form) }}

API
~~~~

.. py:function:: render_form(form, inline=false, tooltips=false, custom=false, col_type="md", compact_tables=false, horizontal=false, horizontal_label_width=3, **kwargs)

    Outputs Bootstrap-markup for a complete Flask-WTF form.

    :param form: The form to output.
    :param inline: Whether the form should be rendered inline
    :param tooltips: Whether the error messages should appear as tooltips
    :param custom: Whether the form elements should be converted to Bootstrap custom form elements
    :param col_type: Should be one of [none, "xs", "sm", "md", "lg", "xl"]. Specifies the responsive breakpoints
    :param compact_tables: Whether to use the special "form-row" class instead of "row" when creating nested forms
    :param horizontal: Whether the form should be rendered as a horizontal form
    :param horizontal_label_width: Should be a number between 1 and 11, that specifies the label width if the form is horizontal
    :param kwargs: Specify custom attributes for the ``<form>`` tag. Sensible defaults are already set,
                  but you might want to change the "action", "method" or "id" attribute


{{ render_pager() }}
---------------------

Render a pagination object create by Flask-SQLAlchemy

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'bootstrap/pagination.html' import render_pager %}

    {{ render_pager(pagination) }}


API
~~~~

.. py:function:: render_pager(pagination,\
                      fragment='',\
                      prev=('<span aria-hidden="true">&larr;</span> Previous')|safe,\
                      next=('Next <span aria-hidden="true">&rarr;</span>')|safe,\
                      align='',\
                      **kwargs)

    Renders a simple pager for query pagination.

    :param pagination: :class:`~flask_sqlalchemy.Pagination` instance.
    :param fragment: Add url fragment into link, such as ``#comment``.
    :param prev: Symbol/text to use for the "previous page" button.
    :param next: Symbol/text to use for the "next page" button.
    :param align: Can be 'left', 'center' or 'right', default to 'left'.
    :param kwargs: Additional arguments passed to ``url_for``.


{{ render_pagination() }}
--------------------------

Render a pagination object create by Flask-SQLAlchemy.

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'bootstrap/pagination.html' import render_pagination %}

    {{ render_pagination(pagination) }}

API
~~~~

.. py:function:: render_pagination(pagination,\
                     endpoint=None,\
                     prev='«',\
                     next='»',\
                     ellipses='…',\
                     size=None,\
                     args={},\
                     fragment='',\
                     align='',\
                     **kwargs)

    Render a standard pagination for query pagination.

    :param pagination: :class:`~flask_sqlalchemy.Pagination` instance.
    :param endpoint: Which endpoint to call when a page number is clicked.
                    :func:`~flask.url_for` will be called with the given
                    endpoint and a single parameter, ``page``. If ``None``,
                    uses the requests current endpoint.
    :param prev: Symbol/text to use for the "previous page" button. If
                ``None``, the button will be hidden.
    :param next: Symbol/text to use for the "next page" button. If
                ``None``, the button will be hidden.
    :param ellipses: Symbol/text to use to indicate that pages have been
                    skipped. If ``None``, no indicator will be printed.
    :param size: Can be 'sm' or 'lg' for smaller/larger pagination.
    :param args: Additional arguments passed to :func:`~flask.url_for`. If
                ``endpoint`` is ``None``, uses :attr:`~flask.Request.args` and
                :attr:`~flask.Request.view_args`
    :param fragment: Add url fragment into link, such as ``#comment``.
    :param align: The align of the paginationi. Can be 'left', 'center' or 'right', default to 'left'.
    :param kwargs: Extra attributes for the ``<ul>``-element.


{{ render_static() }}
----------------------
Render a resource reference code (i.e. ``<link>``, ``<script>``).

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'bootstrap/utils.html' import render_static %}

    {{ render_static('css', 'style.css') }}

API
~~~~

.. py:function:: render_static(type, filename_or_url, local=True)

    Render a resource reference code (i.e. ``<link>``, ``<script>``).

    :param type: Resources type, one of ``css``, ``js``, ``icon``.
    :param filename_or_url: The name of the file, or the full url when ``local`` set to ``False``.
    :param local: Load local resources or from the passed URL.
