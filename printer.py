import sys


def print(text):
    sys.stdout.write('\r                                                         ')
    sys.stdout.write('\r' + text)
    sys.stdout.flush()
    sys.stdout.write('\r')
    sys.stdout.flush()
