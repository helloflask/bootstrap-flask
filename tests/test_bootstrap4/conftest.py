import pytest
from flask_bootstrap import Bootstrap4


@pytest.fixture(autouse=True)
def bootstrap(app):
    yield Bootstrap4(app)
