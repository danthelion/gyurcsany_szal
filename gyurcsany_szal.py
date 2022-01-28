"""😈"""

__version__ = "0.1"

import threading


def ferenc():
    print('Gyurcsány')


x = threading.Thread(target=ferenc)
x.start()
x.join()
