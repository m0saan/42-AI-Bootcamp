import time
from random import randint
import logging
import os


class log:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()  # start time
        call = self.func(*args, **kwargs)  # call func
        func_name = self.func.__name__  # func name
        end = time.time()  # end time
        message = "(cmaxime)Running: {}    [ exec-time = {} ms ]\n".format(func_name, (end - start))

        cwd = os.getcwd()
        with open(f"{cwd}/machine.log", "a") as f:
            f.write(message)

        return call



class CoffeeMachine:
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine(self):
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water(self))
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


@log
def f(name):
    print("Hello {}".format(name))


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee(machine)
    machine.make_coffee(machine)
    machine.add_water(machine, 70)


