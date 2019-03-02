from api.blueprints.core.bp import bp


@bp.route('/')
def home():
    return "Hello World"
