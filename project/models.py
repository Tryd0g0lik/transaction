
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from project.models_more.model_init import Base
from project.models_more.postcresbase import create_database_if_not_exsists
from dotenv_ import (SETTING_POSTGRES_DB, DSN)
# Create DB
create_database_if_not_exsists(f"{SETTING_POSTGRES_DB}")


def get_session():
    # Create on ENGINE
    engine = create_engine(DSN)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    """Receive the session"""
    return Session()
