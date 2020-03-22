#!/usr/bin/env python3

"""Первичная подготовка html-файлов для Молитвослова"""
import os


def scan_directory(scan_dir, scan_ext):
    """Получение списка файлов из нужного каталога"""
    found_files = []
    for root, dirs, files in os.walk(scan_dir):
        for name in files:
            if name.endswith(scan_ext):
                os.path.join(root, name)
                found_files.append(os.path.join(root, name))
    return found_files


def modify_file(file):
    """Модификация html-файла для использования в Молитвослове"""
    color1 = "009933"
    color2 = "009999"
    color3 = "e8aa00"
    my_dict = {"Слава Тебе,": color1, "Слава Твоей": color1, "И ныне": color2,
               "Радуйся": color3, "Радуйтесь": color3,
               "Ра́дуйтесь": color3, "Сын Божий": color1,
               "Помилуй меня,": color1, "Господи, Помилуй": color1,
               "Иисусе": color1, "Иисусе Боже": color1, "Христе": color1,
               "Бога Отца": color1,
               "Слава": color1}
    try:
        with open(file, 'r+', encoding='cp1251') as file_handler:
            lines = file_handler.read()
            for wd in my_dict.keys():
                # print(wd, my_dict[wd])
                lines = lines.replace(wd, '<font color="' + my_dict[wd] + '">' + wd + '</font>')
            file_handler.seek(0)
            file_handler.write(lines)
            file_handler.truncate()
            print("Обработан файл:", file)
    except Exception as e:
        print(e)
        print("Ошибка при обработке файла:", file)


def run():
    current_dir = os.path.abspath(os.curdir)
    html_directory = os.path.join(current_dir, 'HTML')

    htm_files = scan_directory(html_directory, (".htm"))

    print("Найдено файлов для обработки:", len(htm_files))
    for file in htm_files:
        modify_file(file)


if __name__ == '__main__':
    run()
