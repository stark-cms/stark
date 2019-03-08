from decouple import config

STARK_SECRET_KEY = config("STARK_SECRET_KEY", default=None)
