import threading


def ferenc():
    print('Gyurcsány')


if __name__ == "__main__":
    x = threading.Thread(target=ferenc)
    x.start()
    x.join()
