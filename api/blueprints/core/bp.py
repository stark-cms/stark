from flask import Blueprint


bp = Blueprint('core', __name__)


def config(app):
    from api.blueprints.core import routes # noqa
    app.register_blueprint(bp)
