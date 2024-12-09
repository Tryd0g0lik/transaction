import click
from flask import Blueprint
# from flask.cli import with_appcontext
# @with_appcontext
usersbp = Blueprint('users', __name__)
@usersbp.cli.command("create-users")
def create_admin():
    """
    TODO: COmmand for a create the user
    :return:
    """
    from project.apps import get_session
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