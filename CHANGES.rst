Changelog
==========

1.1.0
------

Release date: 2019/9/9

- Update Bootstrap version to 4.3.1


1.0.10
------

Release date: 2019/3/7

- Added macro ``render_form_row`` for rendering a row of a bootstrap grid form.


1.0.9
------

Release date: 2018/11/14

- Fix missing error message when form type was horizontal.
- Fix missing input label for RadioField.
- Fix RadioField grid when form type was horizontal.


1.0.8
------

Release date: 2018/9/6

- Correct macro name used in ``templates/boostrap/form.html``: ``form_field`` --> ``render_field``.


1.0.7
------

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
------

Release date: 2018/7/24

-  Add missing ``<script>`` tag in resources URL. (`#3 <https://github.com/greyli/bootstrap-flask/issues/3>`__)

1.0.3
------

Release date: 2018/7/22

-  Built-in resources will be used when ``FLASK_ENV`` set to ``development``.
-  Change CDN provider to jsDelivr.

1.0.2
------

Release date: 2018/7/21

-  Include ``popper.js`` before ``bootstrap.js`` in ``bootstrap.load_js()``. (`#2 <https://github.com/greyli/bootstrap-flask/issues/2>`__)

1.0.1
------

Release date: 2018/7/1

-  Fix local resources path error
-  Add basic unit tests

1.0
-----

Release date: 2018/6/11

Initialize release.
