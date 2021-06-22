#!/usr/bin/python3


import random
from pprint import pprint
from typing import Any

BANNER = """
#################################################################################################################################################

db    db  .d8b.  d8888b. d888888b  .d8b.  d8888b. db      d88888b      .d8b.  db      d88888b  .d8b.  d888888b  .d88b.  d8888b. d888888b  .d8b.  
88    88 d8' `8b 88  `8D   `88'   d8' `8b 88  `8D 88      88'         d8' `8b 88      88'     d8' `8b `~~88~~' .8P  Y8. 88  `8D   `88'   d8' `8b 
Y8    8P 88ooo88 88oobY'    88    88ooo88 88oooY' 88      88ooooo     88ooo88 88      88ooooo 88ooo88    88    88    88 88oobY'    88    88ooo88 
`8b  d8' 88~~~88 88`8b      88    88~~~88 88~~~b. 88      88~~~~~     88~~~88 88      88~~~~~ 88~~~88    88    88    88 88`8b      88    88~~~88 
 `8bd8'  88   88 88 `88.   .88.   88   88 88   8D 88booo. 88.         88   88 88booo. 88.     88   88    88    `8b  d8' 88 `88.   .88.   88   88 
   YP    YP   YP 88   YD Y888888P YP   YP Y8888P' Y88888P Y88888P     YP   YP Y88888P Y88888P YP   YP    YP     `Y88P'  88   YD Y888888P YP   YP 

                            d8888b. d888888b .d8888.  .o88b. d8888b. d88888b d888888b  .d8b.  
                            88  `8D   `88'   88'  YP d8P  Y8 88  `8D 88'     `~~88~~' d8' `8b 
                            88   88    88    `8bo.   8P      88oobY' 88ooooo    88    88ooo88 
                            88   88    88      `Y8b. 8b      88`8b   88~~~~~    88    88~~~88 
                            88  .8D   .88.   db   8D Y8b  d8 88 `88. 88.        88    88   88 
                            Y8888D' Y888888P `8888Y'  `Y88P' 88   YD Y88888P    YP    YP   YP 
                                                                  

                            Arturo Negreiros Samanez
                            Universidad Agraria del Ecuador
                            date 21/06/2021

#################################################################################################################################################\n\n\n\n
"""



class RandomDiscrete:

    def __init__(self, cases_to_evaluate: int) -> None:
        print(BANNER)
        self.random_values = [random.uniform(0,1) for _ in range(cases_to_evaluate)]

    def _checking_random_discrete(self, data: list) -> bool:
        return (len([set(data)]) == 1) and (list(set([data[x] == data[x-1] for x in range(len(data))]))[0] is True) and (list(set(data))[0] == float(1/len(data)))


    def find_position_value(self, data: list, x_values: list) -> Any:
        return [x_values[int((x*len(data))+1) - 1] for x in self.random_values] if self._checking_random_discrete(data) else ["Se aplica transformación inversa: " + self.inverse_transforming(data, x_values, i) for i in self.random_values]
    
    def inverse_transforming(self, data: list, x_values: list, random_float_number: float) -> Any:
        case = data[0]
        x_sample = 0
        counter = 0
        for _ in range(len(data)):
            if random_float_number < case:
                x_sample = x_values[counter]
                break
            else:
                counter += 1
                case += data[counter]

        return "El caso de prueba {} mostró se obtuve {}".format(random_float_number, x_sample)



def main() -> None:
    random_val = RandomDiscrete(3)

    print("[*] Ingresa separado por espacios las probabilidades para verificar si es aleatoria discreta o no...")
    random_values = list(map(float, input("[*] ~> ").split()))
    print("[*] Ingresa los valores correspondientes a cada caso de P(x)")
    integer_values = list(map(int, input("[*] ~> ").split()))
    print(random_values)
    print(integer_values)
    pprint(random_val.find_position_value(random_values, integer_values))
    #print(random_val.find_position_value([0.5,0.6,0.5]))

if __name__ == "__main__":
    main()
