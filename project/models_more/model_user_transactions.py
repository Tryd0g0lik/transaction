import sqlalchemy as sq
from sqlalchemy.orm import relationship
from datetime import datetime
from project.models_more.model_init import Base

class User_Transaction(Base):
    """
    TODO: This is an average table between the User's table and \
        Transaction's table.
        This a table gives us data of who and when was created a transaction.
    :param user_id: int. Is it who made a transaction.
    :param transaction_id: int. This is an transaction order number.
    :param datetime This is parameter has the save the date and time \
        when was made
    :param users Here is connections with the db Users table.
    :param transaction  Here is connections with the db Transaction table.
    """
    __tablename__ = "user_transaction"
    
    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(
        sq.Integer, sq.ForeignKey("users.id"),
        nullable=False
    )
    trasaction_id = sq.Column(sq.Integer, sq.ForeignKey("transaction.id"),
                              nullable=False)
    datetime = sq.Column(sq.DateTime, default=datetime.utcnow)
    users = relationship("Users", backref="users")
    transaction = relationship("Transaction", backref="transactions",
                               uselist=False)
    def __str__(self):
        return f"User's index: {self.user_id}, \
user transaction's index:{self.trasaction_id}"