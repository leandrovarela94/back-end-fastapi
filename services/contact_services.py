from pydantic import BaseModel

from models.contact import Contact
from sql.mysql import Mysql

cur, conn = Mysql.connect_mysql()


class ContactSevices(BaseModel):

    def get_contact_mysql():
        query = 'SELECT * FROM list_contacts'

        cur.execute(query)

        return cur.fetchall()

    def get_one_contacts_mysql(id):
        query = f"SELECT * FROM list_contacts WHERE id ={id}"

        cur.execute(query)

        return cur.fetchall()

    def post_contacts_mysql(contact: Contact, Body=(...)):

        query = f"INSERT INTO list_contacts (name,phone,email) VALUES('{contact.name}','{contact.phone}','{contact.email}')"

        cur.execute(query)

        conn.commit()

    def delete_contact_mysql(id: int):

        cur.execute(f"DELETE FROM list_contacts WHERE id = ({id})")

        conn.commit()

    def update_contact_mysql(contact, id):

        cur.execute(
            f"UPDATE list_contacts set name = '{contact.name}', phone = '{contact.phone}', email ='{contact.email}' WHERE id = {id} ")

        conn.commit()
