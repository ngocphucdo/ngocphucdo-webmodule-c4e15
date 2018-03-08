from mongoengine import Document, StringField, IntField, BooleanField, ListField
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() #0: female, 1: male
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    description = StringField()
    image = StringField()
    measurments = ListField()
