from flask import Flask

from .blueprints.core import bp as bp_core


def create_app() -> Flask:
    """
    Create and set up an application Flask
    :return: The application Flask itself
    """

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'My_Hiper_Top_Secret_Key'

    # Set up of Blueprints

    bp_core.config(app, url_prefix='')

    return app
