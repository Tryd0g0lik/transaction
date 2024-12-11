# from flask_admin.contrib.sqla import ModelView
#
# from project.forms.transaction_sessions.edit_form import \
#     FormEditorTransactionData
# from project.models_more.model_transaction import Transaction
#
# from project.models_more.model_user import Users
# from project.models_more.model_user_transactions import User_Transaction


# class MyTransactionAdmin(ModelView):
#     form_base_class = FormEditorTransactionData

    # def get_create_form(self):
    #     from project.models import get_session
    #     session = get_session()
    #     form = super().get_create_form()
    #     # Заполнение поля user_id списком пользователей
    #     user_list = session(Transaction).query.all()
    #     form.user_id.choices = [(user.id, str(user)) for user in user_list]
    #     return form
    #
    # def on_model_change(self, form, model, is_created):
    #     from project.models import get_session
    #     session = get_session()
    #     # Создание записи в User_Transaction после создания Transaction
    #     if is_created:
    #         user_transaction = User_Transaction(user_id=form.user_id.data,
    #                                              transaction_id=model.id)
    #         session.add(user_transaction)
    #         session.commit()