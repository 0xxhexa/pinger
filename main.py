import os
import time
import colorama
from colorama import Fore
import msvcrt

def main():
    os.system("cls")
    print(f"{Fore.LIGHTBLUE_EX}_  _ ____ _  _ ____    ___  _ _  _ ____ ____ ____ ")
    print(f"|__| |___  \/  |__|    |__] | |\ | | __ |___ |__/ ")
    print(f"|  | |___ _/\_ |  |    |    | | \| |__] |___ |  \ ")
    print(f"                                                  ")
    hostname = input(f"[>>] IP: ")
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            print("Close in 3sec")
            time.sleep(1)
            print("Close in 2sec")
            time.sleep(1)
            print("Close in 1sec")
            time.sleep(1)
            os.system('cls')
            main()
            break

        status = os.system(f"ping -n 1 {hostname} > nul")

        if status == 0:
            print(f"{Fore.LIGHTBLUE_EX}{hostname} is ON!")
        else:
            print(f"{Fore.LIGHTRED_EX}{hostname} is OFF!")

main()