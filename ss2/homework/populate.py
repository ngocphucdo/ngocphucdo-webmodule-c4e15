import mlab
from models.customer import customer
from random import randint, choice
from faker import Faker

fake = Faker()

mlab.connect()
for i in range(50):
    print('Saving service', i + 1, '.....')
    customer1 = customer(name=fake.name(),gender=randint(0,1),email=fake.email(),
        phone_number=fake.phone_number(),job=fake.job(),contacted=choice([True, False]))

    customer1.save()
