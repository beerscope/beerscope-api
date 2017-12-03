import pytest

from beerscope import create_app, models


@pytest.fixture(scope='session')
def app():
    app = create_app('config/test.cfg')
    models.db.create_all(app=app)

    with app.app_context():
        yield app
