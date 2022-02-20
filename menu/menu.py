import os, sys, requests
from subprocess import Popen
from colorama import Fore as color 
from time import sleep

bold = '\033[1m'
endbold = '\033[0m'

def banner():
    os.system('clear')
    print(color.RED+"""
        
  __  __ _____    _____ ____  ______ _  _  __ ______ 
 |  \/  |  __ \  |  __ \___ \|  ____| || |/_ |____  |
 | \  / | |__) | | |  | |__) | |__  | || |_| |   / / 
 | |\/| |  _  /  | |  | |__ <|  __| |__   _| |  / /  
 | |  | | | \ \ _| |__| |__) | |       | | | | / /   
 |_|  |_|_|  \_(_)_____/____/|_|       |_| |_|/_/    
                                                     
                           """+color.WHITE+'version 1.0')
    print(bold +color.LIGHTWHITE_EX+"""    
┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑ 
    ------------------------------------
    ⚒  Programmer: MR.D3F417           ⚒
    ⚒  Lable : BlackGUARD              ⚒
    ⚒  Discord : discord.gg/KsskgvE48z ⚒
    ------------------------------------
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""+endbold)
    sleep(0.1)


def menu_respaws():
    try:
        print(color.RED+"[1] "+ color.LIGHTYELLOW_EX+"INSTAGRAM")
        print(color.CYAN+"*********************")
        sleep(0.1)
        
        print(color.RED+"[0] "+ color.LIGHTYELLOW_EX+"Exit")
        print(color.CYAN+"*********************")
        sleep(0.1)
    except:
        print(color.RED+"[-] Something Went Wrong....")
        sleep(1)
        sys.exit()



