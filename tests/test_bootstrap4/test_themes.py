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


@pytest.mark.parametrize('theme', themes)
def test_bootswatch_local(theme, client):
    current_app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    current_app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = theme
    data = client.get('/').get_data(as_text=True)
    assert 'https://cdn.jsdelivr.net/npm/bootswatch' not in data
    assert f'bootswatch/{theme}/bootstrap.min.css' in data
    with client.get(f'/bootstrap/static/css/bootswatch/{theme}/bootstrap.min.css') as css_response:
        assert css_response.status_code != 404


@pytest.mark.parametrize('theme', themes)
def test_bootswatch_cdn(bootstrap, theme, client):
    current_app.config['BOOTSTRAP_SERVE_LOCAL'] = False
    current_app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = theme
    data = client.get('/').get_data(as_text=True)
    assert 'https://cdn.jsdelivr.net/npm/bootswatch' in data
    assert f'dist/{theme}/bootstrap.min.css' in data
    css_rv = bootstrap.load_css()
    assert f'/bootstrap/static/css/bootswatch/{theme}/bootstrap.min.css' not in data
    assert 'https://cdn.jsdelivr.net/npm/bootswatch' in css_rv
