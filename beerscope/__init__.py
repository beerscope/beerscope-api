import os

import flask


def create_app(config_filename):
    app = flask.Flask(
        __name__,
        root_path=os.path.sep.join([os.path.dirname(__file__), '..']),
    )
    app.config.from_pyfile(config_filename)

    from . import models
    models.db.init_app(app)

    from . import organizer_views
    organizer_views.manager.init_app(app, flask_sqlalchemy_db=models.db)

    return app
