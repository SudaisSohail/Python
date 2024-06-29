import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

for i in range(2):
    print(f"{Fore.RED} {Style.BRIGHT} {Back.BLACK} I love IBRAHIM.")
    print(f"{Fore.BLACK} {Style.BRIGHT} {Back.BLACK} I love IBRAHIM.")
    print(f"{Fore.BLUE} {Style.BRIGHT} {Back.BLACK} I love IBRAHIM.")
    print(f"{Fore.WHITE} {Style.BRIGHT} {Back.BLACK} I love IBRAHIM.")
    print(f"{Fore.GREEN} {Style.BRIGHT} {Back.BLACK} I love IBRAHIM.")
    print(f"{Fore.YELLOW} {Style.BRIGHT} {Back.BLACK} I love IBRAHIM.")
    print(f"{Fore.BLACK} {Style.BRIGHT} {Back.BLACK} I love IBRAHIM.")
    print(f"{Fore.CYAN} {Style.BRIGHT} {Back.BLACK} I love IBRAHIM. \n")
