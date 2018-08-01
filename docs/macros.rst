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

{{ render_field() }}
---------------------

Render a form field create by Flask-WTF/WTForms.

Example
~~~~~~~~
.. code-block:: jinja

    {% from 'bootstrap/form.html' import render_field %}

    <form method="post">
        {{ form.csrf_token() }}
        {{ render_field(form.username) }}
        {{ render_field(form.password) }}
        {{ render_field(form.submit) }}
    </form>

API
~~~~

.. py:function:: render_field(field, form_type="basic", horizontal_columns=('lg', 2, 10), button_map={})

    Render a single form field.

    :param field: The form field (attribute) to render.
    :param form_type: One of ``basic``, ``inline`` or ``horizontal``. See the
                     Bootstrap docs for details on different form layouts.
    :param horizontal_columns: When using the horizontal layout, layout forms
                              like this. Must be a 3-tuple of ``(column-type,
                              left-column-size, right-column-size)``.
    :param button_map: A dictionary, mapping button field names to Bootstrap category names such as
                      ``primary``, ``danger`` or ``success``. Buttons not found
                      in the ``button_map`` will use the ``secondary`` type of
                      button.


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

.. py:function:: quick_form(form,\
                    action="",\
                    method="post",\
                    extra_classes=None,\
                    role="form",\
                    form_type="basic",\
                    horizontal_columns=('lg', 2, 10),\
                    enctype=None,\
                    button_map={},\
                    id="",\
                    novalidate=False,\
                    render_kw={})

    Outputs Bootstrap-markup for a complete Flask-WTF form.

    :param form: The form to output.
    :param method: ``<form>`` method attribute.
    :param extra_classes: The classes to add to the ``<form>``.
    :param role: ``<form>`` role attribute.
    :param form_type: One of ``basic``, ``inline`` or ``horizontal``. See the
                     Bootstrap docs for details on different form layouts.
    :param horizontal_columns: When using the horizontal layout, layout forms
                              like this. Must be a 3-tuple of ``(column-type,
                              left-column-size, right-column-size)``.
    :param enctype: ``<form>`` enctype attribute. If ``None``, will
                    automatically be set to ``multipart/form-data`` if a
                    :class:`~wtforms.fields.FileField` is present in the form.
    :param button_map: A dictionary, mapping button field names to names such as
                      ``primary``, ``danger`` or ``success``. Buttons not found
                      in the ``button_map`` will use the ``default`` type of
                      button.
    :param id: The ``<form>`` id attribute.
    :param novalidate: Flag that decide whether add ``novalidate`` class in ``<form>``.
    :param render_kw: A dictionary, specifying custom attributes for the
                     ``<form>`` tag.

.. py:function:: form_errors(form, hiddens=True)

    Renders paragraphs containing form error messages. This is usually only used
    to output hidden field form errors, as others are attached to the form
    fields.

    :param form: Form whose errors should be rendered.
    :param hiddens: If ``True``, render errors of hidden fields as well. If
                   ``'only'``, render *only* these.


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
