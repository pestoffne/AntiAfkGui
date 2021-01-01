#! /usr/bin/python3
from time import sleep
import sys
from pynput.keyboard import Controller
from datetime import timedelta

from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow

from foo import Ui_MainWindow
from parser import text_to_ms
from background_listener import BackgroundListener


class MainWindow(QMainWindow, Ui_MainWindow):
    state = 'idle'
    time_down = 50
    key_spam = '0'
    key_start_stop = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_start_stop.clicked.connect(self.on_start_or_stop_clicked)
        self.update_button_start_stop('idle')
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer_timeout)
        self.le_key_start_stop.textChanged.connect(self.on_le_key_start_stop_text_changed)
        self.keyboard = Controller()
        self.background_listener = BackgroundListener()
        self.background_listener.key_stop_clicked.connect(self.on_start_or_stop_clicked)
        self.background_listener.start()

    def start(self):
        self.update_button_start_stop('run')
        self.le_key_spam.setEnabled(False)
        self.le_period.setEnabled(False)
        self.le_down_time.setEnabled(False)
        self.le_key_start_stop.setEnabled(False)
        try:
            period = text_to_ms(self.le_period.text()) // timedelta(milliseconds=1)
            self.time_down = text_to_ms(self.le_down_time.text()) / timedelta(seconds=1)
            self.key_spam = self.le_key_spam.text()
            self.timer.start(period)
        except IndexError:
            self.stop()

    def stop(self):
        self.update_button_start_stop('idle')
        self.le_key_spam.setEnabled(True)
        self.le_period.setEnabled(True)
        self.le_down_time.setEnabled(True)
        self.le_key_start_stop.setEnabled(True)
        self.timer.stop()

    def update_button_start_stop(self, state):
        self.state = state
        keyss = self.key_start_stop
        self.button_start_stop.setText(
            ('Старт' if state == 'idle' else 'Стоп') +
            ('' if keyss is None or len(keyss) == 0 else ' (\"' + keyss + '\")'))
        self.button_start_stop.setStyleSheet(
            'background-color: green' if state == 'idle' else 'background-color: red')

    @pyqtSlot()
    def on_start_or_stop_clicked(self):
        if self.state == 'idle':
            self.start()
        else:
            self.stop()

    @pyqtSlot()
    def on_timer_timeout(self):
        try:
            self.keyboard.press(self.key_spam)
            sleep(self.time_down)
            self.keyboard.release(self.key_spam)
        except ValueError:
            self.stop()

    @pyqtSlot()
    def on_le_key_start_stop_text_changed(self):
        self.key_start_stop = self.le_key_start_stop.text()
        self.background_listener.set_key_stop(self.key_start_stop)
        self.update_button_start_stop(self.state)


if __name__ == '__main__':
    a = QApplication(sys.argv)
    b = MainWindow()
    b.show()
    a.exec_()
