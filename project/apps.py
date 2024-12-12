from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from werkzeug.routing import BaseConverter

from project.admins import admin_pannel
from project.models import get_session
from dotenv_ import (SECRET_KEY, DSN)



@admin_pannel()
def create_flask():
    class RegexConverter(BaseConverter):
        def __init__(self, url_map, regex):
            super(RegexConverter, self).__init__(url_map)
            self.regex = regex
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
    TODO: COmmand for a create the user
    :return:
    """
    # from project.apps import get_session
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