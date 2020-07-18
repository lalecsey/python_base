# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):
    pass
class NotEmailError(Exception):
    pass

class ErrorChecking():

    def __init__(self, line):
        self.line = line
        self.name = None
        self.email = None
        self.age = None
        self.checking()

    def _checking_line(self):
        if self.name and self.email and self.age:
            return True
        else:
            raise ValueError('НЕ присутсвуют все три поля')

    def _checking_name(self):
        if self.name.isalpha():
            return True
        else:
            raise NotNameError('поле имени содержит НЕ только буквы')

    def _checking_email(self):
        if ('@' in self.email) and ('.' in self.email):
            return True
        else:
            raise NotEmailError('поле содержит НЕ email')

    def _checking_age(self):
        if 10 <= int(self.age) <= 99:
            return True
        else:
            raise ValueError('Не является числом в диапозоне от 10 до 99')

    def checking(self):
        self.name, self.email, self.age = self.line.split(' ')
        self._checking_line()
        self._checking_name()
        self._checking_email()
        self._checking_age()
        print(self.name)


path = 'registrations.txt'
good = 'registrations_good.log'
bad = 'registrations_bad.log'

with open(path, 'r', encoding='utf8') as file:
    with open(good, 'w', encoding='utf8') as f_good:
        with open(bad, 'w', encoding='utf8') as f_bad:
            for line in file:
                try:
                    check_error = ErrorChecking(line=line[:-1])
                    f_good.write(line)
                except ValueError as exc:
                    if 'unpack' in exc.args[0]:
                        message = f'Не хватает операндов {exc} в строке | {line}'
                        print(message)
                        f_bad.write(message)
                    else:
                        message = f'поле возраст НЕ является числом от 10 до 99 в строке | {line}'
                        print(message)
                        f_bad.write(message)
                except NotNameError as exc:
                    message = f'поле имени содержит НЕ только буквы в строке | {line}'
                    print(message)
                    f_bad.write(message)
                except NotEmailError as exc:
                    message = f'поле содержит НЕ email в строке | {line}'
                    print(message)
                    f_bad.write(message)



