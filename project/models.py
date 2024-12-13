"""
Here is containing the 'get_session' function, We will have receives \
an integration of new data to the db.
"""
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from project.models_more.model_init import Base
from project.models_more.postcresbase import create_database_if_not_exsists
from dotenv_ import (SETTING_POSTGRES_DB, DSN)
# Create DB
create_database_if_not_exsists(f"{SETTING_POSTGRES_DB}")


def get_session():
    from project.logs import configure_logging
    log = logging.getLogger(__name__)
    configure_logging(logging.INFO)
    # Create on ENGINE
    log.info("[get_session]: START")
    log.info(f"[get_session]: DSN {DSN}")
    engine = create_engine(DSN)
    log.info("[get_session]: received the engine of sqlalchemy")
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    log.info("[get_session]: before run 'Session'")
    """Receive the session"""
    return Session()
