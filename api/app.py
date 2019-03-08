from flask import Flask
from api.settings import STARK_SECRET_KEY

def create_app():
    """
    Create and set up an application Flask
    :return: The application Flask itself
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = STARK_SECRET_KEY

    # Blueprint

    from api.blueprints.core import bp as bp_core
    bp_core.config(app)

    return app
