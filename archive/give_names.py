from faker import Faker
from random import randint


def generate_name_and_sex():
    fake = Faker('ru_RU')  # Set the locale to Russian
    dice = randint(0, 1)
    if dice == 0:
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
        sex = 'М'
    else:
        first_name = fake.first_name_female()
        last_name = fake.last_name_female()
        sex = 'Ж'


    return first_name, last_name, sex

