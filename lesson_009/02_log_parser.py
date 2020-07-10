# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class LogParser():


    def __init__(self, file_in, file_out ):
        self.file_in = file_in
        self.file_out = file_out
        self.stat = {}

    def read_file(self):
        with open(self.file_in, 'r') as file:
            for line in file:
                if line.endswith('NOK\n'):
                    line = line[1:17]
                    if line in self.stat:
                        self.stat[line] += 1
                    else:
                        self.stat[line] = 1


    def write_file(self):
        file = open(self.file_out, 'w', encoding='utf8')
        for time in self.stat.keys():
            line = f' [{time}] {str(self.stat[time])}\n'
            file.write(line)
        file.close()

    def stat_prtint(self):
        print(self.stat)



first_log = LogParser(file_in='events.txt', file_out='events_log.txt')
first_log.read_file()
first_log.write_file()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
