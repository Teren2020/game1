from game1.archive import create_population, natural_death

amount_of_people = 10
population = create_population.create_population(amount_of_people)
for object in population:

    print(object.first_name, object.last_name, object.age)
population = natural_death.check_natural_death(population)
for object in population:

    print(object.first_name, object.last_name, object.age)

