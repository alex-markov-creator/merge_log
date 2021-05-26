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
import log_merge
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
        self.btnQuit = QtWidgets.QPushButton("&Запуск")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.btnQuit.clicked.connect(self.run)# Обработчик сигнала

    @QtCore.Slot()
    def run(self):
        print('hi!')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()   # Создаем экземпляр класса
    window.setWindowTitle("ООП-стиль создания окна")
    window.resize(300, 70)
    window.show()         # Отображаем окно
    sys.exit(app.exec_()) # Запускаем цикл обработки событий