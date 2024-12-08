import sqlalchemy as sq
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project.apps import app_
from project.models_more.model_init import Base
from project.models_more.model_transaction import Transaction
from project.models_more.model_user import Users
from project.models_more.postcresbase import create_database_if_not_exsists
from dotenv_ import (SETTING_POSTGRES_DB,
                     SETTING_POSTGRES_HOST,
                     SETTING_POSTGRES_PORT)
# Create DB
create_database_if_not_exsists(f"{SETTING_POSTGRES_DB}")
# Create on ENGINE
engine = create_engine()
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

def get_session():
    """Receive the session"""
    return Session()
# DATABASE_URL = f"{SETTING_POSTGRES_HOST}:{SETTING_POSTGRES_PORT}"
# DNS: str = app_.config["SQLALCHEMY_DATABASE_URI"]
# engine = sq.create_engine(DNS, pool_pre_ping=True)

