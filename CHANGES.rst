Changelog
=========

1.5
---

Release data: --

- Fix ``tox`` broken environments.
- Fix ``ResourceWarning`` in ``test_local_resources`` (`#78 <https://github.com/greyli/bootstrap-flask/pull/78>`__).
- Fix ``IndexError`` when using ``render_table`` with empty data (`#75 <https://github.com/greyli/bootstrap-flask/issues/75>`__).
- Add support for actions column in ``render_table`` macro (`#76 <https://github.com/greyli/bootstrap-flask/issues/76>`__).
- Add support for Bootswatch theme via configuration ``BOOTSTRAP_BOOTSWATCH_THEME`` (`#88 <https://github.com/greyli/bootstrap-flask/pull/88>`__).
- Fix checkbox render issue: add ``for`` attribute to link ``<label>`` with checkbox, only add ``is-invalid`` class when there are errors.
- Change default button style class from ``btn-secondary`` to ``btn-primary`` (`#62 <https://github.com/greyli/bootstrap-flask/issues/62>`__).
- Deprecated ``form_errors`` macro and it will be removed in 2.0, add ``render_hidden_errors`` macro as replacement.


1.4
---

Release data: 6/15

- Add ``render_table`` macro to render a Bootstrap table (`#71 <https://github.com/greyli/bootstrap-flask/pull/71>`__).


1.3.2
-----

Release data: 2020/5/30

- Support display error message for ``RadioField`` and ``BooleanField``, display description for ``RadioField``.


1.3.1
-----

Release data: 2020/4/29

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
