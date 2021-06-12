Changelog
=========


2.0.0
-----

Release date: -

- Drop Python 2 and 3.5 support.


1.7.1
-----

Release date: -

- Fix bootswatch theme bug: remove theme name ``'default'`` (`#141 <https://github.com/greyli/bootstrap-flask/pull/141>`__).
- Add configuration ``BOOTSTRAP_TABLE_VIEW_TITLE``, ``BOOTSTRAP_TABLE_EDIT_TITLE``,
``BOOTSTRAP_TABLE_DELETE_TITLE``, ``BOOTSTRAP_TABLE_NEW_TITLE`` to support changing
the icon title of table actions.


1.7.0
-----

Release date: 2021/6/10

- Add a ``custom_actions`` parameter for the ``render_table`` macro. When passing a
list of tuples ``[(title, bootstrap icon, link)]`` to the ``custom_actions`` parameter,
the ``render_table`` macro will create an icon (link) on the action column for each
tuple in the list. The title text (first index of each tuple) will show when hovering
over each ``custom_actions`` button (`#134 <https://github.com/greyli/bootstrap-flask/pull/134>`__).
- Update Bootstrap Icons to v1.5.0.
- Improve action icons for ``render_table``, now the icons can be styled with the
``action-icon`` CSS class (`#137 <https://github.com/greyli/bootstrap-flask/pull/137>`__).
- Change the default ``action_pk_placeholder`` to ``':id'``. The support to the old
value will be removed in version 2.0
(`#138 <https://github.com/greyli/bootstrap-flask/pull/138>`__).


1.6.0
-----

Release date: 2021/5/29

- Add a ``new_url`` parameter for the ``render_table`` macro. When passing an URL to the ``new_url`` parameter, the ``render_table`` macro will create an icon (link) on the action header  (`#133 <https://github.com/greyli/bootstrap-flask/pull/133>`__).
- Fix the display of the delete icon for ``render_table`` macro (`#132 <https://github.com/greyli/bootstrap-flask/pull/132>`__).


1.5.3
-----

Release date: 2021/5/18

- Fix class for horizontal form label (`#131 <https://github.com/greyli/bootstrap-flask/pull/131>`__).
- Fix hidden field label issue for ``render_field`` macro (`#130 <https://github.com/greyli/bootstrap-flask/pull/130>`__).
- Refactor tests (`#125 <https://github.com/greyli/bootstrap-flask/pull/125>`__).


1.5.2
-----

Release date: 2021/4/13

- Fix `render_table` macro for SQLAlchemy >= 1.4 (`#124 <https://github.com/greyli/bootstrap-flask/issues/124>`__).


1.5.1
-----

Release date: 2020/11/9

- Fix missing end angle bracket for bootswatch CSS link tag (`#110 <https://github.com/greyli/bootstrap-flask/issues/110>`__).
- Migrate tests to pytest (`#109 <https://github.com/greyli/bootstrap-flask/pull/109>`__).


1.5
---

Release date: 2020/8/30

- Fix ``tox`` broken environments.
- Fix ``ResourceWarning`` in ``test_local_resources`` (`#78 <https://github.com/greyli/bootstrap-flask/pull/78>`__).
- Fix ``IndexError`` when using ``render_table`` with empty data (`#75 <https://github.com/greyli/bootstrap-flask/issues/75>`__).
- Add support for actions column in ``render_table`` macro (`#76 <https://github.com/greyli/bootstrap-flask/issues/76>`__).
- Add support for Bootswatch theme via configuration ``BOOTSTRAP_BOOTSWATCH_THEME`` (`#88 <https://github.com/greyli/bootstrap-flask/pull/88>`__).
- Fix checkbox render issue: add ``for`` attribute to link ``<label>`` with checkbox, only add ``is-invalid`` class when there are errors.
- Change default button style class from ``btn-secondary`` to ``btn-primary`` (`#62 <https://github.com/greyli/bootstrap-flask/issues/62>`__).
- Deprecated ``form_errors`` macro and it will be removed in 2.0, add ``render_hidden_errors`` macro as replacement.
- Add ``render_icon`` macro to render Bootstrap icon with Bootstrap Icon SVG Sprite (`#99 <https://github.com/greyli/bootstrap-flask/pull/99>`__).
- Add configuration ``BOOTSTRAP_MSG_CATEGORY`` to set default message category.


1.4
---

Release date: 2020/6/15

- Add ``render_table`` macro to render a Bootstrap table (`#71 <https://github.com/greyli/bootstrap-flask/pull/71>`__).


1.3.2
-----

Release date: 2020/5/30

- Support display error message for ``RadioField`` and ``BooleanField``, display description for ``RadioField``.


1.3.1
-----

Release date: 2020/4/29

- Fix add ``field.render_kw.class`` to form label class attribute.
- Fix append extra space in class attribute when no ``field.render_kw.class`` presents (`#63 <https://github.com/greyli/bootstrap-flask/issues/63>`__).

1.3.0
-----

Release date: 2020/4/23

- Fix ``enctype`` attribute setting for WTForms ``MultipleFileField`` (`Flask-Bootstrap #198<https://github.com/mbr/flask-bootstrap/issues/198>`__).
- Fix WTForms field class append bug when using ``render_kw={'class': 'my-class'}`` (`#53 <https://github.com/greyli/bootstrap-flask/issues/53>`__).
- Fix WTForms field description not showing for ``BooleanField`` (`Flask-Bootstrap #197<https://github.com/mbr/flask-bootstrap/issues/197>`__).
- Add configuration variable ``BOOTSTRAP_BTN_STYLE``(default to ``primary``) and ``BOOTSTRAP_BTN_SIZE``(default to ``md``) to set default form button style and size globally.
- Add parameter ``button_style`` and ``button_map`` for ``render_form`` and ``render_field`` to set button style and size.

1.2.0
-----

Release date: 2019/12/5

- Add macro ``render_messages`` for rendering flashed messages.
- Fix rendering bug for WTForms ``FormField`` (`#34 <https://github.com/greyli/bootstrap-flask/issues/34>`__).

1.1.0
-----

Release date: 2019/9/9

- Update Bootstrap version to 4.3.1


1.0.10
------

Release date: 2019/3/7

- Added macro ``render_form_row`` for rendering a row of a bootstrap grid form.


1.0.9
-----

Release date: 2018/11/14

- Fix missing error message when form type was horizontal.
- Fix missing input label for RadioField.
- Fix RadioField grid when form type was horizontal.


1.0.8
-----

Release date: 2018/9/6

- Correct macro name used in ``templates/bootstrap/form.html``: ``form_field`` --> ``render_field``.


1.0.7
-----

Release date: 2018/8/30

- Built-in resources loading not based on``FLASK_ENV``.


1.0.6
------

Release date: 2018/8/7

- Fix unmatched built-in jQuery filename. (`#8 <https://github.com/greyli/bootstrap-flask/issues/8>`__)

1.0.5
------

Release date: 2018/8/7

- Fix KeyError Exception if ENV isn't defined. (`#7 <https://github.com/greyli/bootstrap-flask/pull/7>`__)


1.0.4
-----

Release date: 2018/7/24

-  Add missing ``<script>`` tag in resources URL. (`#3 <https://github.com/greyli/bootstrap-flask/issues/3>`__)

1.0.3
-----

Release date: 2018/7/22

-  Built-in resources will be used when ``FLASK_ENV`` set to ``development``.
-  Change CDN provider to jsDelivr.

1.0.2
-----

Release date: 2018/7/21

-  Include ``popper.js`` before ``bootstrap.js`` in ``bootstrap.load_js()``. (`#2 <https://github.com/greyli/bootstrap-flask/issues/2>`__)

1.0.1
-----

Release date: 2018/7/1

-  Fix local resources path error
-  Add basic unit tests

1.0
---

Release date: 2018/6/11

Initial release.
