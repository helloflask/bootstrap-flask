import pytest
from flask import current_app


@pytest.mark.usefixtures('client')
class TestBootstrap:
    def test_extension_init(self, bootstrap):
        assert 'bootstrap' in current_app.extensions

    def test_load_css(self, bootstrap):
        rv = bootstrap.load_css()
        assert 'bootstrap.min.css' in rv

    def test_load_js(self, bootstrap):
        rv = bootstrap.load_js()
        assert 'bootstrap.min.js' in rv

    def test_local_resources(self, bootstrap, client):
        current_app.config['BOOTSTRAP_SERVE_LOCAL'] = True

        response = client.get('/')
        data = response.get_data(as_text=True)
        assert 'https://cdn.jsdelivr.net/npm/bootstrap' not in data
        assert 'bootstrap.min.js' in data
        assert 'bootstrap.min.css' in data
        assert 'jquery.min.js' in data

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
