import os


class Config():
    CSRF_ENABLE = True
    SECRET = "123456@Aa"
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLETE_FOLDER = os.path.join(ROOT_DIR, "templates")
    APP = None


class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = "localhost"
    PORT_HOST = 8000
    URL_MAIN = "http://%s/%s" % (IP_HOST, PORT_HOST)
    SQLALCHEMY_DATABASE_URI = "projetoPython"


app_config = {
    "development": DevelopmentConfig()
}

app_active = os.getenv("FLASK_ENV")
if app_active is None:
    app_active = "development"
