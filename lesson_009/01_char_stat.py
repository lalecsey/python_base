# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import os
import zipfile

class Stat():

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._collect_for_line(line=line)

    def _collect_for_line(self, line):
            for char in line:
                if char.isalpha():
                    if char in self.stat:
                        self.stat[char] += 1
                    else:
                        self.stat[char] = 1

    def stat_print(self):
        sort_keys = list(self.stat.keys())
        sort_keys.sort()
        a = ['A', 'a', 'А', 'а']
        for i in sort_keys:
            if i in a:
                print('+', '-' * 5, '+', '-' * 10, '+')
                print('+ {0:^5} + {1:10d} +'.format(i, self.stat[i]))
            else:
                print('+ {0:^5} + {1:10d} +'.format(i, self.stat[i]))

        print('+', '-' * 5, '+', '-' * 10, '+')

# print(os.path.abspath())
stat_mir = Stat(file_name='voyna-i-mir.txt.zip')
stat_mir.collect()
stat_mir.stat_print()


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
