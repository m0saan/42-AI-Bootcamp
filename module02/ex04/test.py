from ai42.logger import log
from time import sleep


@log
def f():
    print("Hello")
    sleep(1)

f()