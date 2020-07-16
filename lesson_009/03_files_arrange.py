# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname        возвращает имя директории пути path
#   os.path.join           соединяет пути
#   os.path.normpath       нормализует путь, убирая избыточные разделители
#   os.path.getmtime       время последнего изменения файла, в секундах
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

dir_in = 'icons'
dir_out = 'icons_by_year'


# def _time_file(list_file):
#     for file_name in list_file:
#         path = os.path.join(dirpath, file_name)
#         time_file = time.gmtime(os.path.getmtime(path))
#         return time_file


for dirpath, dirnames, filenames in os.walk(dir_in):
    print(dirpath, dirnames, filenames)
    for file_name in filenames:
        path = os.path.join(dirpath, file_name)
        time_file = time.gmtime(os.path.getmtime(path))
        path = os.path.join(dir_out, str(time_file[0]), str(time_file[1]), str(time_file[2]))
        os.makedirs(path)
        shutil.copy2(os.path.join(dirpath, file_name), path)


# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
