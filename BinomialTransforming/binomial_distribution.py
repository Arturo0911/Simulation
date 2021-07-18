#!/usr/bin/python3


from pprint import pprint

from math import *
from random import *
from warnings import simplefilter

BANNER = """
                ____  _      __       _ __               _
               / __ \(_)____/ /______(_) /_  __  _______(_)___  _____
              / / / / / ___/ __/ ___/ / __ \/ / / / ___/ / __ \/ __  |
             / /_/ / (__  ) /_/ /  / / /_/ / /_/ / /__/ / /_/ / / / /
            /_____/_/____/\__/_/  /_/_.___/\__,_/\___/_/\____/_/ /_/

            BBBBBBBBBBBBBBBBB     iiii                                                              iiii                    lllllll
            B::::::::::::::::B   i::::i                                                            i::::i                   l:::::l
            B::::::BBBBBB:::::B   iiii                                                              iiii                    l:::::l
            BB:::::B     B:::::B                                                                                            l:::::l
              B::::B     B:::::Biiiiiiinnnn  nnnnnnnn       ooooooooooo      mmmmmmm    mmmmmmm   iiiiiii   aaaaaaaaaaaaa    l::::l
              B::::B     B:::::Bi:::::in:::nn::::::::nn   oo:::::::::::oo  mm:::::::m  m:::::::mm i:::::i   a::::::::::::a   l::::l
              B::::BBBBBB:::::B  i::::in::::::::::::::nn o:::::::::::::::om::::::::::mm::::::::::m i::::i   aaaaaaaaa:::::a  l::::l
              B:::::::::::::BB   i::::inn:::::::::::::::no:::::ooooo:::::om::::::::::::::::::::::m i::::i            a::::a  l::::l
              B::::BBBBBB:::::B  i::::i  n:::::nnnn:::::no::::o     o::::om:::::mmm::::::mmm:::::m i::::i     aaaaaaa:::::a  l::::l
              B::::B     B:::::B i::::i  n::::n    n::::no::::o     o::::om::::m   m::::m   m::::m i::::i   aa::::::::::::a  l::::l
              B::::B     B:::::B i::::i  n::::n    n::::no::::o     o::::om::::m   m::::m   m::::m i::::i  a::::aaaa::::::a  l::::l
              B::::B     B:::::B i::::i  n::::n    n::::no::::o     o::::om::::m   m::::m   m::::m i::::i a::::a    a:::::a  l::::l
            BB:::::BBBBBB::::::Bi::::::i n::::n    n::::no:::::ooooo:::::om::::m   m::::m   m::::mi::::::ia::::a    a:::::a l::::::l
            B:::::::::::::::::B i::::::i n::::n    n::::no:::::::::::::::om::::m   m::::m   m::::mi::::::ia:::::aaaa::::::a l::::::l
            B::::::::::::::::B  i::::::i n::::n    n::::n oo:::::::::::oo m::::m   m::::m   m::::mi::::::i a::::::::::aa:::al::::::l
            BBBBBBBBBBBBBBBBB   iiiiiiii nnnnnn    nnnnnn   ooooooooooo   mmmmmm   mmmmmm   mmmmmmiiiiiiii  aaaaaaaaaa  aaaallllllll

            Owner: Arturo Negreiros Samanez
            version: 1.0.0
            date: 25/06/2021
"""
print(BANNER)
class Binomial:

    def __init__(self, uniform_values: int) -> None:
        self.rand_values = [uniform(0,1) for _ in range(uniform_values)]

    def create_binomial_elements(self, success_value: float, number_test: int) -> list:

        stack = list()
        p_value = pow((1 - success_value),number_test)
        f_value = p_value
        stack.append(p_value)
        for x in range(0, number_test):
            p_value = (((number_test-x)/(x + 1)) * ((success_value)/( 1 -success_value)) * (p_value))
            f_value += p_value
            stack.append("{0:.7f}".format(f_value))

        return stack

    def _init_process(self,n_number: int, success: float, u_test_case:float) -> int:
        """
        :param n_number
        :param success
        :param u_test_case
        """
        counter = 0
        prob_value = pow(float(1 -success), n_number)
        f_val = prob_value
        stack = list()
        stack.append(prob_value)
        while True:

            if u_test_case < f_val:
                break
            else:
                prob_value = ((float(n_number -  counter) / float(counter + 1)) * ((success)/(1-success)))*prob_value
                f_val += prob_value
                counter += 1
                stack.append(f_val)

        return counter
    def calculating_number_success(self, number:int, success:float) -> list:

        print("[*] Número de elementos de probabilidades son: \n")
        print("======================================")
        print(self.create_binomial_elements(success, number))
        print("======================================")
        print("\n")
        print("======================================")
        print("[*] El número de simulaciones es: \n")
        pprint(self.rand_values)
        print("======================================")
        print("\n\n")
        return ["[*] Éxito en la posicion: {} para el uniforme: {}".format(str(self._init_process(number, success, i)), i) for i in self.rand_values]


def main():

    try:
        uniform_values = int(input("[*] Ingrese el número de elementos simulaciones: "))
        binomial = Binomial(uniform_values)
        # pprint(binomial.rand_values)
        x_success = float(input("[*] Ingrese la probabilidad del éxito: "))
        n_number = int(input("[*] Ingrese el número de pruebas a realizar: "))
        pprint(binomial.calculating_number_success(n_number, x_success))
    except ValueError as e:
        raise ValueError("The value cannot be processed")
    except KeyboardInterrupt:
        print("\n[*] Saliendo...")


if __name__ == "__main__":
    main()


