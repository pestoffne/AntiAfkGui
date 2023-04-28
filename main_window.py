#! /usr/bin/env python3
from time import sleep
import sys
from datetime import timedelta
from os import system

from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui_main_window import Ui_MainWindow
from parser import text_to_ms
from background_listener import BackgroundListener


class MainWindow(QMainWindow):
    ui = Ui_MainWindow()
    state = 'idle'
    time_down = 50
    key_spam = '0'
    key_start_stop = None

    def __init__(self):
        super().__init__()
        self.ui.setupUi(self)
        self.ui.button_start_stop.clicked.connect(self.on_start_or_stop_clicked)
        self.update_button_start_stop('idle')
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer_timeout)
        self.ui.le_key_start_stop.textChanged.connect(self.on_le_key_start_stop_text_changed)
        self.background_listener = BackgroundListener()
        self.background_listener.key_stop_clicked.connect(self.on_start_or_stop_clicked)
        self.background_listener.start()

    def start(self):
        self.update_button_start_stop('run')
        self.ui.le_key_spam.setEnabled(False)
        self.ui.le_period.setEnabled(False)
        self.ui.le_down_time.setEnabled(False)
        self.ui.le_key_start_stop.setEnabled(False)
        try:
            period = text_to_ms(self.ui.le_period.text()) // timedelta(milliseconds=1)
            self.time_down = text_to_ms(self.ui.le_down_time.text()) / timedelta(seconds=1)
            self.key_spam = self.ui.le_key_spam.text()
            self.timer.start(period)
        except IndexError:
            self.stop()

    def stop(self):
        self.update_button_start_stop('idle')
        self.ui.le_key_spam.setEnabled(True)
        self.ui.le_period.setEnabled(True)
        self.ui.le_down_time.setEnabled(True)
        self.ui.le_key_start_stop.setEnabled(True)
        self.timer.stop()

    def update_button_start_stop(self, state):
        self.state = state
        keyss = self.key_start_stop
        self.ui.button_start_stop.setText(
            ('Старт' if state == 'idle' else 'Стоп') +
            ('' if keyss is None or len(keyss) == 0 else ' (\"' + keyss + '\")'))
        self.ui.button_start_stop.setStyleSheet(
            'background-color: green' if state == 'idle' else 'background-color: red')

    @pyqtSlot()
    def on_start_or_stop_clicked(self):
        if self.state == 'idle':
            self.start()
        else:
            self.stop()

    @pyqtSlot()
    def on_timer_timeout(self):
        system('xte "keydown {}" "usleep {}" "keyup {}"'.format(
            self.key_spam, int(self.time_down * 1_000_000), self.key_spam))

    @pyqtSlot()
    def on_le_key_start_stop_text_changed(self):
        self.key_start_stop = self.ui.le_key_start_stop.text()
        self.background_listener.set_key_stop(self.key_start_stop)
        self.update_button_start_stop(self.state)


if __name__ == '__main__':
    a = QApplication(sys.argv)
    b = MainWindow()
    b.show()
    a.exec_()
