import flask_restless

from . import models

manager = flask_restless.APIManager()
keg_blueprint = manager.create_api(models.Keg, methods=['GET', 'POST', 'DELETE'], primary_key='id')
