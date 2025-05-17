import pytest
from bs4 import BeautifulSoup
from flask import Flask, render_template_string


@pytest.fixture
def app():
    app = Flask(__name__)
    app.secret_key = "test"
    return app


def test_cdn_integrity(app):
    @app.route("/")
    def index():
        return render_template_string(
            "{{ bootstrap.load_css() }}{{ bootstrap.load_js() }}"
        )

    client = app.test_client()
    response = client.get("/")
    html = response.get_data(as_text=True)
    soup = BeautifulSoup(html, "html.parser")

    css = soup.find("link", rel="stylesheet")
    js = soup.find("script", src=lambda s: s and "bootstrap" in s)

    bootstrap = app.extensions["bootstrap"]
    assert css["integrity"] == bootstrap.bootstrap_css_integrity
    assert js["integrity"] == bootstrap.bootstrap_js_integrity
    assert css["crossorigin"] == "anonymous"
    assert js["crossorigin"] == "anonymous"
