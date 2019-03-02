from flask import Flask


def create_app():
    """
    Create and set up an application Flask
    :return: The application Flask itself
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'My_Top_Secert_Key'

    # Blueprint

    from api.blueprints.core import bp as bp_core
    bp_core.config(app)

    return app
