# -*- coding: utf-8 -*-
"""
    Boostrap-Flask
    ~~~~~~~~~~~~~~
    :copyright: (c) 2017 by Grey Li.
    :license: MIT, see LICENSE for more details.
"""
from flask import current_app, Markup, Blueprint, url_for

try:
    from wtforms.fields import HiddenField
except ImportError:

    def is_hidden_field_filter(field):
        raise RuntimeError('WTForms is not installed.')
else:

    def is_hidden_field_filter(field):
        return isinstance(field, HiddenField)


class Bootstrap(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['bootstrap'] = self

        blueprint = Blueprint('bootstrap', __name__, template_folder='templates',
                              static_folder='static', static_url_path='/bootstrap/static')
        app.register_blueprint(blueprint)

        app.jinja_env.globals['bootstrap'] = self
        app.jinja_env.globals['bootstrap_is_hidden_field'] = \
            is_hidden_field_filter
        app.jinja_env.add_extension('jinja2.ext.do')
        # default settings
        app.config.setdefault('SHARE_SERVE_LOCAL', False)

    @staticmethod
    def load_css():
        pass

    @staticmethod
    def load_js(with_jquery=True, with_popper=True):
        pass
