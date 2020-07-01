# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

from random import randint
from termcolor import cprint

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_for_cats(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за кошачей едой.'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food_cat += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def pick_up_cat(self, cat):
        house = self.house
        cat.house = house
        cprint('{} подобрал кота по имени {}'.format(self.name, cat.name_cat), color='cyan')


    def clean_the_house(self):
        cprint('{} убрался в доме'.format(self.name), color='magenta')
        self.house.dirt -= 100
        self.fullness -= 20

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 10:
            self.shopping()
        elif self.house.food_cat <= 10:
            self.shopping_for_cats()
        elif self.house.money <= 50:
            self.work()
        elif self.house.dirt > 100:
            self.clean_the_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 50
        self.food_cat = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, еды у кота {}, грязь в доме {}'.format(
            self.food, self.money, self.food_cat, self.dirt)


class Cat:

    def __init__(self, name):
        self.name_cat = name
        self.fullness_cat = 20
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name_cat, self.fullness_cat)

    def sleep(self):
        cprint('{} спит'.format(self.name_cat), color='green')
        self.fullness_cat -= 10

    def eat(self):
        if self.house.food_cat >= 10:
            cprint('{} поел'.format(self.name_cat), color='yellow')
            self.fullness_cat += 20
            self.house.food_cat -= 10
        else:
            cprint('{} нет еды'.format(self.name_cat), color='red')

    def soil(self):
        cprint('{} рвёт обои'.format(self.name_cat), color='green')
        self.fullness_cat -= 10
        self.house.dirt += 5

    def act(self):
        if self.fullness_cat <= 0:
            cprint('{} умер...'.format(self.name_cat), color='red')
            return
        dice = randint(1, 6)
        if self.fullness_cat < 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.eat()
        else:
            self.soil()



citizens = [
   Man(name='Кенни')
]

cats = [
    Cat(name='Пушкин')
]

my_sweet_home = House()

for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for i in range(len(cats)):
    citizens[0].pick_up_cat(cats[i])

# citizens[0].pick_up_cat(cats[0])

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    for cat in cats:
        cat.act()
    print('--- в конце дня ---')
    for cat in cats:
        print(cat)
    for citisen in citizens:
        print(citisen)
    print(my_sweet_home)


