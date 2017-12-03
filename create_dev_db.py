#!/usr/bin/env python

from beerscope import create_app, models


if __name__ == '__main__':
    app = create_app('config/dev.cfg')

    with app.app_context():
        models.db.create_all(app=app)
