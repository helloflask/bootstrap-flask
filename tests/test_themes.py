from flask import current_app
import pytest


themes = [
    'cerulean',
    'cosmo',
    'cyborg',
    'darkly',
    'flatly',
    'journal',
    'litera',
    'lumen',
    'lux',
    'materia',
    'minty',
    'pulse',
    'sandstone',
    'simplex',
    'sketchy',
    'slate',
    'solar',
    'spacelab',
    'superhero',
    'united',
    'yeti'
]


class TestThemes:
    @pytest.mark.parametrize('theme', themes)
    def test_bootswatch_local(self, theme, client):
        current_app.config['BOOTSTRAP_SERVE_LOCAL'] = True
        current_app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = theme
        data = client.get('/').get_data(as_text=True)
        assert 'https://cdn.jsdelivr.net/npm/bootswatch' not in data
        assert 'swatch/%s/bootstrap.min.css' % theme in data
        with client.get('/bootstrap/static/css/swatch/%s/bootstrap.min.css' % theme) as css_response:
            assert css_response.status_code != 404

    @pytest.mark.parametrize('theme', themes)
    def test_bootswatch_cdn(self, theme, client, bootstrap):
        current_app.config['BOOTSTRAP_SERVE_LOCAL'] = False
        current_app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = theme
        data = client.get('/').get_data(as_text=True)
        assert 'https://cdn.jsdelivr.net/npm/bootswatch' in data
        assert 'dist/%s/bootstrap.min.css' % theme in data
        css_rv = bootstrap.load_css()
        assert '/bootstrap/static/css/swatch/%s/bootstrap.min.css' % theme not in data
        assert 'https://cdn.jsdelivr.net/npm/bootswatch' in css_rv
