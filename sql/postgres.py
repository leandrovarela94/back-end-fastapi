import os

import psycopg2
from pydantic import BaseModel


class Postgres(BaseModel):

    def connect_postgres():
        conn = psycopg2.connect(
            database=os.environ['DATA_BASE'], user=os.environ['USER_POSTGRES'], password=os.environ['PASSWORD_POSTGRES'])

        cur = conn.cursor()

        return cur, conn
