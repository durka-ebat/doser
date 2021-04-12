import os
from colorama import Fore, Back, Style

def banner():
    print(Fore.MAGENTA + "──╔╗")
    print(Fore.MAGENTA + "──║║")
    print(Fore.MAGENTA + "╔═╝╠══╦══╦══╦═╗")
    print(Fore.MAGENTA + "║╔╗║╔╗║══╣║═╣╔╝")
    print(Fore.MAGENTA + "║╚╝║╚╝╠══║║═╣║")
    print(Fore.MAGENTA + "╚══╩══╩══╩══╩╝")

banner()

cycles1 = int(0)
cycles2 = int(1)
site = input("Введите сайт: ")
os.system('cls' if os.name=='nt' else 'clear')

def dos1():
    os.system("ping " + site)
    print(Fore.GREEN + "Пакеты успешно отправлены! (Ctrl + C для остановки)")

while cycles1 < cycles2:
    dos1()