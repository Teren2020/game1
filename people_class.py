from random import randint, choice
from game1.archive.give_names import generate_name_and_sex
class Person:
    CHANCE_MARRIAGE = 20       # вероятность женитьбы в процентах каждый год л
    population = []


    def __init__(self, sex, first_name, last_name, age):
        self.sex = sex
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.spouse = None

    def __str__(self):

        return f'{self.first_name} {self.last_name}, {str(self.age)}'

    '''
    функция создает список, состоящий из объектов класса Person в классе Person
    функция принимает количество нужных элементов списка
    функция ничего не возвращает
    '''

    @classmethod
    def create_population(cls, quantity: int):
        for _ in range(quantity):
            first_name, last_name, sex = generate_name_and_sex()
            age = randint(0, 85)
            person = Person(sex, first_name, last_name, age)
            # person_data = (name, age, sex)
            cls.population.append(person)

    '''
    функция получает список population и делает проверку каждому человеку, должен ли он умереть от естественной смертью, 
    чем старше человек тем больше шансов что он умрет естественоной смертью
    диапозон лет, когда умирает человек естественной смерью: 65 -- 130
    шанс умереть в 64 лет - 0%, в 130 -- 100
    функция ничего не приниает
    функция ничего не возвращает
    функция сделана для ежегодного запуска
    '''

    @classmethod
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


    '''
    функция изменяет фамилию объект класса
    функция принимает определенный объект и новую фамилию
    функция ничего не возвращает
    '''

    def change_lastname(self, new_lastname):
        self.last_name = new_lastname

    '''
    функция примениятся к женщине, матери ребенка, и создает новый объект класса с возрастом 0
    функция приниает отца ребенка
    функция возвращает ребенка 
    '''

    def create_child(self, father):
        dice = randint(0,1)
        if dice == 1:
            lastname = father.last_name
        else:
            lastname = self.last_name
        first_name, last_name, sex = generate_name_and_sex()
        child = Person(age=0, first_name=first_name, sex=sex, last_name=lastname)

        return child

    '''
    функция перебирает варианты возможных супруг и возвращает нужный
    функция принимает пол и возраст женящегося
    функция возвращает супруга
    '''

    @classmethod
    def choose_spouse(cls, sex, age):
        list_suitable = []
        for person in cls.population:


            if randint(1, 100) <= 100 - (abs(age - person.age)) * 3 and person.age >= 18:
                age_is_normal = True
            else:
                age_is_normal = False

            if person.sex != sex and age_is_normal and person.spouse == None:
                list_suitable.append(person)

        spouse = choice(list_suitable)
        return spouse

    '''
    функция проходит по всем неженатым объектам в списке population и определяет случайным образом произошла ли
    женитьба. Если произошла то функция добавляет новый параметр объекту класса Person на ком он женат.
    функция ничего не принимает
    функция ничего не возвращает 
    Сделана для ежегодного запуска
    '''

    @classmethod
    def marriage_people(cls):
        for person in cls.population:
            if not person.spouse and person.age > 18:
                dice = randint(1, 100)
                if dice <= cls.CHANCE_MARRIAGE:
                    spouse = cls.choose_spouse(person.sex, person.age)
                    person.spouse = spouse
                    print(f'{person} и {spouse} поженились')

Person.create_population(200)
for el in Person.population:
    print(el)
Person.marriage_people()
Person.check_natural_death()
for el in Person.population:
    print(el)

'''
добавить в функцию формулу которая будет уменьшать вероятность женитьбы при разнице в возрасте, а именно на 1 процент за каждый год разницы в возрасте
изучить документацию метода choice
natural death перенести в метод, прибратся (написать комментарии)
'''










