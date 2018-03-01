from mongoengine import Document, StringField, IntField, BooleanField

class Customer(Document):
    name = StringField()
    gender = IntField()
    email = StringField()
    phone_number = StringField()
    job = StringField()
    contacted = BooleanField()
