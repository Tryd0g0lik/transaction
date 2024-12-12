"""Here contain structure for 'Users' table of db """
import sqlalchemy as sq
from project.models_more.model_init import Base


class Users(Base):
    """
    This is a model Users of table in db.
    :param balance: float This is a balance of users.
    :param commission_rate: float. This is the size of commission.
    :param webhook_url: str. url.
    :param wallet_address: str. This is a webhook.
    """
    __tablename__ = "users"
    
    id = sq.Column(sq.Integer, primary_key=True)
    balance = sq.Column(sq.Float, nullable=False)
    commission_rate = sq.Column(sq.Float, nullable=False)
    webhook_url = sq.Column(sq.String(255), nullable=False)
    wallet_address = sq.Column(sq.String(255), unique=True)
    
    def __str__(self):
        return f"Index: {self.id}, Balance: {self.balance}, Commissiom:\
{self.commission_rate}"
    
    #
