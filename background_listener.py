from PyQt5.QtCore import QObject, pyqtSignal
from pynput.keyboard import Listener, Key


class BackgroundListener(QObject):

    key_stop_clicked = pyqtSignal()
    key_stop = None
    state = 0

    def on_press(self, key):
        try:
            key_char = key.char
        except AttributeError:
            return

        if key_char == self.key_stop:
            if self.state == 0:
                self.state = 1

    def on_release(self, key):
        try:
            key_char = key.char
        except AttributeError:
            return

        if key_char == self.key_stop:
            if self.state == 1:
                self.state = 2
                self.key_stop_clicked.emit()
                self.state = 0

    def set_key_stop(self, key_stop):
        self.key_stop = key_stop
        self.state = 0

    def start(self):
        listener = Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()

    def stop(self):
        listener.stop()

