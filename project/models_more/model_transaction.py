"""Here contain structure for 'Transaction' table of db """
import sqlalchemy as sq
from project.models_more.model_init import Base

class Transaction(Base):
    """
    :param amount: float. It's sum of transaction.
    :param commission: float. It's the size of commission.
    :param status: str. here is we can to choice only this status: \
    'ожидание', 'подтвеждена', 'отменена', 'истекла'.
    """
    __tablename__ = "transaction"
    
    id = sq.Column(sq.Integer, primary_key=True)
    amount = sq.Column(sq.Float, nullable=False)
    commission = sq.Column(sq.Float, nullable=False)
    status = sq.Column(sq.String(28), nullable=False)
    
    def __str__(self):
        return f" Index: {self.id}, Commission: {self.commission} Status: \
{self.status}"


