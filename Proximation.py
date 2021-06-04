#!/usr/bin/python3

import random

PRESENTATION = """
        :::'###::::'########::'########::'########:::'#######::'##::::'##:'####:'##::::'##::::'###::::'########:'####::'#######::'##::: ##::'######::
        ::'## ##::: ##.... ##: ##.... ##: ##.... ##:'##.... ##:. ##::'##::. ##:: ###::'###:::'## ##:::... ##..::. ##::'##.... ##: ###:: ##:'##... ##:
        :'##:. ##:: ##:::: ##: ##:::: ##: ##:::: ##: ##:::: ##::. ##'##:::: ##:: ####'####::'##:. ##::::: ##::::: ##:: ##:::: ##: ####: ##: ##:::..::
        '##:::. ##: ########:: ########:: ########:: ##:::: ##:::. ###::::: ##:: ## ### ##:'##:::. ##:::: ##::::: ##:: ##:::: ##: ## ## ##:. ######::
         #########: ##.....::: ##.....::: ##.. ##::: ##:::: ##::: ## ##:::: ##:: ##. #: ##: #########:::: ##::::: ##:: ##:::: ##: ##. ####::..... ##:
         ##.... ##: ##:::::::: ##:::::::: ##::. ##:: ##:::: ##:: ##:. ##::: ##:: ##:.:: ##: ##.... ##:::: ##::::: ##:: ##:::: ##: ##:. ###:'##::: ##:
         ##:::: ##: ##:::::::: ##:::::::: ##:::. ##:. #######:: ##:::. ##:'####: ##:::: ##: ##:::: ##:::: ##::::'####:. #######:: ##::. ##:. ######::
        ..:::::..::..:::::::::..:::::::::..:::::..:::.......:::..:::::..::....::..:::::..::..:::::..:::::..:::::....:::.......:::..::::..:::......:::
"""

def presentation():
    print(PRESENTATION)
    print("[*] Owner Arturo Negreiros")
    print("[*] Follow me https://twitter.com/DevTuron\n")

def aproximations(range_numbers:int, limit_a:int, limit_b:int)->float:

    random_float_numbers = [ (((limit_b - limit_a)*random.uniform(0,1))+limit_a)  for i in range(0,range_numbers)]
    function_applied = [((value/2)+ value)  for value in random_float_numbers]
    sum_float = sum(function_applied)/float(range_numbers)
    
    return sum_float


def CLI():

    presentation()
    try:
        range_numbers = int(input("input the range to generate the random numbers: "))
        range_a = int(input("input the limit a: "))
        range_b = int(input("input the limit b: "))

        print(aproximations(range_numbers, range_a, range_b))
    
    except:
        print("You should to input numbers no another format!")


def main():
    cli = CLI()

if __name__ == '__main__':
    
    main()


