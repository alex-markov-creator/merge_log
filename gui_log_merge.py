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

* Задачка повышенной сложности (вместо работы с аргументами командной строки)
Необходимо реализовать графический интерфейс пользователя, который включает следующие элементы:
    1. кнопка выбора первого *.jsonl-файла
    2. текстовое поле для отображения полного пути к первому выбранному *.jsonl-файлу
    3. кнопка выбора второго *.jsonl-файла
    4. текстовое поле для отображения полного пути к второму выбранному *.jsonl-файлу
    5. кнопка «Запуск», которая осуществляет запуск процесса обработки *.jsonl-файлов
Графический интерфейс необходимо реализовать с использованием библиотеки PySide2 (либо PySide6).
"""
import re
from dateutil.parser import parse
import PySide2
from PySide2 import QtCore, QtWidgets, QtGui
print(PySide2.__version__)
print(QtCore.__version__)

class MyWindow(QtWidgets.QWidget):
    # Определение класса
    def __init__(self, parent=None):
        # Определяет конструктор класса
        QtWidgets.QWidget.__init__(self, parent)
        # Вызывается конструктор базового класса, и ему передается ссылка на родительский компонент.
        self.btnFile_a = QtWidgets.QPushButton("&Первый файл лога")
        self.btnFile_b = QtWidgets.QPushButton("&Второй файл лога")
        self.text = QtWidgets.QTextEdit()
        self.btnRun = QtWidgets.QPushButton("&Запуск")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.btnFile_a)
        self.vbox.addWidget(self.btnFile_b)
        self.vbox.addWidget(self.text)
        self.vbox.addWidget(self.btnRun)
        self.setLayout(self.vbox)
        self.btnFile_a.clicked.connect(self.path_file_a)# Обработчик сигнала
        self.btnFile_b.clicked.connect(self.path_file_b)# Обработчик сигнала
        self.btnRun.clicked.connect(self.run)# Обработчик сигнала

    @QtCore.Slot()
    def run(self):
        self.file_a = ''.join(self.infile_a)
        self.file_b = ''.join(self.infile_b)
        self.file_out = 'gui_log_c.jsonl'
        for infile in self.file_a,self.file_b:
            with open(infile, 'r') as file:
                with open(self.file_out, 'a+') as write_file:
                    for line in file:
                        write_file.write(line)
        with open(self.file_out, 'a+') as f_in:
            print(*sorted(f_in.readlines(), key=lambda x: parse(re.search(r'(?<=")\d[-:\d ]+', x).group())))
        self.text.setText('gui_log_c.jsonl')

    @QtCore.Slot()
    def path_file_a(self):
        dialog = QtWidgets.QFileDialog(parent=window,
                               filter="Logs (*.jsonl)",
                               caption="Путь к файл")
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        dialog.setDirectory(QtCore.QDir.currentPath())

        result = dialog.exec()
        if result == QtWidgets.QDialog.Accepted:
            self.infile_a = dialog.selectedFiles()
            self.text.setText(''.join(self.infile_a))
            return self.infile_a
        else:
            print("Нажата кнопка Cancel")

    @QtCore.Slot()
    def path_file_b(self):
        dialog = QtWidgets.QFileDialog(parent=window,
                               filter="Logs (*.jsonl)",
                               caption="Путь к файл")
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        dialog.setDirectory(QtCore.QDir.currentPath())

        result = dialog.exec()
        if result == QtWidgets.QDialog.Accepted:
            self.infile_b = dialog.selectedFiles()
            self.text.setText(''.join(self.infile_b))
            return self.infile_b
        else:
            print("Нажата кнопка Cancel")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()   # Создаем экземпляр класса
    window.setWindowTitle("Логи в один файл")
    window.resize(300, 70)
    window.show()         # Отображаем окно
    sys.exit(app.exec_()) # Запускаем цикл обработки событий