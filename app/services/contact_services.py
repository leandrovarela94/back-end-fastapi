from models.contact import Contact
from pydantic import BaseModel
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

    def post_contacts_mysql(contact: Contact):

        query = f"INSERT INTO list_contacts (name,phone,email) VALUES(%s,%s,%s)"
        val = (contact.name, contact.phone, contact.email)
        cur.execute(query, val)

        conn.commit()
        conn.close()

    def delete_contact_mysql(id: int):

        cur.execute(f"DELETE FROM list_contacts WHERE id = ({id})")

        conn.commit()
        conn.close()

    def update_contact_mysql(contact, id):
        query = f"UPDATE list_contacts SET name = %s, phone = %s, email = %s WHERE id = %s "
        val = (contact.name, contact.phone, contact.email, id)
        cur.execute(query, val)

        conn.commit()
        conn.close()
