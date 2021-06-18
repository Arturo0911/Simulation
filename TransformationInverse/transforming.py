#!/usr/bin/python3
# encoding: utf-8

import random
from typing import (
    Tuple
)

BANNER = """
    '########:'########:::::'###::::'##::: ##::'######::'########::'#######::'########::'##::::'##:'####:'##::: ##::'######:::
    ::: ##:::: ##:::: ##::'##:. ##:: ####: ##: ##:::..:: ##::::::: ##:::: ##: ##:::: ##: ####'####:: ##:: ####: ##: ##:::..:::
    ... ##..:: ##.... ##:::'## ##::: ###:: ##:'##... ##: ##.....::'##.... ##: ##.... ##: ###::'###:. ##:: ###:: ##:'##... ##::
    ::: ##:::: ########::'##:::. ##: ## ## ##:. ######:: ######::: ##:::: ##: ########:: ## ### ##:: ##:: ## ## ##: ##::'####:
    ::: ##:::: ##.. ##::: #########: ##. ####::..... ##: ##...:::: ##:::: ##: ##.. ##::: ##. #: ##:: ##:: ##. ####: ##::: ##::
    ::: ##:::: ##::. ##:: ##.... ##: ##:. ###:'##::: ##: ##::::::: ##:::: ##: ##::. ##:: ##:.:: ##:: ##:: ##:. ###: ##::: ##::
    ::: ##:::: ##:::. ##: ##:::: ##: ##::. ##:. ######:: ##:::::::. #######:: ##:::. ##: ##:::: ##:'####: ##::. ##:. ######:::
    :::..:::::..:::::..::..:::::..::..::::..:::......:::..:::::::::.......:::..:::::..::..:::::..::....::..::::..:::......::::
    
    '####:'##::: ##:'##::::'##:'########:'########:::'######::'########:
    . ##:: ###:: ##: ##:::: ##: ##.....:: ##.... ##:'##... ##: ##.....::
    : ##:: ####: ##: ##:::: ##: ##::::::: ##:::: ##: ##:::..:: ##:::::::
    : ##:: ## ## ##: ##:::: ##: ######::: ########::. ######:: ######:::
    : ##:: ##. ####:. ##:: ##:: ##...:::: ##.. ##::::..... ##: ##...::::
    : ##:: ##:. ###::. ## ##::: ##::::::: ##::. ##::'##::: ##: ##:::::::
    '####: ##::. ##:::. ###:::: ########: ##:::. ##:. ######:: ########:
    ....::..::::..:::::...:::::........::..:::::..:::......:::........::
    
    [*] author: Arturo Negreiros (Payl0xd) 
    [*] version 1.1.2
    [*] follow: https://twitter.com/DevTuron
    [*] you can find this source code in https://github.com/Arturo0911/Simulation/tree/master/TransformationInverse
    [*] Never stop learning <3
"""


def default_values() -> Tuple[list, list]:
    p_function = [1 / 8, 4 / 8, 2 / 8, 1 / 8]
    x_function = [-5, 1, 2, 3]
    return x_function, p_function


def implement(func_values: list, func_probability: list, aleatory_number: float) -> int:
    """
    :param aleatory_number: number generated by random.uniform(0,1)
    :param func_values: the values of the variable that its, the property value
    :param func_probability: probability values
    :return: which element correspond the called function
    :TODO:
        - You should to input the probability function Xi and Pi
            and input the numbers of values that you want to generate
    """

    counter = 1
    func = func_probability[0]
    x_sample = 0

    for i in range(0, len(func_values)):
        if aleatory_number < func:
            x_sample = func_values[counter - 1]
            break
        else:
            counter += 1
            func += func_probability[counter - 1]

    return x_sample


def random_seed(number=5) -> list:
    return [random.uniform(0, 1) for _ in range(number)]


class TransformationInverse:

    def __init__(self) -> None:
        print(BANNER)
        self.x_values = None
        self.p_values = None
        # self.random_num = random.uniform(0, 1)

    def cmd(self) -> None:
        print("User:~$ En cualquier momento puedes presionar 'ENTER' y salir del programa")
        while True:
            print(
                "User:~$ presiona (d o default) para elegir valores de x y p estándares, si quieres ingresar tus propios valores presiona (p o personalizado)")

            preference = input("User:~$ ")
            preference = preference.lower()
            if preference == "d" or preference == "DEFAULT":
                self.x_values, self.p_values = default_values()
                print(self.x_values)
                print(self.p_values)
            elif preference == "":
                break
            else:
                print("User:~$ Ingresa los valores de X: ")
                self.x_values = list(map(int, input().split(" ")))
                print("User:~$ Ingresa los valores probabilísticos de p: ")
                self.p_values = list(map(float, input().split(" ")))
            print(self.x_values)
            print(self.p_values)
            print("User:~$ obtener valores (r o random) para la simulacion o elegir los (p o predeterminados) ")
            seed = input("User:~$ ")
            seed = seed.lower()
            if seed == "":
                break
            elif seed == "r" or seed == "random":
                seed_values = random_seed()
            else:
                seed_values = list(map(float, input("User:~$ ").split(" ")))

            print(seed_values)
        print("     [*] Saiendo...")


if __name__ == '__main__':
    # stack_test = [0.91, 0.41, 0.33, 0.59, 0.14]
    transformation = TransformationInverse()
    # transformation.CLI()
    # for x in stack_test:
    #    print(transformation.implement(x_function, z_function, x))

    # Implementing an interactive shell
    transformation.cmd()