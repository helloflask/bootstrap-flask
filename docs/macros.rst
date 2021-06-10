Use Macros
==========

These macros will help you to generate Bootstrap-markup codes quickly and easily.

render_nav_item()
------------------
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

    :param endpoint: The endpoint used to generate URL.
    :param text: The text that will displayed on the item.
    :param badge: Badge text.
    :param use_li: Default to generate ``<a></a>``, if set to ``True``, it will generate ``<li><a></a></li>``.
    :param kwargs: Additional keyword arguments pass to ``url_for()``.


render_breadcrumb_item()
--------------------------
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

    :param endpoint: The endpoint used to generate URL.
    :param text: The text that will displayed on the item.
    :param kwargs: Additional keyword arguments pass to ``url_for()``.

render_field()
----------------

Render a form input for form field created by Flask-WTF/WTForms.

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

.. py:function:: render_field(field, form_type="basic", horizontal_columns=('lg', 2, 10), button_style="", button_size="", button_map={})

    :param field: The form field (attribute) to render.
    :param form_type: One of ``basic``, ``inline`` or ``horizontal``. See the
                     Bootstrap docs for details on different form layouts.
    :param horizontal_columns: When using the horizontal layout, layout forms
                              like this. Must be a 3-tuple of ``(column-type,
                              left-column-size, right-column-size)``.
    :param button_style: Accept Bootstrap button style name (i.e. primary, secondary, outline-success, etc.),
                    default to ``secondary`` (e.g. ``btn-secondary``). This will overwrite config ``BOOTSTRAP_BTN_STYLE``.
    :param button_size: Accept Bootstrap button size name: sm, md, lg, block, default to ``md``. This will
                    overwrite config ``BOOTSTRAP_BTN_SIZE``.
    :param button_map: A dictionary, mapping button field name to Bootstrap button style names. For example,
                      ``{'submit': 'success'}``. This will overwrite ``button_style`` and ``BOOTSTRAP_BTN_STYLE``.

.. tip:: See :ref:`button_customization` to learn how to customize form buttons.

render_form()
---------------

Render a complete form element for form object created by Flask-WTF/WTForms.

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'bootstrap/form.html' import render_form %}

    {{ render_form(form) }}

API
~~~~

.. py:function:: render_form(form,\
                    action="",\
                    method="post",\
                    extra_classes=None,\
                    role="form",\
                    form_type="basic",\
                    horizontal_columns=('lg', 2, 10),\
                    enctype=None,\
                    button_style="",\
                    button_size="",\
                    button_map={},\
                    id="",\
                    novalidate=False,\
                    render_kw={})

    :param form: The form to output.
    :param action: The URL to receive form data.
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
                    :class:`~wtforms.fields.FileField` or :class:`~wtforms.fields.MultipleFileField` is present in the form.
    :param button_style: Accept Bootstrap button style name (i.e. primary, secondary, outline-success, etc.),
                    default to ``secondary`` (e.g. ``btn-secondary``). This will overwrite config ``BOOTSTRAP_BTN_STYLE``.
    :param button_size: Accept Bootstrap button size name: sm, md, lg, block, default to ``md``. This will
                    overwrite config ``BOOTSTRAP_BTN_SIZE``.
    :param button_map: A dictionary, mapping button field name to Bootstrap button style names. For example,
                      ``{'submit': 'success'}``. This will overwrite ``button_style`` and ``BOOTSTRAP_BTN_STYLE``.
    :param id: The ``<form>`` id attribute.
    :param novalidate: Flag that decide whether add ``novalidate`` class in ``<form>``.
    :param render_kw: A dictionary, specifying custom attributes for the
                     ``<form>`` tag.

.. tip:: See :ref:`button_customizatoin` to learn how to customize form buttons.


render_hidden_errors()
----------------------

Render error messages for hidden form field (``wtforms.HiddenField``).

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'bootstrap/form.html' import render_field, render_hidden_errors %}

    <form method="post">
        {{ form.hidden_tag() }}
        {{ render_hidden_errors(form) }}
        {{ render_field(form.username) }}
        {{ render_field(form.password) }}
        {{ render_field(form.submit) }}
    </form>

API
~~~~

.. py:function:: render_hidden_errors(form)

    :param form: Form whose errors should be rendered.


render_form_row()
------------------

Render a row of a grid form with the given fields.

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'bootstrap/form.html' import render_form_row %}

    <form method="post">
        {{ form.csrf_token() }}
        {{ render_form_row([form.username, form.password]) }}
        {{ render_form_row([form.remember]) }}
        {{ render_form_row([form.submit]) }}
        {# Custom col which should use class col-md-2, and the others the defaults: #}
        {{ render_form_row([form.title, form.first_name, form.surname], col_map={'title': 'col-md-2'}) }}
        {# Custom col which should use class col-md-2 and modified col class for the default of the other fields: #}
        {{ render_form_row([form.title, form.first_name, form.surname], col_class_default='col-md-5', col_map={'title': 'col-md-2'}) }}
    </form>

API
~~~~

.. py:function:: render_form_row(fields,\
                                 row_class='form-row',\
                                 col_class_default='col',\
                                 col_map={},\
                                 button_style="",\
                                 button_size="",\
                                 button_map={})

    :param fields: An iterable of fields to render in a row.
    :param row_class: Class to apply to the div intended to represent the row, like ``form-row``
                      or ``row``
    :param col_class_default: The default class to apply to the div that represents a column
                                if nothing more specific is said for the div column of the rendered field.
    :param col_map: A dictionary, mapping field.name to a class definition that should be applied to
                            the div column that contains the field. For example: ``col_map={'username': 'col-md-2'})``
    :param button_style: Accept Bootstrap button style name (i.e. primary, secondary, outline-success, etc.),
                    default to ``secondary`` (e.g. ``btn-secondary``). This will overwrite config ``BOOTSTRAP_BTN_STYLE``.
    :param button_size: Accept Bootstrap button size name: sm, md, lg, block, default to ``md``. This will
                    overwrite config ``BOOTSTRAP_BTN_SIZE``.
    :param button_map: A dictionary, mapping button field name to Bootstrap button style names. For example,
                      ``{'submit': 'success'}``. This will overwrite ``button_style`` and ``BOOTSTRAP_BTN_STYLE``.

.. tip:: See :ref:`button_customizatoin` to learn how to customize form buttons.


render_pager()
-----------------

Render a simple pager for query pagination object created by Flask-SQLAlchemy.

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

    :param pagination: :class:`~flask_sqlalchemy.Pagination` instance.
    :param fragment: Add URL fragment into link, such as ``#comment``.
    :param prev: Symbol/text to use for the "previous page" button.
    :param next: Symbol/text to use for the "next page" button.
    :param align: Can be 'left', 'center' or 'right', default to 'left'.
    :param kwargs: Additional arguments passed to ``url_for``.


render_pagination()
--------------------

Render a standard pagination for query pagination object created by Flask-SQLAlchemy.

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
    :param fragment: Add URL fragment into link, such as ``#comment``.
    :param align: The align of the pagination. Can be 'left', 'center' or 'right', default to 'left'.
    :param kwargs: Extra attributes for the ``<ul>``-element.


render_static()
----------------
Render a resource reference code (i.e. ``<link>``, ``<script>``).

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'bootstrap/utils.html' import render_static %}

    {{ render_static('css', 'style.css') }}

API
~~~~

.. py:function:: render_static(type, filename_or_url, local=True)

    :param type: Resources type, one of ``css``, ``js``, ``icon``.
    :param filename_or_url: The name of the file, or the full URL when ``local`` set to ``False``.
    :param local: Load local resources or from the passed URL.


render_messages()
------------------

Render Bootstrap alerts for flash messages send by ``flask.flash()``.

Example
~~~~~~~~

Flash the message in your view function with ``flash(message, category)``:

.. code-block:: python

    from flask import flash

    @app.route('/test')
    def test():
        flash('a info message', 'info')
        flash('a danger message', 'danger')
        return your_template

Render the messages in your base template (normally below the navbar):

.. code-block:: jinja

    {% from 'bootstrap/utils.html' import render_messages %}

    <nav>...</nav>
    {{ render_messages() }}
    <main>...</main>

API
~~~~

.. py:function:: render_messages(messages=None,\
                    container=False,\
                    transform={...},\
                    default_category=config.BOOTSTRAP_MSG_CATEGORY,\
                    dismissible=False,\
                    dismiss_animate=False)

    :param messages: The messages to show. If not given, default to get from ``flask.get_flashed_messages(with_categories=True)``.
    :param container: If true, will output a complete ``<div class="container">`` element, otherwise just the messages each wrapped in a ``<div>``.
    :param transform: A dictionary of mappings for categories. Will be looked up case-insensitively. Default maps all Python loglevel names to Bootstrap CSS classes.
    :param default_category: If a category does not has a mapping in transform, it is passed through unchanged. ``default_category`` will be used when ``category`` is empty.
    :param dismissible: If true, will output a button to close an alert. For fully functioning dismissible alerts, you must use the alerts JavaScript plugin.
    :param dismiss_animate: If true, will enable dismiss animate when click the dismiss button.

When you call ``flash('message', 'category')``, there are 8 category options available, mapping to Bootstrap 4's alerts type:

primary, secondary, success, danger, warning, info, light, dark.

If you want to use HTML in your message body, just wrapper your message string with ``flask.Markup`` to tell Jinja it's safe:

.. code-block:: python

    from flask import flash, Markup

    @app.route('/test')
    def test():
        flash(Markup('a info message with a link: <a href="/">Click me!</a>'), 'info')
        return your_template


render_table()
--------------

Render a Bootstrap table with given data.

Example
~~~~~~~

.. code-block:: jinja

    {% from 'bootstrap/table.html' import render_table %}

    {{ render_table(data) }}

API
~~~~

.. py:function:: render_table(data,\
                              titles=None,\
                              primary_key='id',\
                              primary_key_title='#',\
                              caption=None,\
                              table_classes=None,\
                              header_classes=None,\
                              responsive=False,\
                              responsive_class='table-responsive',\
                              show_actions=False,\
                              actions_title='Actions',\
                              custom_actions=None,\
                              view_url=None,\
                              edit_url=None,\
                              delete_url=None,\
                              new_url=None,\
                              action_pk_placeholder=':id')

    :param data: An iterable of data objects to render. Can be dicts or class objects.
    :param titles: An iterable of tuples of the format (prop, label) e.g ``[('id', '#')]``, if not provided,
                will automatically detect on provided data, currently only support SQLAlchemy object.
    :param primary_key: Primary key identifier for a single row, default to ``id``.
    :param primary_key_title: Primary key title for a single row, default to ``#``.
    :param caption: A caption to attach to the table.
    :param table_classes: A string of classes to apply to the table (e.g ``'table-small table-dark'``).
    :param header_classes: A string of classes to apply to the table header (e.g ``'thead-dark'``).
    :param responsive: Whether to enable/disable table responsiveness.
    :param responsive_class: The responsive class to apply to the table. Default is ``'table-responsive'``.
    :param show_actions: Whether to display the actions column. Default is ``False``.
    :param actions_title: Title for the actions column header. Default is ``'Actions'``.
    :param custom_actions: A list of tuples for creating custom action buttons, where each tuple contains
                ('Title Text displayed on hover', 'bootstrap icon name', 'url_for()')
                (e.g.``[('Run', 'play-fill', url_for('run_report', report_id=':id'))]``).
    :param view_url: URL to use for the view action.
    :param edit_url: URL to use for the edit action.
    :param delete_url: URL to use for the delete action.
    :param new_url: URL to use for the create action (new in version 1.6.0).
    :param action_pk_placeholder: The placeholder which replaced by the primary key when build the action URLs. Default is ``':id'``.

.. tip:: The default value of ``action_pk_placeholder`` changed to ``:id`` in version 1.7.0.
    The old value (``:primary_key``) will be removed in version 2.0. Currently, you can't
    use ``int`` converter on the URL variable of primary key. 


render_icon()
-------------

Render a Bootstrap icon.

Example
~~~~~~~

.. code-block:: jinja

    {% from 'bootstrap/utils.html' import render_icon %}

    {{ render_icon('heart') }}

API
~~~~

.. py:function:: render_icon(name, size=config.BOOTSTRAP_ICON_SIZE, color=config.BOOTSTRAP_ICON_COLOR)

    :param name: The name of icon, you can find all available names at `Bootstrap Icon <https://icons.getbootstrap.com/>`_.
    :param size: The size of icon, you can pass any vaild size value (e.g. ``32``/``'32px'``, ``1.5em``, etc.), default to
                use configuration ``BOOTSTRAP_ICON_SIZE`` (default value is `'1em'`).
    :param color: The color of icon, follow the context with ``currentColor`` if not set. Accept values are Bootstrap style name
                (one of ``['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'muted']``) or any valid color
                string (e.g. ``'red'``, ``'#ddd'`` or ``'(250, 250, 250)'``), default to use configuration ``BOOTSTRAP_ICON_COLOR`` (default value is ``None``).
