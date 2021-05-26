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
from pathlib import Path
import shutil
import json
import re
from dateutil.parser import parse

def time_of_function(function):
    """
    time decorator
    """
    def wrapped(*args):
        start_time = time.perf_counter()
        start_time_ns = time.perf_counter_ns()
        res = function(*args)
        print(f'seconds: {time.perf_counter() - start_time}')
        print(f'nsseconds: {time.perf_counter_ns() - start_time_ns}')
        return res
    return wrapped

@dataclasses.dataclass
class ParseArgs(object):
    """Commandline class"""
    def __init__(self):
        parser = argparse.ArgumentParser(description='Tool to generate test logs.')
        parser.add_argument(
            'input_dir_1',
            metavar='<INPUT DIR1>',
            type=str,
            help=f'path to dir with generated logs_a',
        )
        parser.add_argument(
            'input_dir_2',
            metavar='<INPUT DIR2>',
            type=str,
            help=f'path to dir with generated logs_b',
        )
        parser.add_argument(
            '-o',
            '--out',
            metavar='<OUTPUT DIR>',
            type=str,
            default=os.getcwd(),
            help=f'path to dir with output file',
        )
        parser.add_argument(
            '-f', '--force',
            action='store_const',
            const=True,
            default=False,
            help='force write log',
            dest='force_write',
        )
        self.args = parser.parse_args()

    def parse_dir(self) -> list:
        """
        directory return function
        a = ParseArgs()
        a.parse_dir()[0] - path dir file_a
        a.parse_dir()[1] - path dir file_b
        a.parse_dir()[2] - path dir file_out
        """
        return [os.path.dirname(self.args.input_dir_1), os.path.dirname(self.args.input_dir_2), os.path.dirname(self.args.out)]

    def parse_filename(self) -> list:
        """
        filenames return function
        a = ParseArgs()
        a.parse_filename()[0] - filename file_a
        a.parse_filename()[1] - filename file_b
        """
        return [os.path.basename(self.args.input_dir_1), os.path.basename(self.args.input_dir_2)]

@dataclasses.dataclass
class CreateDir(object):
    """
    File-out directory class
    dir_path = Path(a.parse_dir()[-1])
    b = CreateDir(dir_path, force_write=args.force_write)
    """
    def __init__(self, dir_path: Path, *, force_write: bool = False) -> None:
        """
        initialization function
        """
        if dir_path.exists():
            if not force_write:
                raise FileExistsError(
                    f'Dir "{dir_path}" already exists. Remove it first or choose another one.')
            shutil.rmtree(dir_path)
        dir_path.mkdir(parents=True)

@dataclasses.dataclass
class MergeLogFiles(object):
    """A class for merging files"""
    def __init__(self):
        """
        initialization function
        """
        a = ParseArgs()
        self.args = a.args
        self.file_a = args.input_dir_1
        self.file_b = args.input_dir_2
        self.file_out = args.out

    @time_of_function
    def jsonl_file(self):
        """
        function of reading, combining and sorting files
        """
        for infile in self.file_a,self.file_b:
            with open(infile, 'r') as file:
                with open(self.file_out, 'a+') as write_file:
                    for line in file:
                        write_file.write(line)
        with open(self.file_out, 'a+') as f_in:
            print(*sorted(f_in.readlines(), key=lambda x: parse(re.search(r'(?<=")\d[-:\d ]+', x).group())))

if __name__ == '__main__':
    # Arguments
    a = ParseArgs()
    args = a.args
    # Create dir
    dir_path = Path(a.parse_dir()[-1])
    b = CreateDir(dir_path, force_write=args.force_write)
    # Merge logs
    c = MergeLogFiles()
    c.jsonl_file()







