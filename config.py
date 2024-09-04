import os
from dotenv import load_dotenv

load_dotenv()

class Expiration_Date:
    EXPIRATION_DATE = os.getenv("EXPIRATION_DATE")

class SERVER_HOST:
    HOST = os.getenv("HOST")

class PostgresConfig(object):
    PG_DATABASES_NAME = os.environ["PG_DATABASES_NAME"]
    PG_DATABASES_USER = os.environ["PG_DATABASES_USER"]
    PG_DATABASES_PASSWORD = os.environ["PG_DATABASES_PASSWORD"]
    PG_DATABASES_HOST = os.environ["PG_DATABASES_HOST"]
    PG_DATABASES_PORT = os.environ["PG_DATABASES_PORT"]