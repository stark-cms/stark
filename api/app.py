from flask import Flask


def create_app() -> Flask:
    """
    Create and set up an application Flask
    :return: The application Flask itself
    """
    app = Flask(__name__, template_folder='templates')

    # Set up of Blueprints

    from api.blueprints.core import bp as bp_core
    bp_core.config(app, url_prefix='')

    return app
