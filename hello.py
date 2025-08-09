from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

name = input(Fore.CYAN + "What's your name? " + Style.RESET_ALL)
time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(Fore.GREEN + f"\nHello, {name}! 👋")
print(Fore.YELLOW + f"The current date and time is: {time_now}")
print(Fore.MAGENTA + "Your virtual environment is working correctly ✅")
print(Fore.RED + "Our first GitHub commit!")