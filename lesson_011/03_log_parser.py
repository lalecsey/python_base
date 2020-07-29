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


class LogParser:

    def __init__(self, file_in):
        self.i = 0
        self.file_in = file_in
        self.stat = {}
        self._read_file()

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i <= len(self.stat):
            for self.time in self.stat:
                return [self.time, self.stat[self.time]]
        else:
            raise StopIteration


    def _read_file(self):
        with open(self.file_in, 'r') as file:
            for line in file:
                if line.endswith('NOK\n'):
                    line = line[1:17]
                    if line in self.stat:
                        self.stat[line] += 1
                    else:
                        self.stat[line] = 1



grouped_events = LogParser(file_in='events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')