from flask import Blueprint, Flask

bp = Blueprint('core', __name__, template_folder='templates')


def config(app: Flask, url_prefix: str = '') -> None:
    from blueprints.core import routes  # noqa
    app.register_blueprint(bp, url_prefix=url_prefix)
