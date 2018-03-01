import mlab
from models.service import Service
from random import randint, choice
from faker import Faker

fake = Faker()

mlab.connect()
for i in range(50):
    print('Saving service', i + 1, '.....')
    service = Service(name=fake.name(), yob=randint(1990, 2000), gender=randint(0,1), height=randint(150, 180),
            phone_number=fake.phone_number(), address=fake.address(), status=choice([True, False]))

    service.save()

# print(fake.name())
