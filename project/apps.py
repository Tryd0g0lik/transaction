from flask import Flask

from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from werkzeug.routing import BaseConverter
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import (sq, Users, Transaction)
from dotenv_ import (EMAIL_HOST, EMAIL_PORT, MAIL_DEFAULT_SENDER, MAIL_PASSWORD,
                     MAIL_USE_TLS, MAIL_USERNAME, SECRET_KEY,
                     SETTING_POSTGRES_DB,
                     SETTING_POSTGRES_HOST,
                     SETTING_POSTGRES_PASSWORD,
                     SETTING_POSTGRES_PORT,
                     SETTING_POSTGRES_USER)
class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super(RegexConverter, self).__init__(url_map)
        self.regex = regex

def create_flask() -> dict:
    app = Flask(__name__, template_folder="templates")
    app.config.form_object(__name__)
    csrf = CSRFProtect(app)
    DSN = f"postgresql://{SETTING_POSTGRES_USER}:\
    {SETTING_POSTGRES_PASSWORD}@\
    {SETTING_POSTGRES_HOST}:\
    {SETTING_POSTGRES_PORT}/\
    {SETTING_POSTGRES_DB}"
    app.config["SQLALCHEMY_DATABASE_URI"] = DSN
    app.url_map.converters["regex"] = RegexConverter
    app.config["JWT_COOKIE_SECURE"] = True
    
    bcrypt = Bcrypt(app)
    
    app.config["SECRET_KEY"] = SECRET_KEY
    bootstrap = Bootstrap(app)

    app.config["BOOTSTRAP"] = bootstrap

    # LOGIN SESSION
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login"
    
    # Celery
    
    return {
        "app": app,
        "csrf": csrf,
        "bcrypt": bcrypt,
        "login_manager": login_manager,
    }



flask_dict = create_flask()
app_ = flask_dict["app"]
csrf = flask_dict["csrf"]
bcrypt = flask_dict["bcrypt"]
login_manager = flask_dict["login_manager"]
app_type = type(app_)


admin = Admin(app_)
admin.add_view(ModelView(Users, sq))