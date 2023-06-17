import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.contact import Contact
from services.contact_services import ContactSevices

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_health():
    return {f"Servidor Online"}


@app.get("/contacts/")
async def read_all():

    result = ContactSevices.get_contact_mysql()

    response_final = [{
        "id": item[0],
        "name": item[1],
        "phone": item[2],
        "email": item[3]
    }for item in result
    ]

    return response_final


@app.get("/contacts/{id}")
async def read_one(id: int):

    result = ContactSevices.get_one_contacts_mysql(id)

    response_final = [{
        "id": item[0],
        "name": item[1],
        "phone": item[2],
        "email": item[3]
    }for item in result
    ]

    return response_final


@app.post("/contacts/")
def create_contact(contact: Contact):

    ContactSevices.post_contacts_mysql(contact)

    return {f"Sucess Created"}


@app.delete("/contacts/{id}")
def delete_contact(id: int):

    ContactSevices.delete_contact_mysql(id)
    return {f"Sucess : Deleted"}


@app.put("/contacts/{id}")
def update_contact(contact: Contact, id: int):

    ContactSevices.update_contact_mysql(
        contact, id)

    return {f"Sucess Updated"}
