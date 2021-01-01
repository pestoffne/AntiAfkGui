#! /usr/bin/python3
from time import sleep
import sys
from pynput.keyboard import Controller
from datetime import timedelta

from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow

from foo import Ui_MainWindow
from parser import text_to_ms


class MainWindow(QMainWindow, Ui_MainWindow):
    state = 'init'
    time_down = 50
    key = '0'

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_start_stop.clicked.connect(self.start_or_stop_clicked)
        self.button_start_stop.setText('Старт')
        self.button_start_stop.setStyleSheet("background-color: green")
        self.state = 'idle'
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer_timeout)
        self.keyboard = Controller()

    def start(self):
        self.button_start_stop.setText('Стоп')
        self.button_start_stop.setStyleSheet("background-color: red")
        self.state = 'run'
        try:
            period = text_to_ms(self.le_period.text()) // timedelta(milliseconds=1)
            self.time_down = text_to_ms(self.le_down_time.text()) / timedelta(seconds=1)
            self.key = self.le_key.text()
            self.timer.start(period)
        except IndexError:
            self.stop()

    def stop(self):
        self.button_start_stop.setText('Старт')
        self.button_start_stop.setStyleSheet("background-color: green")
        self.state = 'idle'
        self.timer.stop()

    @pyqtSlot()
    def start_or_stop_clicked(self):
        if self.state == 'idle':
            self.start()
        else:
            self.stop()

    @pyqtSlot()
    def on_timer_timeout(self):
        try:
            self.keyboard.press(self.key)
            sleep(self.time_down)
            self.keyboard.release(self.key)
        except ValueError:
            self.stop()


if __name__ == '__main__':
    a = QApplication(sys.argv)
    b = MainWindow()
    b.show()
    a.exec_()
