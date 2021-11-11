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

CDN_BASE = 'https://cdn.jsdelivr.net/npm'


def raise_helper(message):  # pragma: no cover
    raise RuntimeError(message)


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


class _Bootstrap:
    """
    Base extension class for different Bootstrap versions.

    .. versionadded:: 2.0.0
    """

    bootstrap_version = None
    jquery_version = None
    popper_version = None
    bootstrap_css_integrity = None
    bootstrap_js_integrity = None
    jquery_integrity = None
    popper_integrity = None
    static_folder = None
    bootstrap_css_filename = 'bootstrap.min.css'
    bootstrap_js_filename = 'bootstrap.min.js'
    jquery_filename = 'jquery.min.js'
    popper_filename = 'popper.min.js'

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['bootstrap'] = self

        blueprint = Blueprint('bootstrap', __name__, static_folder=f'static/{self.static_folder}',
                              static_url_path=f'/bootstrap{app.static_url_path}',
                              template_folder='templates')
        app.register_blueprint(blueprint)

        app.jinja_env.globals['bootstrap'] = self
        app.jinja_env.globals['bootstrap_is_hidden_field'] = is_hidden_field_filter
        app.jinja_env.globals['get_table_titles'] = get_table_titles
        app.jinja_env.globals['warn'] = warnings.warn
        app.jinja_env.globals['raise'] = raise_helper
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

    def load_css(self, version=None, bootstrap_sri=None):
        """Load Bootstrap's css resources with given version.

        .. versionadded:: 0.1.0

        :param version: The version of Bootstrap.
        """
        serve_local = current_app.config['BOOTSTRAP_SERVE_LOCAL']
        bootswatch_theme = current_app.config['BOOTSTRAP_BOOTSWATCH_THEME']
        if version is None:
            version = self.bootstrap_version
        bootstrap_sri = self._get_sri('bootstrap_css', version, bootstrap_sri)

        if serve_local:
            if not bootswatch_theme:
                base_path = 'css'
            else:
                base_path = f'css/bootswatch/{bootswatch_theme.lower()}'
            boostrap_url = url_for('bootstrap.static', filename=f'{base_path}/{self.bootstrap_css_filename}')
        else:
            if not bootswatch_theme:
                base_path = f'{CDN_BASE}/bootstrap@{version}/dist/css'
            else:
                base_path = f'{CDN_BASE}/bootswatch@{version}/dist/{bootswatch_theme.lower()}'
            boostrap_url = f'{base_path}/{self.bootstrap_css_filename}'

        if bootstrap_sri and not bootswatch_theme:
            css = f'<link rel="stylesheet" href="{boostrap_url}" integrity="{bootstrap_sri}" crossorigin="anonymous">'
        else:
            css = f'<link rel="stylesheet" href="{boostrap_url}">'
        return Markup(css)

    def _get_js_script(self, version, name, sri):
        """Get <script> tag for JavaScipt resources."""
        serve_local = current_app.config['BOOTSTRAP_SERVE_LOCAL']
        paths = {
            'bootstrap': f'js/{self.bootstrap_js_filename}',
            'jquery': f'{self.jquery_filename}',
            '@popperjs/core': f'umd/{self.popper_filename}',
            'popper.js': f'umd/{self.popper_filename}',
        }
        if serve_local:
            url = url_for('bootstrap.static', filename=paths[name])
        else:
            url = f'{CDN_BASE}/{name}@{version}/dist/{paths[name]}'
        if sri:
            return f'<script src="{url}" integrity="{sri}" crossorigin="anonymous"></script>'
        return f'<script src="{url}"></script>'

    def _get_sri(self, name, version, sri):
        serve_local = current_app.config['BOOTSTRAP_SERVE_LOCAL']
        sris = {
            'bootstrap_css': self.bootstrap_css_integrity,
            'bootstrap_js': self.bootstrap_js_integrity,
            'jquery': self.jquery_integrity,
            'popper': self.popper_integrity,
        }
        versions = {
            'bootstrap_css': self.bootstrap_version,
            'bootstrap_js': self.bootstrap_version,
            'jquery': self.jquery_version,
            'popper': self.popper_version
        }
        if sri is not None:
            return sri
        if version == versions[name] and serve_local is False:
            return sris[name]
        return None

    def load_js(self, version=None, jquery_version=None,  # noqa: C901
                popper_version=None, with_jquery=True, with_popper=True,
                bootstrap_sri=None, jquery_sri=None, popper_sri=None):
        """Load Bootstrap and related library's js resources with given version.

        .. versionadded:: 0.1.0

        :param version: The version of Bootstrap.
        :param jquery_version: The version of jQuery (only needed with Bootstrap 4).
        :param popper_version: The version of Popper.js.
        :param with_jquery: Include jQuery or not (only needed with Bootstrap 4).
        :param with_popper: Include Popper.js or not.
        """
        if version is None:
            version = self.bootstrap_version
        if popper_version is None:
            popper_version = self.popper_version

        bootstrap_sri = self._get_sri('bootstrap_js', version, bootstrap_sri)
        popper_sri = self._get_sri('popper', popper_version, popper_sri)
        bootstrap = self._get_js_script(version, 'bootstrap', bootstrap_sri)
        popper = self._get_js_script(popper_version, self.popper_name, popper_sri) if with_popper else ''
        if version.startswith('4'):
            if jquery_version is None:
                jquery_version = self.jquery_version
            jquery_sri = self._get_sri('jquery', jquery_version, jquery_sri)
            jquery = self._get_js_script(jquery_version, 'jquery', jquery_sri) if with_jquery else ''
            return Markup(f'''{jquery}
        {popper}
        {bootstrap}''')
        return Markup(f'''{popper}
        {bootstrap}''')


class Bootstrap4(_Bootstrap):
    """
    Extension class for Bootstrap 4.

    Initilize the extension::

        from flask import Flask
        from flask_bootstrap import Bootstrap

        app = Flask(__name__)
        bootstrap = Bootstrap(app)

    Or with the application factory::

        from flask import Flask
        from flask_bootstrap import Bootstrap

        bootstrap = Bootstrap()

        def create_app():
            app = Flask(__name__)
            bootstrap.init_app(app)

    .. versionchanged:: 2.0.0
       Move common logic to base class ``_Bootstrap``.
    """
    bootstrap_version = '4.3.1'
    jquery_version = '3.4.1'
    popper_version = '1.14.0'
    bootstrap_css_integrity = 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T'
    bootstrap_js_integrity = 'sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM'
    jquery_integrity = 'sha384-vk5WoKIaW/vJyUAd9n/wmopsmNhiy+L2Z+SBxGYnUkunIxVxAv/UtMOhba/xskxh'
    popper_integrity = 'sha384-cs/chFZiN24E4KMATLdqdvsezGxaGsi4hLGOzlXwp5UZB1LY//20VyM2taTB4QvJ'
    popper_name = 'popper.js'
    static_folder = 'bootstrap4'


class Bootstrap5(_Bootstrap):
    """
    Base class for Bootstrap 5.

    Initilize the extension::

        from flask import Flask
        from flask_bootstrap import Bootstrap5

        app = Flask(__name__)
        bootstrap = Bootstrap5(app)

    Or with the application factory::

        from flask import Flask
        from flask_bootstrap import Bootstrap5

        bootstrap = Bootstrap5()

        def create_app():
            app = Flask(__name__)
            bootstrap5.init_app(app)

    .. versionadded:: 2.0.0
    """
    bootstrap_version = '5.1.1'
    popper_version = '2.10.1'
    bootstrap_css_integrity = 'sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU'
    bootstrap_js_integrity = 'sha384-skAcpIdS7UcVUC05LJ9Dxay8AXcDYfBJqt1CJ85S/CFujBsIzCIv+l9liuYLaMQ/'
    popper_integrity = 'sha384-W8fXfP3gkOKtndU4JGtKDvXbO53Wy8SZCQHczT5FMiiqmQfUpWbYdTil/SxwZgAN'
    popper_name = '@popperjs/core'
    static_folder = 'bootstrap5'


class Bootstrap(Bootstrap4):
    def __init__(self, app):
        super().__init__(app=app)
        warnings.warn(
            'For Bootstrap 4, please import and use "Bootstrap4" class, the "Bootstrap" class '
            'is deprecated and will be removed in 3.0.',
            stacklevel=2
        )
