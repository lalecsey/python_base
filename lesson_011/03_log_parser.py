# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


class LogParser():

    def __init__(self, file_in):
        self.file_in = file_in
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