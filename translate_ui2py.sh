#! /bin/bash
# Translates the ui files to python code. The ui files are edited in QtCreator's designer mode.

pyuic5 -o ui_main_window.py main_window.ui
