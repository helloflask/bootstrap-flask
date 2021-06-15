import pytest
from flask import current_app
from flask_bootstrap import (
    VERSION_BOOTSTRAP, VERSION_JQUERY, VERSION_POPPER, 
    BOOTSTRAP_CSS_INTEGRITY, BOOTSTRAP_JS_INTEGRITY, 
    JQUERY_INTEGRITY, POPPER_INTEGRITY
)

@pytest.mark.usefixtures('client')
class TestBootstrap:
    def test_extension_init(self, bootstrap):
        assert 'bootstrap' in current_app.extensions

    def test_load_css_with_default_versions(self, bootstrap):
        rv = bootstrap.load_css()
        bootstrap_css = ('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@%s/dist/css/%s"'
            ' integrity="%s" crossorigin="anonymous">' % (VERSION_BOOTSTRAP, 'bootstrap.min.css', 
            BOOTSTRAP_CSS_INTEGRITY))
        assert bootstrap_css in rv

    def test_load_css_with_non_default_versions(self, bootstrap):
        def _check_assertions(rv):
            assert 'bootstrap.min.css' in rv
            assert 'integrity="' not in rv
            assert 'crossorigin="anonymous"' not in rv

        rv = bootstrap.load_css(version='1.2.3')
        _check_assertions(rv)
        rv = bootstrap.load_css(version='5.0.0')
        _check_assertions(rv)

    def test_load_js_with_default_versions(self, bootstrap):
        rv = bootstrap.load_js()
        bootstrap_js = ('<script src="https://cdn.jsdelivr.net/npm/bootstrap@%s/dist/js/%s"'
                        ' integrity="%s" crossorigin="anonymous"></script>' % 
                        (VERSION_BOOTSTRAP, 'bootstrap.min.js', BOOTSTRAP_JS_INTEGRITY))
        jquery_js = ('<script src="https://cdn.jsdelivr.net/npm/jquery@%s/dist/%s"'
                        ' integrity="%s" crossorigin="anonymous"></script>' % 
                        (VERSION_JQUERY, 'jquery.min.js', JQUERY_INTEGRITY))
        popper_js = ('<script src="https://cdn.jsdelivr.net/npm/popper.js@%s/dist/umd/%s"'
                        ' integrity="%s" crossorigin="anonymous"></script>' % 
                        (VERSION_POPPER, 'popper.min.js', POPPER_INTEGRITY))
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

        rv = bootstrap.load_js(version='1.2.3', jquery_version='1.2.3', 
            popper_version='1.2.3')
        _check_assertions(rv)
        rv = bootstrap.load_js(version='5.0.0', jquery_version='5.0.0', 
            popper_version='5.0.0')
        _check_assertions(rv)

    def test_local_resources(self, bootstrap, client):
        current_app.config['BOOTSTRAP_SERVE_LOCAL'] = True

        response = client.get('/')
        data = response.get_data(as_text=True)
        assert 'https://cdn.jsdelivr.net/npm/bootstrap' not in data
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
        assert 'https://cdn.jsdelivr.net/npm/bootstrap' not in css_rv
        assert 'https://cdn.jsdelivr.net/npm/bootstrap' not in js_rv
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
        assert 'https://cdn.jsdelivr.net/npm/bootstrap' not in css_rv
        assert 'https://cdn.jsdelivr.net/npm/bootstrap' not in js_rv
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
        assert 'https://cdn.jsdelivr.net/npm/bootstrap' in data
        assert 'bootstrap.min.js' in data
        assert 'bootstrap.min.css' in data

        css_rv = bootstrap.load_css()
        js_rv = bootstrap.load_js()
        assert '/bootstrap/static/css/bootstrap.min.css' not in css_rv
        assert '/bootstrap/static/js/bootstrap.min.js' not in js_rv
        assert 'https://cdn.jsdelivr.net/npm/bootstrap' in css_rv
        assert 'https://cdn.jsdelivr.net/npm/bootstrap' in js_rv

    def test_cdn_resources_with_custom_sri_hash(self, bootstrap, client):
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
    def test_load_js_args(self, with_jquery, with_popper, bootstrap, client):
        current_app.config['BOOTSTRAP_SERVE_LOCAL'] = True
        js_rv = bootstrap.load_js(with_jquery=with_jquery, with_popper=with_popper)

        assert ('jquery.min.js' in js_rv) == with_jquery
        assert ('popper.min.js' in js_rv) == with_popper
