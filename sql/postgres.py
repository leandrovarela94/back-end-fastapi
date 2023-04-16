import psycopg2
from pydantic import BaseModel


class Postgres(BaseModel):

    def connect_postgres():
        conn = psycopg2.connect(
            database='containers-us-west-179.railway.app', user='postgres', password='grT1581tkP6rYZy9DXVQ')

        cur = conn.cursor()

        return cur, conn
