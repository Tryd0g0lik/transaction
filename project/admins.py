""" This is a decorative function for an admin panel."""
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from flask_login import LoginManager
from flask_admin.form import SecureForm
from flask_admin.contrib.fileadmin import FileAdmin

# from project.admins_.user_transaction_admin import MyTransactionAdmin
from project.forms.transaction_sessions.edit_form import \
    FormEditorTransactionData
from project.forms.user_sessions.edit_form import FormEditorUserData
from project.models import get_session
from project.models_more.model_transaction import Transaction
from project.models_more.model_user import Users
from project.models_more.model_user_transactions import User_Transaction


# Decorator

def admin_pannel():
    """
    TODO: This is a decorative function for an admin panel.\n
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
        class MyTransactionDate(ModelView):
            # form_base_class = SecureForm
            form = FormEditorTransactionData
        class MyUserAdminEdit(ModelView):
            # form_base_class = SecureForm
            # can_delete = True
            # ADMIN FORMS
            form = FormEditorUserData
        class MyUserAdmin(ModelView):
            # form_base_class = SecureForm
            # can_delete = True
            # ADMIN FORMS
            form = FormEditorUserData
            # Кнопка будет в шаблоне
            # list_template = 'index.html'
            # create_template ="/templates/index.html"
        # ADMIN PANEL
        app_dict = app_()
        admin = Admin(app_dict["app"])
        
        session = get_session()
        admin.add_views(
            MyUserAdmin(Users, session, name="User", url="/admin/users/"),
            MyTransactionDate(
                User_Transaction, session,
                url="/admin/user_transaction/"
                ),
        )
        # admin.add_views
        # admin.add_view(MyTransactionDate(Transaction, session,
        #                                  url="/admin/transaction/new/"))
        # admin.add_view(MyTransactionDate(User_Transaction, session,
        #                                   url="/admin/user_transaction/"))
        # admin.add_view(MyUserAdmin(User_Transaction, session))
        # https://flask-admin.readthedocs.io/en/latest/advanced/#managing-files-folders
        admin.add_view(FileAdmin("project/static", '/static/', name='Static Files'))
        
        # LOGIN
        login_manager = LoginManager()
        login_manager.init_app(app_dict["app"])
        
        # Loder of user
        @login_manager.user_loader
        def user_loader(user_id):
            from project.apps import get_session
            session = get_session()
            return session(Users).query.get(user_id)

        return app_dict
    return wrapper

        
