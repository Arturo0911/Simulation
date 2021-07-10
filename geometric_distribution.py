#!/usr/bin/python3

from random import uniform
from math import pow
from pprint import pprint

print("""
    '########::'####::'######::'########:'########::'####:'########::'##::::'##::'######::'####:'##::: ##:
     ##.... ##:. ##::'##... ##:... ##..:: ##.... ##:. ##:: ##.... ##: ##:::: ##:'##... ##:. ##:: ###:: ##:
     ##:::: ##:: ##:: ##:::..::::: ##:::: ##:::: ##:: ##:: ##:::: ##: ##:::: ##: ##:::..::: ##:: ####: ##:
     ##:::: ##:: ##::. ######::::: ##:::: ########::: ##:: ########:: ##:::: ##: ##:::::::: ##:: ## ## ##:
     ##:::: ##:: ##:::..... ##:::: ##:::: ##.. ##:::: ##:: ##.... ##: ##:::: ##: ##:::::::: ##:: ##. ####:
     ##:::: ##:: ##::'##::: ##:::: ##:::: ##::. ##::: ##:: ##:::: ##: ##:::: ##: ##::: ##:: ##:: ##:. ###:
     ########::'####:. ######::::: ##:::: ##:::. ##:'####: ########::. #######::. ######::'####: ##::. ##:
     ........:::....:::......::::::..:::::..:::::..::....::........::::.......::::......:::....::..::::..::


     :'######:::'########::'#######::'##::::'##:'########:'########:'########::'####::'######:::::'###::::
    '##... ##:: ##.....::'##.... ##: ###::'###: ##.....::... ##..:: ##.... ##:. ##::'##... ##:::'## ##:::
     ##:::..::: ##::::::: ##:::: ##: ####'####: ##:::::::::: ##:::: ##:::: ##:: ##:: ##:::..:::'##:. ##::
     ##::'####: ######::: ##:::: ##: ## ### ##: ######:::::: ##:::: ########::: ##:: ##:::::::'##:::. ##:
     ##::: ##:: ##...:::: ##:::: ##: ##. #: ##: ##...::::::: ##:::: ##.. ##:::: ##:: ##::::::: #########:
     ##::: ##:: ##::::::: ##:::: ##: ##:.:: ##: ##:::::::::: ##:::: ##::. ##::: ##:: ##::: ##: ##.... ##:
    . ######::: ########:. #######:: ##:::: ##: ########:::: ##:::: ##:::. ##:'####:. ######:: ##:::: ##:
    :......::::........:::.......:::..:::::..::........:::::..:::::..:::::..::....:::......:::..:::::..:


                [...]           Owner: Arturo Negreiros Samanez                             [...]
                [...]           date:  09/07/2021                                           [...]
                [...]           follow me: https://twitter.com/DevTuron                     [...]
                [...]           source code: https://github.com/Arturo0911/Simulation       [...]
""")


def geometric_form(pr: float, i_counter: int) -> float:
    return float(1 - pow((1 - pr),i_counter))

def all_values(k_values: int, pr: float) -> list:
    return [geometric_form(pr, i) for i in range(1, k_values+1)]

def making_values_geometrict(k_values: int, pr: float) -> int:
    uniform_val = uniform(0,1)
    print("[*] Estos son los %s valores generados \n"%k_values)
    for i, j  in enumerate(all_values(k_values, pr)):
        print("%s : %s"%(i+1,j))

    print("\n\n")
    print("[*] El valor aleatorio generados es: %s"%uniform_val)
    # uniform_val = 0.9
    x_value = None
    counter = 1

    for x in range(1, len(all_values(k_values, pr))+1):
        if uniform_val < all_values(k_values, pr)[counter-1]:
            x_value = counter
            break
        else:
            counter += 1
    print("[*] el valor de x corresponde a la posicion : %s que es menor que el valor %s"%(x_value,all_values(k_values, pr)[x_value-1]))



def main():
    # making_values_geometrict(15, 0.4)
    try:
        print("[*] Distribucion geométrica")
        while True:
            k_val = int(input("[*] ingresa la cantidad de valores que debe tener k: "))
            if k_val < 1000:
                break
            else:
                print("[x] El valor de k no debe ser mayor a 1000")

        while True:
            pr_val = float(input("[*] Ingrese el valor de pr: "))
            if pr_val < 1:
                break
            else:
                print("[x] El valor de pr debe ser un valor probabilístico, o sea entre 0 y 1")
        
        making_values_geometrict(k_val, pr_val)
        
    except KeyboardInterrupt:
        print("[*] Saliendo...")
    except Exception:
        print("[*] Saliendo")
    

if __name__ == "__main__":

    main()