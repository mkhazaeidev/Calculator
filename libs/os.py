from os import system
from sys import platform


def set_clear():
    if platform == "linux" or platform == "linux2":
        return lambda: system("clear")
    elif platform == "darwin":
        return lambda: system("clear")
    elif platform == "win32":
        return lambda: system("cls")


clear = set_clear()
