from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    money_earned = 0
    food_eaten = 0

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.food_cat = 0

    def __str__(self):
        return 'В доме осталось еды {}, осталось денег {}, грязи в доме {}'.format(
            self.food, self.money, self.dirt)


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.happy = 100

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.food >= 30:
            self.fullness += 30
            self.house.food -= 30
            cprint('{} кушает'.format(self.name), color='green')
            House.food_eaten += 30
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def striked_cat(self):
        cprint('{} гладит кота'.format(self.name), color='magenta')
        self.fullness -= 10
        self.happy += 5


class Husband(Man):

    def __init__(self, name, house):
        super().__init__(name=name)
        self.house = house

    def __str__(self):
        res = super().__str__()
        return res + ', счастья {}'.format(self.happy)

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер от голода ...'.format(self.name), color='red')
        elif self.happy < 10:
            cprint('{} умер от дипресии ...'.format(self.name), color='red')
            return
        if self.house.dirt >= 90:
            self.happy -= 5
        self.house.dirt += 5
        dice = randint(1, 5)
        if self.fullness <= 20:
            self.eat()
        elif self.house.money <= 90:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.striked_cat()
        else:
            self.gaming()

    def work(self):
        cprint('{} сходил на работу.'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10
        self.happy -= 5
        House.money_earned += 150

    def gaming(self):
        cprint('{} играет в WoT.'.format(self.name), color='yellow')
        self.fullness -= 10
        self.happy += 20

    def striked_cat(self):
        pass


class Wife(Man):
    fur_coat = 0

    def __init__(self, name, house):
        super().__init__(name=name)
        self.house = house

    def __str__(self):
        res = super().__str__()
        return res + ', счастья {}'.format(self.happy)

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер от голода ...'.format(self.name), color='red')
        elif self.happy < 10:
            cprint('{} умер от дипресии ...'.format(self.name), color='red')
            return
        if self.house.dirt >= 90:
            self.happy -= 5
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 60:
            self.shopping()
        elif self.house.food_cat <= 20:
            self.shopping_cat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.shopping()
        elif dice == 3:
            self.striked_cat()
        elif dice == 4:
            self.buy_fur_coat()
        else:
            self.clean_house()

    def shopping(self):
        self.fullness -= 10
        if self.house.money >= 90:
            cprint('{} сходиила в магазин за едой'.format(self.name), color='blue')
            self.house.money -= 90
            self.house.food += 90
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_cat(self):
        self.fullness -= 10
        if self.house.money >= 40:
            cprint('{} сходиила в магазин за едой для кота'.format(self.name), color='blue')
            self.house.money -= 40
            self.house.food_cat += 40
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buy_fur_coat(self):
        self.fullness -= 10
        if self.house.money >= 350:
            cprint('{} купила шубу.'.format(self.name), color='yellow')
            self.happy += 60
            Wife.fur_coat += 1
        else:
            cprint('{} на шубу нет денег'.format(self.name), color='red')


    def clean_house(self):
        cprint('{} убралась в доме'.format(self.name), color='magenta')
        self.house.dirt = 0
        self.fullness -= 10
        self.happy -= 5

class Cat:

    def __init__(self, name, house):
        self.name_cat = name
        self.fullness_cat = 30
        self.house = house

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name_cat, self.fullness_cat)

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

    def eat(self):
        if self.house.food_cat >= 10:
            cprint('{} поел'.format(self.name_cat), color='yellow')
            self.fullness_cat += 20
            self.house.food_cat -= 10
        else:
            cprint('{} нет еды'.format(self.name_cat), color='red')

    def sleep(self):
        cprint('{} спит'.format(self.name_cat), color='green')
        self.fullness_cat -= 10

    def soil(self):
        cprint('{} рвёт обои'.format(self.name_cat), color='green')
        self.fullness_cat -= 10
        self.house.dirt += 5



class Child(Man):

    def __init__(self, name, house):
        super().__init__(name=name)
        self.house = house

    def __str__(self):
        res = super().__str__()
        return res + ', счастья {}'.format(self.happy)

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 2)
        if self.fullness <= 20:
            self.eat()
        if dice == 1:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food >= 10:
            self.fullness += 10
            self.house.food -= 10
            cprint('{} кушает'.format(self.name), color='green')
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        cprint('{} спит'.format(self.name), color='green')
        self.fullness -= 10

# home = House()
# serge = Husband(name='Сережа', house=home)
# masha = Wife(name='Маша', house=home)

# print(serge)
# print(masha)
# print(home)
#
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')
#
# cprint('Всего шуб куплено {}'.format(Wife.fur_coat), color='yellow')
#


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов



######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)



######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
kolya = Child(name='Коля', house=home)
murzik = Cat(name='Мурзик', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')

cprint('Всего заработал денег {}'.format(House.money_earned), color='yellow')
cprint('Всего еды съели {}'.format(House.food_eaten), color='yellow')
cprint('Всего шуб куплено {}'.format(Wife.fur_coat), color='yellow')
# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

