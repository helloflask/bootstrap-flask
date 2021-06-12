# -*- coding: utf-8 -*-
"""
    flask_bootstrap
    ~~~~~~~~~~~~~~
    :copyright: (c) 2017 by Grey Li.
    :license: MIT, see LICENSE for more details.
"""
import warnings

from flask import current_app, Markup, Blueprint, url_for

try:  # pragma: no cover
    from wtforms.fields import HiddenField
except ImportError:
    def is_hidden_field_filter(field):
        raise RuntimeError('WTForms is not installed.')
else:
    def is_hidden_field_filter(field):
        return isinstance(field, HiddenField)

# central definition of used versions
VERSION_BOOTSTRAP = '4.3.1'
VERSION_JQUERY = '3.4.1'
VERSION_POPPER = '1.14.0'


def get_table_titles(data, primary_key, primary_key_title):
    """Detect and build the table titles tuple from ORM object, currently only support SQLAlchemy.

    .. versionadded:: 1.4.0
    """
    if not data:
        return []
    titles = []
    for k in data[0].__table__.columns.keys():
        if not k.startswith('_'):
            titles.append((k, k.replace('_', ' ').title()))
    titles[0] = (primary_key, primary_key_title)
    return titles


class Bootstrap(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['bootstrap'] = self

        blueprint = Blueprint('bootstrap', __name__, template_folder='templates',
                              static_folder='static', static_url_path='/bootstrap' + app.static_url_path)
        app.register_blueprint(blueprint)

        app.jinja_env.globals['bootstrap'] = self
        app.jinja_env.globals['bootstrap_is_hidden_field'] = is_hidden_field_filter
        app.jinja_env.globals['get_table_titles'] = get_table_titles
        app.jinja_env.globals['warn'] = warnings.warn
        app.jinja_env.add_extension('jinja2.ext.do')
        # default settings
        app.config.setdefault('BOOTSTRAP_SERVE_LOCAL', False)
        app.config.setdefault('BOOTSTRAP_BTN_STYLE', 'primary')
        app.config.setdefault('BOOTSTRAP_BTN_SIZE', 'md')
        app.config.setdefault('BOOTSTRAP_BOOTSWATCH_THEME', None)
        app.config.setdefault('BOOTSTRAP_ICON_SIZE', '1em')
        app.config.setdefault('BOOTSTRAP_ICON_COLOR', None)
        app.config.setdefault('BOOTSTRAP_MSG_CATEGORY', 'primary')
        app.config.setdefault('BOOTSTRAP_TABLE_VIEW_TITLE', 'View')
        app.config.setdefault('BOOTSTRAP_TABLE_EDIT_TITLE', 'Edit')
        app.config.setdefault('BOOTSTRAP_TABLE_DELETE_TITLE', 'Delete')
        app.config.setdefault('BOOTSTRAP_TABLE_NEW_TITLE', 'New')

    @staticmethod
    def load_css(version=VERSION_BOOTSTRAP):
        """Load Bootstrap's css resources with given version.

        .. versionadded:: 0.1.0

        :param version: The version of Bootstrap.
        """
        css_filename = 'bootstrap.min.css'
        serve_local = current_app.config['BOOTSTRAP_SERVE_LOCAL']
        bootswatch_theme = current_app.config['BOOTSTRAP_BOOTSWATCH_THEME']

        if not bootswatch_theme:
            base_path = 'css/'
        else:
            base_path = 'css/swatch/%s/' % bootswatch_theme.lower()

        if serve_local:
            css = '<link rel="stylesheet" href="%s" type="text/css">' % \
                url_for('bootstrap.static', filename=base_path + css_filename)
        else:
            if not bootswatch_theme:
                css = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@%s/dist/css/%s"' \
                    ' type="text/css">' % (version, css_filename)
            else:
                css = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@%s/dist/%s/%s"' \
                    ' type="text/css">' % (version, bootswatch_theme.lower(), css_filename)
        return Markup(css)

    @staticmethod
    def load_js(version=VERSION_BOOTSTRAP, jquery_version=VERSION_JQUERY,
                popper_version=VERSION_POPPER, with_jquery=True, with_popper=True):
        """Load Bootstrap and related library's js resources with given version.

        .. versionadded:: 0.1.0

        :param version: The version of Bootstrap.
        :param jquery_version: The version of jQuery.
        :param popper_version: The version of Popper.js.
        :param with_jquery: Include jQuery or not.
        :param with_popper: Include Popper.js or not.
        """
        js_filename = 'bootstrap.min.js'
        jquery_filename = 'jquery.min.js'
        popper_filename = 'popper.min.js'

        serve_local = current_app.config['BOOTSTRAP_SERVE_LOCAL']

        if serve_local:
            js = '<script src="%s"></script>' % url_for('bootstrap.static', filename='js/' + js_filename)
        else:
            js = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@%s/dist/js/%s">' \
                 '</script>' % (version, js_filename)

        if with_jquery:
            if serve_local:
                jquery = '<script src="%s"></script>' % url_for('bootstrap.static', filename=jquery_filename)
            else:
                jquery = '<script src="https://cdn.jsdelivr.net/npm/jquery@%s/dist/%s">' \
                 '</script>' % (jquery_version, jquery_filename)
        else:
            jquery = ''

        if with_popper:
            if serve_local:
                popper = '<script src="%s"></script>' % url_for('bootstrap.static', filename=popper_filename)
            else:
                popper = '<script src="https://cdn.jsdelivr.net/npm/popper.js@%s/dist/umd/%s">' \
                     '</script>' % (popper_version, popper_filename)
        else:
            popper = ''
        return Markup('''%s
    %s
    %s''' % (jquery, popper, js))
