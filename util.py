import random

from PyQt5.QtCore import QObject, pyqtSignal


class Signal(QObject):
    moved_on = pyqtSignal()
    plot_last_time = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)


def shuffle(data: list):
    N = len(data)
    k = N
    while k > 0:
        i = random.randint(0, N - 1)
        j = random.randint(0, N - 1)
        data[i], data[j] = data[j], data[i]
        k -= 1
    return data
