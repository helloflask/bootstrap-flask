from flask import current_app


class TestBootstrap(object):
    def test_extension_init(self, client, bootstrap):
        assert 'bootstrap' in current_app.extensions

    def test_load_css(self, client, bootstrap):
        rv = bootstrap.load_css()
        assert 'bootstrap.min.css' in rv

    def test_load_js(self, client, bootstrap):
        rv = bootstrap.load_js()
        assert 'bootstrap.min.js' in rv

    def test_local_resources(self, client, bootstrap):
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

    def test_cdn_resources(self, client, bootstrap):
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

    def test_bootswatch_local(self, client, bootswatch_themes):
        current_app.config['BOOTSTRAP_SERVE_LOCAL'] = True

        for theme in bootswatch_themes:
            current_app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = theme
            data = client.get('/').get_data(as_text=True)
            assert 'https://cdn.jsdelivr.net/npm/bootswatch' not in data
            assert 'swatch/%s/bootstrap.min.css' % theme in data
            with client.get('/bootstrap/static/css/swatch/%s/bootstrap.min.css' % theme) as css_response:
                assert css_response.status_code != 404

    def test_bootswatch_cdn(self, client, bootstrap, bootswatch_themes):
        current_app.config['BOOTSTRAP_SERVE_LOCAL'] = False

        for theme in bootswatch_themes:
            current_app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = theme
            data = client.get('/').get_data(as_text=True)
            assert 'https://cdn.jsdelivr.net/npm/bootswatch' in data
            assert 'dist/%s/bootstrap.min.css' % theme in data
            css_rv = bootstrap.load_css()
            assert '/bootstrap/static/css/swatch/%s/bootstrap.min.css' % theme not in data
            assert 'https://cdn.jsdelivr.net/npm/bootswatch' in css_rv
