import os

import psycopg2
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

database_postgres = os.environ["DATABASE"]
host_postgres = os.environ["HOSTNAME_POSTGRES"]
user_postgres = os.environ["USER_POSTGRES"]
password_postgres = os.environ["PASSWORD_POSTGRES"]


class Postgres(BaseModel):

    def connect_postgres():
        conn = psycopg2.connect(
            database=database_postgres, host=host_postgres, user=user_postgres, password=password_postgres)
        cur = conn.cursor()

        return cur, conn
