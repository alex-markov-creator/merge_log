#-*- coding: utf-8 -*-
"""
log_merge.py - merged log files: log_a.jsonl and log_b.jsonl
author: a.bezzubov

Имеется два файла с логами в формате JSONL, пример лога:
…
{"timestamp": "2021-02-26 08:59:20", "log_level": "INFO", "message": "Hello"}
{"timestamp": "2021-02-26 09:01:14", "log_level": "INFO", "message": "Crazy"}
{"timestamp": "2021-02-26 09:03:36", "log_level": "INFO", "message": "World!"}
…

Сообщения в заданных файлах упорядочены по полю timestamp в порядке возрастания.

Требуется написать скрипт, который объединит эти два файла в один.
При этом сообщения в получившемся файле тоже должны быть упорядочены в порядке возрастания по полю timestamp.

К заданию прилагается вспомогательный скрипт на python3, который создает два файла "log_a.jsonl" и "log_b.jsonl".

Командлайн для запуска:
log_generator.py <path/to/dir>

* Базовая задача
Ваше приложение должно поддерживать следующий командлайн:
<your_script>.py <path/to/log1> <path/to/log2> -o <path/to/merged/log>

* Задачка повышенной сложности (вместо работы с аргументами командной строки)
Необходимо реализовать графический интерфейс пользователя, который включает следующие элементы:
    1. кнопка выбора первого *.jsonl-файла
    2. текстовое поле для отображения полного пути к первому выбранному *.jsonl-файлу
    3. кнопка выбора второго *.jsonl-файла
    4. текстовое поле для отображения полного пути к второму выбранному *.jsonl-файлу
    5. кнопка «Запуск», которая осуществляет запуск процесса обработки *.jsonl-файлов
Графический интерфейс необходимо реализовать с использованием библиотеки PySide2 (либо PySide6).
"""
import os
import sys
import time
import dataclasses
import argparse

_LOG_FILENAMES = 'log_a.jsonl', 'log_b.jsonl'
_LOG_MERGEDNAMES = 'log_merge.jsonl'

#ДЕКОРАТОР ХРОНОМЕТРАЖА
def time_of_function(function):
    """
    #ДЕКОРАТОР  ВРЕМЕНИ ВЫПОЛНЕНИЯ
    """
    def wrapped(*args):
        start_time = time.perf_counter()
        start_time_ns = time.perf_counter_ns()
        res = function(*args)
        print(f'Время выполнения в секундах: {time.perf_counter() - start_time}')
        print(f'Время выполнения в наносекундах: {time.perf_counter_ns() - start_time_ns}')
        return res
    return wrapped

@dataclasses.dataclass
class ParseArgs(object):
    """Commandline class"""
    def __init__(self, _LOG_FILENAMES:tuple):
        self._LOG_FILENAMES = _LOG_FILENAMES
    #@time_of_function
    def _parse_args(self) -> argparse.Namespace:
        parser = argparse.ArgumentParser(description='Tool to generate test logs.')

        parser.add_argument(
            'input_dir_1',
            metavar='<INPUT DIR1>',
            type=str,
            help=f'path to dir with generated logs {_LOG_FILENAMES[0]}',
        )

        parser.add_argument(
            'input_dir_2',
            metavar='<INPUT DIR2>',
            type=str,
            help=f'path to dir with generated logs {_LOG_FILENAMES[1]}',
        )

        parser.add_argument(
            '-o',
            '--out',
            metavar='<OUTPUT DIR>',
            type=str,
            help=f'path to dir with output file {_LOG_MERGEDNAMES}',
        )

        return parser.parse_args()

@dataclasses.dataclass
class CreateDir(object):
    """File save directory class """
    def __init__(self, output_dir):
        pass

    def func(self):
        pass

    def func(self):
        pass

@dataclasses.dataclass
class MergeLogFiles(object):
    """A class for merging files with names in the _LOG_FILENAMES variable into one file with a name in the _LOG_MERGENAMES variable
    """
    def __init__(self, _LOG_MERGEDNAMES: str):
        pass

    def func(self):
        pass

    def func(self):
        pass

if __name__ == '__main__':
    a = ParseArgs(_LOG_FILENAMES)
    args = a._parse_args()
    if len(sys.argv)==5:
        args_out = sys.argv[-1]
    else:
        args_out = os.getcwd()
    #print(args.input_dir_1, args.input_dir_2, args_out)







