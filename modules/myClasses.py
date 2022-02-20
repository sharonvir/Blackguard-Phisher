import time, os
from colorama import Fore as Color


class Psentense:
    def printer(self, sentense): #Get a input from the user and Type print it out 
        sentense_len = len(sentense)
        for letter in range(sentense_len):
            print(Color.CYAN + sentense[letter], end='', flush = True);time.sleep(0.1) #print it  out word by word




class Introduce(Psentense):
    def __init__(self):
        os.system('clear')
        self.printer("[!] Hello Friend :) | wwww.blackberryy.ir")
        time.sleep(1)
        print(Color.GREEN+"""                        
  __  __ _____    _____ ____  ______ _  _  __ ______ 
 |  \/  |  __ \  |  __ \___ \|  ____| || |/_ |____  |
 | \  / | |__) | | |  | |__) | |__  | || |_| |   / / 
 | |\/| |  _  /  | |  | |__ <|  __| |__   _| |  / /  
 | |  | | | \ \ _| |__| |__) | |       | | | | / /   
 |_|  |_|_|  \_(_)_____/____/|_|       |_| |_|/_/    
                                                 ,Product


        """)

        time.sleep(0.6)








	    	    


    