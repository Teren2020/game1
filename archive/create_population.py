from game1.archive.give_names import generate_name_and_sex
from random import randint
from people_class import Person

def create_population(quantity: int) -> list:
    population = []
    for _ in range(quantity):
        first_name, last_name, sex = generate_name_and_sex()
        age = randint(0, 85)
        person = Person(sex, first_name, last_name, age)
        # person_data = (name, age, sex)
        population.append(person)
    return population


# quantity = 12
# people_data = create_population(quantity)
# for object in people_data:
#     print(object.first_name, object.age)