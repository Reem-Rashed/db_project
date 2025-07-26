import json
import enum
import collections
import dataclasses
from typing import List
from uuid import uuid4
import utils

utils.print_name()

# attributes name , contact,contry,gender
# {name:str ,contact:str ,contry:enum,gender:enum}
# ...[{name:str ,contact:str ,contry:enum,gender:enum}]

class Country(enum.Enum):
    """enum to store values of countries"""
    JORDAN=enum.auto()
    SAUDI_ARABIA=enum.auto()
    EGYPT=enum.auto()

class Gender(enum.Enum):
    """enum to store values of gender"""
    MALE=enum.auto()
    FEMALE=enum.auto()

@dataclasses.dataclass
class Contact:
   """ a  dataclass to single contact"""
   contact_id: str=None
   name:str ="Jane Deo"
   contact_number:str = None
   country:Country = Country.JORDAN
   gender:Gender= Gender.FEMALE

@dataclasses.dataclass
class Contacts:
    """ a lise of contact """
    contacts=list[Contact]


class ContactDB:
    """a database containing my contacts"""

    contacts: Contacts = []

    def create_contact(
        self, name: str, contact_number: str, country: Country, gender: Gender
    ):
        truncated_uuid = str(uuid4())
        truncated_uuid = truncated_uuid[::-1]
        truncated_uuid = truncated_uuid[:4].upper()

        contact = Contact(
            contact_id=truncated_uuid,
            name=name,
            contact_number=contact_number,
            country=country,
            gender=gender,
        )

        self.contacts.append(contact)

        print(
            f"Contact ID {truncated_uuid} created successfully.\nContact Name: {name}"
        )
        return contact

    def read_contact(self, contact_id: str) -> Contacts:
        for contact in self.contacts:
            if contact.contact_id == contact_id:
                return contact
        return f"Contact ID {contact_id} does not exist"

    # def update_contact(self, contact_id: str, update_parameter: UpdateParameters) -> Contacts:
    #     match update_parameter:
    #         case UpdateParameters.NAME:


db=ContactDB()
contact = db.create_contact(
    name="Reem Rashed" ,
    contact_number="0098877" ,
    country=Country.JORDAN ,
    gender=Gender.FEMALE
)
print(db.read_contact(contact.contact_id))
