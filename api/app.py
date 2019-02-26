from flask import Flask

import api.settings as default_settings


def create_app(settings=None) -> Flask:
    """
    Create and set up an application Flask
    :return: The application Flask itself
    """

    if settings is None:
        settings = default_settings

    app = Flask(__name__, template_folder='templates')
    app.config.from_object(settings)
    app.debug = app.config['DEBUG']

    # Set up of Blueprints

    from api.blueprints.core import bp as bp_core
    bp_core.config(app, url_prefix='')

    return app
