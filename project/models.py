import sqlalchemy as sq
from project.apps import bcrypt
from project.models_more.model_init import Base

class Users(Base):
    """This is a model Users of table in db"""
    __tablename__ = "users"
    
    id = sq.Column(sq.Integer, primary_key=True)
    balance = sq.Column(sq.Float, nullable=False)
    commision_rate = sq.Column(sq.Float, nullable=False)
    webhook_url = sq.Column(sq.String(255), nullable=False)
    wallet_address = sq.Column(sq.String(255), unique=True)
    
    def __str__(self):
        return f"Index: {self.id}, Balance: {self.balance}, Commissiom:\
{self.commision_rate}"

class Transaction(Base):
    __tablename__ = "transaction"
    
    id = sq.Column(sq.Integer, primary_key=True)
    amount = sq.Column(sq.Float, nullable=False)
    commission = sq.Column(sq.Float, nullable=False)
    # "ожидание", "подтверждена", "отменена", "истекла"
    status = sq.Column(sq.String(28), nullable=False)
    
    def __str__(self):
        return f" Index: {self.id}, Commission: {self.commission} Status: \
{self.status}"


