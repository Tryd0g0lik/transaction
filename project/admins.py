from flask_admin.contrib.sqla import ModelView

from flask_admin import Admin, AdminIndexView, expose, helpers
from flask_jwt_extended import current_user
from flask_login import LoginManager

# from project.apps import app_ as app
from project.models import get_session
from project.models_more.model_transaction import Transaction
from project.models_more.model_user import Users
from project.models_more.model_user_transactions import User_Transaction
# from project.views import UserAdmin

# def admin_pannel_params(name_):
def admin_pannel():
    def wrapper(app_) -> dict:
        class MyUserAdmin(ModelView):
            pass
            # Кнопка будет в шаблоне
            # list_template = 'index.html'
            # create_template ="/templates/index.html"
        app_dict = app_()
        admin = Admin(app_dict["app"])
        
        session = get_session()
        admin.add_view(MyUserAdmin(Users, session))
        # return admin
        login_manager = LoginManager()
        login_manager.init_app(app_dict["app"])
        
        # login_manager.login_view = "login"
        @login_manager.user_loader
        def user_loader(user_id):
            return Users.get(user_id)

        return app_dict
    return wrapper
    # return admin_pannel
        
