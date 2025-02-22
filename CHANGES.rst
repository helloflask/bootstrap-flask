Changelog
=========

- Reduced icon whitespace and support for classes.
- Upgrade to Bootstrap Icons 1.11.3.

2.4.1
-----

Release date: 2024/10/3

- Fix the badge classes in the ``render_nav_item`` macro for Bootstrap 5.
- Add ``_badge_classes`` param to the ``render_nav_item`` macro to set badge classes.
- Support ``bootswatch_theme`` as parameter to ``load_css``.

2.4.0
-----

Release date: 2024/4/7

- Test against Python 3.12.
- Replaced deprecated color "muted" with "secondary" (`#340 <https://github.com/helloflask/bootstrap-flask/pull/340>`__).
- Adding ``body_classes`` parameter to ``render_table`` (`#350 <https://github.com/helloflask/bootstrap-flask/pull/350>`__).
- Migrate setup.py to pyproject.toml.


2.3.3
-----

Release date: 2023/11/30

- Upgrade to Bootstrap Icons 1.11.2.


2.3.2
-----

Release date: 2023/10/11

- Fix the incorrect JS file integrity value.


2.3.1
-----

Release date: 2023/10/11

- Upgrade to Bootstrap 5.3.2, Bootswatch 5.3.1, and Bootstrap Icons 1.11.1.
- Set up the Azure web app for the example application.


2.3.0
-----

Release date: 2023/7/24

- Drop Python 3.7 support, and test against Python 3.11.
- Render enums in tables by their labels.
- Support creating action URLs for dict data (`#268 <https://github.com/helloflask/bootstrap-flask/issues/268>`__).
- Upgrade to Bootstrap 5.3.0, Bootstrap Icons 1.10.5, and Popper 2.11.8.


2.2.0
-----

Release date: 2022/11/20

- Drop Python 3.6 support, and test against Python 3.10.
- Add support for strict Content Security Policy (CSP) (`#252 <https://github.com/helloflask/bootstrap-flask/pull/252>`__)
- Upgrade to Bootstrap 5.2.2, Popper 2.11.6, Bootswatch 5.2.2, and Bootstrap Icons 1.9.1.
- Fix Flask-SQLAlchemy ``paginate`` named parameters in tests and examples.
- Support to preview available Bootswatch theme in the example application.
- Remove ``.DS_Store`` files from the distribution files.


2.1.0
-----

Release date: 2022/8/20

- Add ``safe_columns`` and ``urlize_columns`` parameters to ``render_table`` macro
  to support rendering table column as HTML/URL (`#204 <https://github.com/helloflask/bootstrap-flask/pull/204>`__).
- Rename the ``badge`` parameter of ``render_nav_item`` macro to ``_badge``.
- Rename the ``use_li`` parameter of ``render_nav_item`` macro to ``_use_li``.


2.0.2
-----

Release date: 2022/2/27

- Add the missing ``form-select`` class for Bootstrap 5 form select fields
  (`#211 <https://github.com/helloflask/bootstrap-flask/pull/211>`__).


2.0.1
-----

Release date: 2022/1/27

- Remove extra quotation mark in ``render_nav_item``
  (`#201 <https://github.com/helloflask/bootstrap-flask/pull/201>`__).
- Fix signature of ``Bootstrap.__init__()`` incompatible with older version
  (`#198 <https://github.com/helloflask/bootstrap-flask/pull/198>`__).


2.0.0
-----

Release date: 2022/1/13

- Drop Python 2 and 3.5 support.
- Combine ``class`` argument of ``render_field`` or ``field.render_kw.class`` with Bootstrap classes
  (`#159 <https://github.com/helloflask/bootstrap-flask/pull/159>`__).
- Add initial support for Bootstrap 5 (`#161 <https://github.com/helloflask/bootstrap-flask/pull/161>`__):
    - Add ``Bootstrap4`` class and deprecate ``Bootstrap``.
    - Add ``Bootstrap5`` class for Bootstrap 5 support.
    - Move Bootstrap 4-related files to ``bootstrap4`` subfolder, and deprecate template path ``bootstrap/``.
    - Bootstrap 4 macros are in the ``bootstrap4/`` template folder, and Bootstrap 5 macros are in ``bootstrap5/``.
    - Add separate tests, templates, static files, and examples for Bootstrap 5.
- Remove the deprecated ``form_errors`` macro and the URL string variable support in ``render_table``.
- Render boolean field as a Bootstrap switch with ``SwitchField`` class (`#175 <https://github.com/helloflask/bootstrap-flask/pull/175>`__).
- Add ``BOOTSTRAP_FORM_GROUP_CLASSES`` config for Bootstrap 5, defaults to ``mb-3``. Also add a ``form_group_classes``
  parameter for ``render_form``, ``render_field``, and ``render_form_row`` (`#184 <https://github.com/helloflask/bootstrap-flask/pull/184>`__).
- Add ``BOOTSTRAP_FORM_INLINE_CLASSES`` config for Bootstrap 5, defaults to ``row row-cols-lg-auto g-3 align-items-center``.
  Also add a ``form_inline_classes`` parameter for ``render_form`` (`#184 <https://github.com/helloflask/bootstrap-flask/pull/184>`__).
- Add ``form_type`` and ``horizontal_columns`` parameters to ``render_form_row`` (`#192 <https://github.com/helloflask/bootstrap-flask/pull/192>`__).
- Add support for WTForms range fields (``DecimalRangeField`` and ``IntegerRangeField``) (`#194 <https://github.com/helloflask/bootstrap-flask/pull/194>`__).
- Bump Bootstrap Icons to v1.7.2.
- Bump Bootstrap & Bootswatch to 4.6.1/5.1.3.


1.8.0
-----

Release date: 2021/9/5

- Fix bootswatch theme bug: remove theme name ``'default'`` (`#141 <https://github.com/helloflask/bootstrap-flask/pull/141>`__).
- Add configuration ``BOOTSTRAP_TABLE_VIEW_TITLE``, ``BOOTSTRAP_TABLE_EDIT_TITLE``,
  ``BOOTSTRAP_TABLE_DELETE_TITLE``, ``BOOTSTRAP_TABLE_NEW_TITLE`` to support changing
  the icon title of table actions (`#140 <https://github.com/helloflask/bootstrap-flask/pull/140>`__).
- Introduce a new and better way to pass table action URLs
  (`#146 <https://github.com/helloflask/bootstrap-flask/pull/146>`__, `#151 <https://github.com/helloflask/bootstrap-flask/pull/151>`__).
- Deprecate ``action_pk_placeholder`` and placeholder action URLs in ``render_table``.
- Support SRI for JS/CSS resources (`#142 <https://github.com/helloflask/bootstrap-flask/pull/142>`__).


1.7.0
-----

Release date: 2021/6/10

- Add a ``custom_actions`` parameter for the ``render_table`` macro. When passing a
  list of tuples ``[(title, bootstrap icon, link)]`` to the ``custom_actions`` parameter,
  the ``render_table`` macro will create an icon (link) on the action column for each
  tuple in the list. The title text (first index of each tuple) will show when hovering
  over each ``custom_actions`` button (`#134 <https://github.com/helloflask/bootstrap-flask/pull/134>`__).
- Update Bootstrap Icons to v1.5.0.
- Improve action icons for ``render_table``, now the icons can be styled with the
  ``action-icon`` CSS class (`#137 <https://github.com/helloflask/bootstrap-flask/pull/137>`__).
- Change the default ``action_pk_placeholder`` to ``':id'``. The support to the old
  value will be removed in version 2.0
  (`#138 <https://github.com/helloflask/bootstrap-flask/pull/138>`__).


1.6.0
-----

Release date: 2021/5/29

- Add a ``new_url`` parameter for the ``render_table`` macro. When passing an URL to the ``new_url`` parameter, the ``render_table`` macro will create an icon (link) on the action header  (`#133 <https://github.com/helloflask/bootstrap-flask/pull/133>`__).
- Fix the display of the delete icon for ``render_table`` macro (`#132 <https://github.com/helloflask/bootstrap-flask/pull/132>`__).


1.5.3
-----

Release date: 2021/5/18

- Fix class for horizontal form label (`#131 <https://github.com/helloflask/bootstrap-flask/pull/131>`__).
- Fix hidden field label issue for ``render_field`` macro (`#130 <https://github.com/helloflask/bootstrap-flask/pull/130>`__).
- Refactor tests (`#125 <https://github.com/helloflask/bootstrap-flask/pull/125>`__).


1.5.2
-----

Release date: 2021/4/13

- Fix `render_table` macro for SQLAlchemy >= 1.4 (`#124 <https://github.com/helloflask/bootstrap-flask/issues/124>`__).


1.5.1
-----

Release date: 2020/11/9

- Fix missing end angle bracket for bootswatch CSS link tag (`#110 <https://github.com/helloflask/bootstrap-flask/issues/110>`__).
- Migrate tests to pytest (`#109 <https://github.com/helloflask/bootstrap-flask/pull/109>`__).


1.5
---

Release date: 2020/8/30

- Fix ``tox`` broken environments.
- Fix ``ResourceWarning`` in ``test_local_resources`` (`#78 <https://github.com/helloflask/bootstrap-flask/pull/78>`__).
- Fix ``IndexError`` when using ``render_table`` with empty data (`#75 <https://github.com/helloflask/bootstrap-flask/issues/75>`__).
- Add support for actions column in ``render_table`` macro (`#76 <https://github.com/helloflask/bootstrap-flask/issues/76>`__).
- Add support for Bootswatch theme via configuration ``BOOTSTRAP_BOOTSWATCH_THEME`` (`#88 <https://github.com/helloflask/bootstrap-flask/pull/88>`__).
- Fix checkbox render issue: add ``for`` attribute to link ``<label>`` with checkbox, only add ``is-invalid`` class when there are errors.
- Change default button style class from ``btn-secondary`` to ``btn-primary`` (`#62 <https://github.com/helloflask/bootstrap-flask/issues/62>`__).
- Deprecated ``form_errors`` macro and it will be removed in 2.0, add ``render_hidden_errors`` macro as replacement.
- Add ``render_icon`` macro to render Bootstrap icon with Bootstrap Icon SVG Sprite (`#99 <https://github.com/helloflask/bootstrap-flask/pull/99>`__).
- Add configuration ``BOOTSTRAP_MSG_CATEGORY`` to set default message category.


1.4
---

Release date: 2020/6/15

- Add ``render_table`` macro to render a Bootstrap table (`#71 <https://github.com/helloflask/bootstrap-flask/pull/71>`__).


1.3.2
-----

Release date: 2020/5/30

- Support display error message for ``RadioField`` and ``BooleanField``, display description for ``RadioField``.


1.3.1
-----

Release date: 2020/4/29

- Fix add ``field.render_kw.class`` to form label class attribute.
- Fix append extra space in class attribute when no ``field.render_kw.class`` presents (`#63 <https://github.com/helloflask/bootstrap-flask/issues/63>`__).


1.3.0
-----

Release date: 2020/4/23

- Fix ``enctype`` attribute setting for WTForms ``MultipleFileField`` (`Flask-Bootstrap #198 <https://github.com/mbr/flask-bootstrap/issues/198>`__).
- Fix WTForms field class append bug when using ``render_kw={'class': 'my-class'}`` (`#53 <https://github.com/helloflask/bootstrap-flask/issues/53>`__).
- Fix WTForms field description not showing for ``BooleanField`` (`Flask-Bootstrap #197 <https://github.com/mbr/flask-bootstrap/issues/197>`__).
- Add configuration variable ``BOOTSTRAP_BTN_STYLE``(default to ``primary``) and ``BOOTSTRAP_BTN_SIZE``(default to ``md``) to set default form button style and size globally.
- Add parameter ``button_style`` and ``button_map`` for ``render_form`` and ``render_field`` to set button style and size.


1.2.0
-----

Release date: 2019/12/5

- Add macro ``render_messages`` for rendering flashed messages.
- Fix rendering bug for WTForms ``FormField`` (`#34 <https://github.com/helloflask/bootstrap-flask/issues/34>`__).


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

- Fix unmatched built-in jQuery filename. (`#8 <https://github.com/helloflask/bootstrap-flask/issues/8>`__)


1.0.5
------

Release date: 2018/8/7

- Fix KeyError Exception if ENV isn't defined. (`#7 <https://github.com/helloflask/bootstrap-flask/pull/7>`__)


1.0.4
-----

Release date: 2018/7/24

-  Add missing ``<script>`` tag in resources URL. (`#3 <https://github.com/helloflask/bootstrap-flask/issues/3>`__)


1.0.3
-----

Release date: 2018/7/22

-  Built-in resources will be used when ``FLASK_ENV`` set to ``development``.
-  Change CDN provider to jsDelivr.


1.0.2
-----

Release date: 2018/7/21

-  Include ``popper.js`` before ``bootstrap.js`` in ``bootstrap.load_js()``. (`#2 <https://github.com/helloflask/bootstrap-flask/issues/2>`__)


1.0.1
-----

Release date: 2018/7/1

-  Fix local resources path error
-  Add basic unit tests


1.0
---

Release date: 2018/6/11

Initial release.
