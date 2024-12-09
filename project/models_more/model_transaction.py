import sqlalchemy as sq

from project.apps import bcrypt
from project.models_more.model_init import Base

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


