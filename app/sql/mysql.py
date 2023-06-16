import os

import mysql.connector
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

database_mysql = os.environ["DATABASE"]
host_mysql = os.environ["HOSTNAME_MYSQL"]
user_mysql = os.environ["USER_MYSQL"]
password_mysql = os.environ["PASSWORD_MYSQL"]


class Mysql:

    def connect_mysql():
        try:
            conn = mysql.connector.connect(
                database=database_mysql, host=host_mysql, user=user_mysql, password=password_mysql)
            cur = conn.cursor()
        except mysql.connector.Error as e:
            print(f"Erro na conexão ao Banco de Dados: {e}")
        return cur, conn

    def disconnect_mysql(conn):
        if conn:
            conn.close()
