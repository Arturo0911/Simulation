#!/usr/bin/python3

import random
import math

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

def aproximations_int1(range_numbers:int, limit_a:int, limit_b:int)->float:

    random_float_numbers = [ (((limit_b - limit_a)*random.uniform(0,1))+limit_a)  for i in range(0,range_numbers)]
    function_applied = [value/math.log(value) for value in random_float_numbers]
    sum_float = sum(function_applied)/float(range_numbers)
    
    return sum_float


def aproximations_int2(range_numbers:int, limit_a:int, limit_b:int)->float:

    random_float_numbers = [ (((limit_b - limit_a)*random.uniform(0,1))+limit_a)  for i in range(0,range_numbers)]
    function_applied = [  (((math.pow(value, 4))/4)+(5*math.pow(value, 3)/3)-(10*value))     for value in random_float_numbers]
    sum_float = sum(function_applied)/float(range_numbers)
    
    return sum_float


def CLI():

    presentation()
    try:
        range_numbers = int(input("input the range to generate the random numbers: "))
        range_a = int(input("input the limit a: "))
        range_b = int(input("input the limit b: "))

        print("ln^x")
        print(aproximations_int1(range_numbers, range_a, range_b),"\n")
        

        range_a = int(input("\ninput the limit a: "))
        range_b = int(input("\ninput the limit b: "))

        print("∫(X³ + 5x² - 10 dx)")
        print(aproximations_int2(range_numbers, range_a, range_b))
    
    except:
        print("You should to input numbers no another format!")


def main():
    cli = CLI()

if __name__ == '__main__':
    
    main()


