

from random import uniform
from math import exp

print("""
    [...]           Owner: Arturo Negreiros Samanez                             [...]
    [...]           date:  09/07/2021                                           [...]
    [...]           follow me: https://twitter.com/DevTuron                     [...]
    [...]           source code: https://github.com/Arturo0911/Simulation       [...]
""")

# achieving an array with the number of
# uniforms we will work
def make_uniform_values(k_times: int) -> list:
    return [uniform(0,1) for _ in range(k_times)]

def implement_distribution(lambda_value, uniform_value):
    
    p_value = exp(-lambda_value)
    f_cumulator = p_value
    counter = 0
    x_val = 0
    while True:
        if uniform_value < f_cumulator:
            x_val = counter
            break
        else:
            p_value *= float((lambda_value)/(counter +1))
            f_cumulator += p_value
            counter += 1

    return x_val


def make_simulations(lambda_value, k_items):

    for x in make_uniform_values(k_items):
        print("el número de evento es {} correspondiente al valor aleatorio {}".format(implement_distribution(lambda_value, x),x))



def main():

    while True:
        try:
            k_values  = int(input("[*] Ingrese el número de simulaciones (k) que desee probar: "))
            if k_values < 0:
                print("[*] Ingresaste un número positivo, por lo que el número se lo tomará como positivo")
                k_values = abs(k_values)
            break
        except:
            print("[*] Debe ingresar un número entero positivo")

    while True:
        try:
            lambda_val = float(input("[*] Ingrese el valor de lambda: "))
            if lambda_val <= - 1:
                print("[!] debe ser un valor positivo lambda; por lo que se convertirá tu valor negativo a positivo")
                lambda_val = abs(lambda_val)
            break
        except:
            print("[X] Debe ingresar un valor numérico")

    make_simulations(lambda_val, k_values)

if __name__ == "__main__":
    main()
