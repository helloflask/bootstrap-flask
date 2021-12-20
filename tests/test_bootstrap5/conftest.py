import pytest
from flask_bootstrap import Bootstrap5


@pytest.fixture(autouse=True)
def bootstrap(app):
    yield Bootstrap5(app)
