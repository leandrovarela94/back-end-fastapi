import psycopg2
from pydantic import BaseModel


class Postgres(BaseModel):

    def connect_postgres():
        conn = psycopg2.connect(
            database='contacts', host='localhost', user='postgres', password='custelinha')

        cur = conn.cursor()

        return cur, conn
