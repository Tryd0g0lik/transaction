from flask import Flask
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from werkzeug.routing import BaseConverter
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from project.models_more.model_user import Users
from project.models_more.model_transaction import Transaction
from project.models_more.model_user_transactions import User_Transaction
from project.models import get_session
from project.commands import create_admin as usersbp
from dotenv_ import (SECRET_KEY, DSN)
class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super(RegexConverter, self).__init__(url_map)
        self.regex = regex

def create_flask() -> dict:
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(__name__)
    csrf = CSRFProtect(app)
   
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
# USER command
app_.register_blueprint(usersbp)
# Admin
admin = Admin(app_, name="transactions_of_user")
session = get_session()
admin.add_view(ModelView(Users, session))
admin.add_view(ModelView(Transaction, session))
admin.add_view(ModelView(User_Transaction, session))

