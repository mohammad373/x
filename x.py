# x
from colorama import Fore
import os
os.system("clear")
print(Fore.RED + """
██╗  ██╗                ███╗   ██╗██╗    ██╗██╗    ██╗██████╗ 
██║  ██║                ████╗  ██║██║    ██║██║    ██║██╔══██╗
███████║                ██╔██╗ ██║██║ █╗ ██║██║ █╗ ██║██████╔╝
██╔══██║                ██║╚██╗██║██║███╗██║██║███╗██║██╔══██╗
██║  ██║    ███████╗    ██║ ╚████║╚███╔███╔╝╚███╔███╔╝██████╔╝
╚═╝  ╚═╝    ╚══════╝    ╚═╝  ╚═══╝ ╚══╝╚══╝  ╚══╝╚══╝ ╚═════╝ 
                                                              
""")


time.sleep(2)
import os

import sys
import time
import requests
from colorama import Fore
def __11__():
                            try:
                                # print(Fore.YELLOW + "\nHellow . Welcome Back ;)")
                                # time.sleep(2)
                                target = input(Fore.GREEN + "\nEnter Your Address Target" + Fore.YWLLOW + " ==>  ")
                                time.sleep(2)
                                if target == "" or None :
                                    try:
                                        print(Fore.BLUE + "\nOk Good Lunch ;)")
                                        time.sleep(2)
                                        os.system("clear")
                                        sys.exit()
                                    except:
                                        pass
                                r = requests.get("http://" + target + "/wp-content/plugins/")
                                if r.status_code == 404 or r.status_code == 500:
                                    try:
                                        time.sleep(2)
                                        print(Fore.YELLOW + "\n[!] - Your Target Testing ...")
                                        time.sleep(2)
                                        print(Fore.YELLOW + "\n[!] - Pleass Wait ...")
                                        print(Fore.RED + "\n[-] - Your Target Is Bot WordPress ;(")
                                        time.sleep(2)
                                        sys.exit()
                                    except:
                                        pass
                                else:
                                    try:
                                        time.sleep(2)
                                        print(Fore.YELLOW + "\n[!] - Your Target Testing ...")
                                        time.sleep(2)
                                        print(Fore.YELLOW + "\n[!] - Pleass Wait ...")
                                        print(Fore.GREEN + "\n[+] - Your Target Is WordPress ; ")
                                        time.sleep(2)
                                        sys.exit()
                                    except:
                                        pass
                            except:
                                pass
__11__()
