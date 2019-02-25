from blueprints.core.bp import bp


@bp.route('/')
def home():
    return "<h1>Hello World</h1>"
