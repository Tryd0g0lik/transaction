from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from flask_login import LoginManager
from project.models import get_session
from project.models_more.model_user import Users

# Decorator
def admin_pannel():
    """
    TODO: This is a decorative function for ab admin panel.\n
        The function for decorate is 'create_admin' from the 'app.py'\n
        Old 'create_admin'.\n
        The old 'create_admin' function returns \n
        ```text \n
        flask_dict = create_flask() \n
        app_ = flask_dict["app"]\n
        csrf = flask_dict["csrf"]\n
        bcrypt = flask_dict["bcrypt"]\n
        ``` \n
        New 'create_admin'\n
        The new 'create_admin' function receives an administration panel and \n
        ```text \n
        flask_dict = create_flask\n
        app_ = flask_dict["app"]\n
        csrf = flask_dict["csrf"]\n
        bcrypt = flask_dict["bcrypt"]\n
        ```\n
        The admin panel is access to path '/admin/'.
    """
    def wrapper(app_) -> dict:
        class MyUserAdmin(ModelView):
            pass
            # Кнопка будет в шаблоне
            # list_template = 'index.html'
            # create_template ="/templates/index.html"
        # ADMIN PANEL
        app_dict = app_()
        admin = Admin(app_dict["app"])
        
        session = get_session()
        admin.add_view(MyUserAdmin(Users, session))
        # LOGIN
        login_manager = LoginManager()
        login_manager.init_app(app_dict["app"])
        
        # Loder of user
        @login_manager.user_loader
        def user_loader(user_id):
            return Users.get(user_id)

        return app_dict
    return wrapper

        
