import pytest
from flask_bootstrap import Bootstrap


@pytest.fixture(autouse=True)
def bootstrap(app):
    yield Bootstrap(app)
