"""
Here is the run app of Flask and
USER's COMMAND of user's interface/ It's for create random of admin
"""
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from werkzeug.routing import BaseConverter

from project.admins import admin_pannel
from project.models import get_session
from dotenv_ import (SECRET_KEY, DSN,)
from flask_redis import FlaskRedis

@admin_pannel()
def create_flask():
    """
    Creating the app flask
    :return:
    """

    class RegexConverter(BaseConverter):
        def __init__(self, url_map, regex):
            super(RegexConverter, self).__init__(url_map)
            self.regex = regex

    app = Flask(__name__, template_folder="templates")
    app.config.from_object(__name__)
    
    # CONFIG APP
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = DSN
    app.config["JWT_COOKIE_SECURE"] = True
    
    
    # Converter reg-expression
    app.url_map.converters["regex"] = RegexConverter
    # EXTENSIONS
    bcrypt = Bcrypt(app)
    bootstrap = Bootstrap(app)
    app.config["BOOTSTRAP"] = bootstrap
    csrf = CSRFProtect(app)

    # CREATE REDIS
    redis_client = FlaskRedis()
    # REDIS INSTALL to the app
    redis_client.init_app(app)
    return {
        "app": app,
        "csrf": csrf,
        "bcrypt": bcrypt,
    }

flask_dict = create_flask
app_ = flask_dict["app"]
csrf = flask_dict["csrf"]
bcrypt = flask_dict["bcrypt"]
app_type = type(app_)


# USER's COMMAND of user's interface
@app_.cli.command("create-users")
def create_admin():
    """
    TODO: Command for a create the user
    :return:
    """
    from project.models_more.model_user import Users
    
    session = get_session()
    try:
        admin_user = Users(
            balance=0.0,
            commission_rate=0.05,
            webhook_url='http://example.com/webhook',
            wallet_address='test_wallet'
        )
        session.add(admin_user)
        session.commit()
        print("Admin user created.")
    except Exception as e:
        print(f"Admin user not created. Mistake => {e.__str__()}")
    finally:
        session.close()