# Upgrade

This document describes how to upgrade Bootstrap-Flask.

# Dependencies

Version upgrades offered as PRs by dependabot, as seen in https://github.com/helloflask/bootstrap-flask/issues?q=is%3Apr+author%3Aapp%2Fdependabot are best closed without merge. In a manual PR, all these version upgrades can be gathered and tested. Sometimes it gives conflicts reported by pip that need investigation that doesn't work well by simply merging all dependabot's PRs.

Note that new version of Python and versions that reached end of life need to handled at the same time, as they might be interdepending.

Files that need to be reviewed are:
- `requirements/*.txt` (all dependencies, if needed, also check `*.in` files)
- `pyproject.toml` (all supported Python versions)
- `tox.ini` (all supported Python versions)
- `workflows/build.yml` (all supported Python versions)
- `workflows/release.yml` (only latest stable Python version)
- `workflows/master_bootstrap-flask-example.yml` (only latest stable Python version)

See also https://devguide.python.org/versions/

# Bootstrap

Note that usually it is good to wait that Bootswatch also supports the new version.

Download the latest `bootstrap-5.y.z-dist.zip` from https://github.com/twbs/bootstrap/releases/latest/ and unzip it.

Create a branch called `bootstrap_5.y.z` and override the following files:
- `flask_bootstrap/static/bootstrap5/js/bootstrap.min.js`
- `flask_bootstrap/static/bootstrap5/js/bootstrap.min.js.map`
- `flask_bootstrap/static/bootstrap5/css/bootstrap.min.css`
- `flask_bootstrap/static/bootstrap5/css/bootstrap.min.css.map`

In `flask_bootstrap/__init__.py` for class `Bootstrap5` change the value of `bootstrap_version` to `5.y.z`. Look up all the values for attribute `integrity` at https://getbootstrap.com/docs/5.3/getting-started/download/#cdn-via-jsdelivr (note the `3` in the link, change if needed) and upgrade:
- `bootstrap_css_integrity` (see link `bootstrap.min.css`)
- `bootstrap_js_integrity` (see script `bootstrap.min.js`, not `bootstrap.bundle.min.js`)
- `popper_integrity` (this probably has not changed)

Test all by running in the main directory `pytest`.

Test the examples after `pip install .` with `python3 examples/bootstrap4/app.py` and `python3 examples/bootstrap5/app.py` by viewing all the example pages in a browser.

Update the file `CHANGES.rst` and create a pull request.

Note that Bootstrap version 4 is no longer updated.

# Bootstrap Icons

Download the latest `bootstrap-icons-x.y.z.zip` from https://github.com/twbs/icons/releases/latest/ and unzip it.

Create a branch called `icons_x.y.z` and override the following files:
- `flask_bootstrap/static/bootstrap4/icons/bootstrap-icons.svg`
- `flask_bootstrap/static/bootstrap5/icons/bootstrap-icons.svg`
- `flask_bootstrap/static/bootstrap4/css/font/bootstrap-icons.min.css`
- `flask_bootstrap/static/bootstrap5/css/font/bootstrap-icons.min.css`
- `flask_bootstrap/static/bootstrap4/css/font/fonts/bootstrap-icons.woff`
- `flask_bootstrap/static/bootstrap4/css/font/fonts/bootstrap-icons.woff2`
- `flask_bootstrap/static/bootstrap5/css/font/fonts/bootstrap-icons.woff`
- `flask_bootstrap/static/bootstrap5/css/font/fonts/bootstrap-icons.woff2`

In `flask_bootstrap/__init__.py` for class `Bootstrap4` and `Bootstrap5` change the value of `icons_version` to `x.y.z`.

Go to the directory `examples` and run `python3 update_icons.py` to update the overview of icons in the examples.

Test all by running in the main directory `pytest`.

Test the examples after `pip install .` with `python3 examples/bootstrap4/app.py` and `python3 examples/bootstrap5/app.py` by viewing all the example pages in a browser.

Update the file `CHANGES.rst` and create a pull request.

TODO Add https://pypi.org/project/lxml/ to dev? requirements?

# Bootswatch

Download the latest `vx.y.z.zip` from https://github.com/thomaspark/bootswatch/tags and unzip it.

Create a branch called `bootswatch_5.y.z` and in the downloaded tree, go to the directory `dist` and do

```sh
find . -name 'bootstrap.rtl.*' -exec rm {} \;
find . -name 'bootstrap.*.map' -exec rm {} \;
```

Then copy the contents for `dist` to override `flask_bootstrap/static/bootstrap5/css/bootswatch`.

Go to the directory `examples` and run `python3 list-bootswatch.py` to update the overview of icons in the examples.

Test all by running in the main directory `pytest`. See also https://github.com/helloflask/bootstrap-flask/discussions/276 for code coverage.

Test the examples after `pip install .` with `python3 examples/bootstrap4/app.py` and `python3 examples/bootstrap5/app.py` by viewing all the example pages in a browser.

Update the file `CHANGES.rst` and create a pull request.

TODO Popper needs to replaced with a new library. See https://github.com/helloflask/bootstrap-flask/issues/256 .

Note that Bootswatch version 4 is no longer updated.

