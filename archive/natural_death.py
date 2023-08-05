'''
функция проверки появления естественной смерти
чем старше человек тем больше шансов что он умрет естественоной смертью
диапозон лет, когда умирает человек естественной смерью: 65 -- 130
шанс умереть в 64 лет - 0%
функция сделана для ежегодного запуска
'''
def check_natural_death(population: list) -> list:
    for object in population:
        age = object.age
        over64 = age - 64
        chance_natural_death = over64 * u
        u = 100 / 65
        dice = randint(0, 100)
        is_dead = dice < chance_natural_death
        if is_dead == False:
            age += 1
        else:
            age = -1
        object.age = age


    return population