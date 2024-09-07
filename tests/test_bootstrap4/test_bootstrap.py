import pytest
from flask import current_app, render_template_string
from flask_bootstrap import CDN_BASE, raise_helper


@pytest.mark.usefixtures('client')
class TestBootstrap:
    def test_raise_helper(self):
        with pytest.raises(RuntimeError, match='Test message'):
            raise_helper('Test message')

    def test_deprecate_bootstrap_class(self):
        from flask_bootstrap import Bootstrap
        from flask import Flask

        app = Flask(__name__)
        with pytest.warns(UserWarning):
            bootstrap = Bootstrap(app)  # noqa: F841

    def test_deprecate_bootstrap_template_path(self, app, client):
        @app.route('/test')
        def foo():
            return render_template_string('''
                    {% from 'bootstrap/utils.html' import render_icon %}
                    {{ render_icon('heart') }}
                    ''')

        with pytest.warns(UserWarning):
            client.get('/test')

    def test_extension_init(self):
        assert 'bootstrap' in current_app.extensions

    def test_load_css_with_default_versions(self, bootstrap):
        rv = bootstrap.load_css()
        bootstrap_css = f'<link rel="stylesheet" href="{CDN_BASE}/bootstrap@{bootstrap.bootstrap_version}/' \
                        f'dist/css/bootstrap.min.css" integrity="{bootstrap.bootstrap_css_integrity}" ' \
                        'crossorigin="anonymous">'
        assert bootstrap_css in rv

    def test_load_css_with_bootswatch_theme(self, bootstrap):
        rv = bootstrap.load_css(bootswatch_theme="mist")
        bootstrap_css = f'<link rel="stylesheet" href="{CDN_BASE}/bootswatch@{bootstrap.bootstrap_version}/' \
                        f'dist/mist/bootstrap.min.css"'
        assert bootstrap_css in rv

    def test_load_css_with_non_default_versions(self, bootstrap):
        def _check_assertions(rv):
            assert 'bootstrap.min.css' in rv
            assert 'integrity="' not in rv
            assert 'crossorigin="anonymous"' not in rv

        rv = bootstrap.load_css(version='4.5.6')
        _check_assertions(rv)
        rv = bootstrap.load_css(version='5.0.0')
        _check_assertions(rv)

    def test_load_js_with_default_versions(self, bootstrap):
        rv = bootstrap.load_js()
        bootstrap_js = f'<script src="{CDN_BASE}/bootstrap@{bootstrap.bootstrap_version}/dist/js/bootstrap.min.js"' \
                       f' integrity="{bootstrap.bootstrap_js_integrity}" crossorigin="anonymous"></script>'
        jquery_js = f'<script src="{CDN_BASE}/jquery@{bootstrap.jquery_version}/dist/jquery.min.js"' \
                    f' integrity="{bootstrap.jquery_integrity}" crossorigin="anonymous"></script>'
        popper_js = f'<script src="{CDN_BASE}/popper.js@{bootstrap.popper_version}/dist/umd/popper.min.js"' \
                    f' integrity="{bootstrap.popper_integrity}" crossorigin="anonymous"></script>'
        assert bootstrap_js in rv
        assert jquery_js in rv
        assert popper_js in rv

    def test_load_js_with_non_default_versions(self, bootstrap):
        def _check_assertions(rv):
            assert 'bootstrap.min.js' in rv
            assert 'jquery.min.js' in rv
            assert 'popper.min.js' in rv
            assert 'integrity="' not in rv
            assert 'crossorigin="anonymous"' not in rv

        rv = bootstrap.load_js(version='4.5.6', jquery_version='4.5.6',
                               popper_version='4.5.6')
        _check_assertions(rv)
        rv = bootstrap.load_js(version='4.0.0', jquery_version='4.0.0',
                               popper_version='4.0.0')
        _check_assertions(rv)

    def test_load_js_with_nonce(self, bootstrap):
        nonce = "rAnd0m"
        rv = bootstrap.load_js(nonce=nonce)
        bootstrap_js = f'<script src="{CDN_BASE}/bootstrap@{bootstrap.bootstrap_version}/dist/js/bootstrap.min.js"' \
                       f' integrity="{bootstrap.bootstrap_js_integrity}" crossorigin="anonymous"' \
                       f' nonce="{nonce}"></script>'
        jquery_js = f'<script src="{CDN_BASE}/jquery@{bootstrap.jquery_version}/dist/jquery.min.js"' \
                    f' integrity="{bootstrap.jquery_integrity}" crossorigin="anonymous"' \
                    f' nonce="{nonce}"></script>'
        popper_js = f'<script src="{CDN_BASE}/popper.js@{bootstrap.popper_version}/dist/umd/popper.min.js"' \
                    f' integrity="{bootstrap.popper_integrity}" crossorigin="anonymous"' \
                    f' nonce="{nonce}"></script>'
        assert bootstrap_js in rv
        assert jquery_js in rv
        assert popper_js in rv

    def test_local_resources(self, bootstrap, client):
        current_app.config['BOOTSTRAP_SERVE_LOCAL'] = True

        response = client.get('/')
        data = response.get_data(as_text=True)
        assert f'{CDN_BASE}/bootstrap' not in data
        assert 'bootstrap.min.js' in data
        assert 'bootstrap.min.css' in data
        assert 'jquery.min.js' in data
        assert 'integrity="' not in data
        assert 'crossorigin="anonymous"' not in data

        with client.get('/bootstrap/static/css/bootstrap.min.css') as css_response:
            assert css_response.status_code != 404
        with client.get('/bootstrap/static/js/bootstrap.min.js') as js_response:
            assert js_response.status_code != 404
        with client.get('/bootstrap/static/jquery.min.js') as jquery_response:
            assert jquery_response.status_code != 404

        css_rv = bootstrap.load_css()
        js_rv = bootstrap.load_js()
        assert '/bootstrap/static/css/bootstrap.min.css' in css_rv
        assert '/bootstrap/static/js/bootstrap.min.js' in js_rv
        assert f'{CDN_BASE}/bootstrap' not in css_rv
        assert f'{CDN_BASE}/bootstrap' not in js_rv
        assert 'integrity="' not in css_rv
        assert 'crossorigin="anonymous"' not in css_rv
        assert 'integrity="' not in js_rv
        assert 'crossorigin="anonymous"' not in js_rv

    def test_local_resources_with_sri(self, bootstrap):
        current_app.config['BOOTSTRAP_SERVE_LOCAL'] = True

        css_rv = bootstrap.load_css(bootstrap_sri='sha384-bootstrap-sri')
        js_rv = bootstrap.load_js(
            bootstrap_sri='sha384-bootstrap-sri',
            jquery_sri='sha384-jquery-sri',
            popper_sri='sha384-popper-sri'
        )
        assert '/bootstrap/static/css/bootstrap.min.css' in css_rv
        assert '/bootstrap/static/js/bootstrap.min.js' in js_rv
        assert f'{CDN_BASE}/bootstrap' not in css_rv
        assert f'{CDN_BASE}/bootstrap' not in js_rv
        assert 'integrity="sha384-bootstrap-sri"' in css_rv
        assert 'crossorigin="anonymous"' in css_rv
        assert 'integrity="sha384-bootstrap-sri"' in js_rv
        assert 'integrity="sha384-jquery-sri"' in js_rv
        assert 'integrity="sha384-popper-sri"' in js_rv
        assert 'crossorigin="anonymous"' in js_rv

    def test_cdn_resources(self, bootstrap, client):
        current_app.config['BOOTSTRAP_SERVE_LOCAL'] = False

        response = client.get('/')
        data = response.get_data(as_text=True)
        assert current_app.config['BOOTSTRAP_SERVE_LOCAL'] is not True
        assert f'{CDN_BASE}/bootstrap' in data
        assert 'bootstrap.min.js' in data
        assert 'bootstrap.min.css' in data

        css_rv = bootstrap.load_css()
        js_rv = bootstrap.load_js()
        assert '/bootstrap/static/css/bootstrap.min.css' not in css_rv
        assert '/bootstrap/static/js/bootstrap.min.js' not in js_rv
        assert f'{CDN_BASE}/bootstrap' in css_rv
        assert f'{CDN_BASE}/bootstrap' in js_rv

    def test_cdn_resources_with_custom_sri_hash(self, bootstrap):
        current_app.config['BOOTSTRAP_SERVE_LOCAL'] = False

        css_rv = bootstrap.load_css(bootstrap_sri='sha384-bootstrap-sri')
        js_rv = bootstrap.load_js(
            bootstrap_sri='sha384-bootstrap-sri',
            jquery_sri='sha384-jquery-sri',
            popper_sri='sha384-popper-sri'
        )
        assert 'integrity="sha384-bootstrap-sri"' in css_rv
        assert 'crossorigin="anonymous"' in css_rv
        assert 'integrity="sha384-bootstrap-sri"' in js_rv
        assert 'integrity="sha384-jquery-sri"' in js_rv
        assert 'integrity="sha384-popper-sri"' in js_rv
        assert 'crossorigin="anonymous"' in js_rv

    def test_disabling_sri(self, bootstrap):
        css_rv = bootstrap.load_css(bootstrap_sri=False)
        js_rv = bootstrap.load_js(
            bootstrap_sri=False,
            jquery_sri=False,
            popper_sri=False
        )
        assert 'href="' in css_rv
        assert 'integrity="' not in css_rv
        assert 'crossorigin="anonymous"' not in css_rv
        assert 'src="' in js_rv
        assert 'integrity="' not in js_rv
        assert 'crossorigin="anonymous"' not in js_rv

    @pytest.mark.parametrize(
        ['with_jquery', 'with_popper'],
        [
            (True, True),
            (False, False),
            (True, False),
            (False, True),
        ]
    )
    def test_load_js_args(self, with_jquery, with_popper, bootstrap):
        current_app.config['BOOTSTRAP_SERVE_LOCAL'] = True
        js_rv = bootstrap.load_js(with_jquery=with_jquery, with_popper=with_popper)

        assert ('jquery.min.js' in js_rv) == with_jquery
        assert ('popper.min.js' in js_rv) == with_popper
