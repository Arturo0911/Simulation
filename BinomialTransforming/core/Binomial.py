#!/usr/bin/python3

from math import *
from random import *

BANNER = """

  ____  _      __       _ __               _           
   / __ \(_)____/ /______(_) /_  __  _______(_)___  ____ 
  / / / / / ___/ __/ ___/ / __ \/ / / / ___/ / __ \/ __ \
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

"""

class Binomial:

    def __init__(self, uniform_values: int) -> None:
        print(BANNER)
        self.rand_values = [uniform(0,1) for _ in range(uniform_values)]

    def _init_process(self,n_number: int, success: float, u_test_case:float) -> int:
        """
        :param n_number
        :param success
        :param u_test_case 
        """
        counter = 0
        prob_value = pow(float(1 -success), n_number)
        while True:
            
            if u_test_case < prob_value:
                break 
            else:
                prob_value += (float(n_number -  counter) / float(counter + 1)) * ((success)/(1-success) )*prob_value
                counter += 1

        return counter
    def calculating_number_success(self, number:int, success:float) -> list:

        return ["number of success {} for {}: ".format(str(self._init_process(number, success, i)), i) for i in self.rand_values]






