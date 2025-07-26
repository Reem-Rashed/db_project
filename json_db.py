import json
import enum
import uuid
import typing

import pydantic

import utils

utils.print_name()

# python primitive data types: str, int, float, bool, None
# attributes: name, contact, country, gender

# shape of data:
# [{"name": str, "contact_number": str, "country": enum, "gender": enum},
# ... ,
# {"name": str, "contact_number": str, "country": enum, "gender": enum}]


# type definitions


class Country(str, enum.Enum):
    """enum to store values of countries"""

    JORDAN = "JORDAN"
    SAUDI_ARABIA = "SAUDI_ARABIA"
    EGYPT = "EGYPT"


class Gender(str, enum.Enum):
    """enum to store values of genders"""

    MALE = "MALE"
    FEMALE = "FEMALE"


class Contact(pydantic.BaseModel):
    """a pydantic base model to store a single contact"""

    contact_id: str = None
    name: str = "John Doe"
    contact_number: str = None
    country: Country = Country.EGYPT
    gender: Gender = Gender.MALE


class Contacts(pydantic.BaseModel):
    """a list of contacts"""

    # go back to the concept of factories
    contacts: typing.List[Contact] = pydantic.Field(default_factory=list)


print(dir(Contacts))


class Field(enum.Enum):
    NAME = enum.auto()
    CONTACT_NUMBER = enum.auto()
    GENDER = enum.auto()
    COUNTRY = enum.auto()


class ContactDB:
    """a database containing my contacts"""

    contacts: Contacts = []

    def create_contact(
        self, name: str, contact_number: str, country: Country, gender: Gender
    ) -> Contact:
        truncated_uuid = str(uuid.uuid4())
        truncated_uuid = truncated_uuid[::-1]
        truncated_uuid = truncated_uuid[:4].upper()

        try:
            valid_number = self.validate_number(contact_number)
            if valid_number:
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
        except Exception as e:
            raise e

    def read_contact(self, contact_id: str) -> Contact:
        for contact in self.contacts:
            if contact.contact_id == contact_id:
                return contact
        return f"Contact ID {contact_id} does not exist"

    def get_contact(self, contact_id: str) -> Contact:
        for contact in self.contacts:
            if contact.contact_id == contact_id:
                return contact

    def validate_number(self, contact_number: str) -> bool:
        # check if number is 10 digits
        # check if number starts with 079, 078 or 077
        num_of_digits = len(contact_number)
        first_two_digits = contact_number[:2]
        third_digit = contact_number[2]

        if (
            (num_of_digits == 10)
            and (first_two_digits == "07")
            and ((third_digit == "7") or (third_digit == "8") or (third_digit == "9"))
        ):
            return True
        raise ValueError(
            f"Incorrect Number Entered: {contact_number}.\nNumber should be formatted as 07XXXXXXXX and should start with 079 or 078 or 077"
        )

    def update_contact(
        self,
        contact_id: str,
        update_field: Field,
        update_parameter: typing.Union[str, Gender, Country],
    ) -> Contact:
        match update_field:
            case Field.NAME:
                contact = self.get_contact(contact_id)
                contact.name = update_parameter
                return contact
            case Field.CONTACT_NUMBER:
                try:
                    valid_number = self.validate_number(update_parameter)
                    if valid_number:
                        contact = self.get_contact(contact_id)
                        contact.contact_number = update_parameter
                        return contact
                except Exception as e:
                    raise e

            case Field.GENDER:
                contact = self.get_contact(contact_id)
                contact.gender = update_parameter
                return contact

            case Field.COUNTRY:
                contact = self.get_contact(contact_id)
                contact.country = update_parameter
                return contact

    def delete_contact(self, contact_id: str):
        for idx, contact in enumerate(self.contacts):
            if contact.contact_id == contact_id:
                del self.contacts[idx]
                print(f"Contact ID {contact_id} deleted successfully")
                return

        raise ValueError(f"Contact ID {contact_id} does not exist.")

    def contact_count(self):
        return f"DB has {len(self.contacts)} contacts."

    def save_db(self, file_name: str):
        serializable_contacts = [contact.model_dump() for contact in self.contacts]
        print(serializable_contacts)
        json.dump(
            serializable_contacts, open(f"{file_name}.json", "w", encoding="utf-8")
        )


db=ContactDB()
contact = db.create_contact(
    name="Reem Rashed" ,
    contact_number="0795432212" ,
    country=Country.JORDAN ,
    gender=Gender.FEMALE
)
print(db.read_contact(contact.contact_id).__dict__)
print(db.contact_count())

db.update_contact(contact.contact_id, Field.CONTACT_NUMBER, "0785907266")
db.save_db("db_1")

db.delete_contact(contact.contact_id)

print(db.contact_count())
