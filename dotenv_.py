"""Here data imports from the file '.env' of django project"""

import os
from pathlib import Path
import dotenv

dotenv.load_dotenv()

SETTING_POSTGRES_DB = os.getenv(
    "SETTING_POSTGRES_DB", ""
)
SETTING_POSTGRES_USER = os.getenv(
    "SETTING_POSTGRES_USER", ""
)
SETTING_POSTGRES_PASSWORD = os.getenv(
    "SETTING_POSTGRES_PASSWORD", ""
)
SETTING_POSTGRES_HOST = os.getenv(
    "SETTING_POSTGRES_HOST", ""
)
SETTING_POSTGRES_PORT = os.getenv(
    "SETTING_POSTGRES_PORT", ""
)
SECRET_KEY = os.getenv("SECRET_KEY", "")
EMAIL_HOST = os.getenv("MAIL_SERVER", "")
EMAIL_PORT = os.getenv("EMAIL_PORT", "")


MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "")
MAIL_USERNAME = os.getenv("MAIL_USERNAME", "")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "")
MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", "")
TOKEN_TIME_MINUTE_EXPIRE = os.getenv("TOKEN_TIME_MINUTE_EXPIRE", "")
HOST_TO_BACKEND = os.getenv("HOST_TO_BACKEND", "")
PORT_TO_BACKEND = os.getenv("PORT_TO_BACKEND", "")
PROTOCOL_TO_BACKEND = os.getenv(
    "PROTOCOL_TO_BACKEND", ""
)
DSN = f"postgresql://{SETTING_POSTGRES_USER}:\
{SETTING_POSTGRES_PASSWORD}@\
{SETTING_POSTGRES_HOST}:\
{SETTING_POSTGRES_PORT}/\
{SETTING_POSTGRES_DB}"

REDIS_URL = os.getenv("REDIS_URL", "")