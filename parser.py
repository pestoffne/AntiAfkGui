from datetime import timedelta
import re


def split_literal(text):
    num_list = re.findall('^[0-9.]+', text)
    return 1 if len(num_list) == 0 else float(num_list[0]), re.findall('[a-zA-Z]+$', text)[0]


def text_to_ms(text):
    value, literal = split_literal(text)

    if literal == 'ms':
        delta = timedelta(milliseconds=value)
    elif literal == 's':
        delta = timedelta(seconds=value)
    elif literal == 'm':
        delta = timedelta(minutes=value)
    elif literal == 'h':
        delta = timedelta(hours=value)
    else:
        delta = timedelta(milliseconds=value)

    return delta
