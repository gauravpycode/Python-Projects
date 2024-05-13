import random
import rich
from rich.console import Console

CONSOLE = Console()
SYMBOLS = list("!@#$%^&*()_+{}\":>?<,./;'[]/")
NUMBERS = list("123457890")
UPPERCASE = list("QWERTYUIOPASDFGHJKLZXCVBNM")
LOWERCASE = list("qwertyuiopasdfghjklzxcvbnm")

def create_password():
    PASSWORD = []

    for i in range(0,upper):
        rndm = random.choice(UPPERCASE)
        PASSWORD.append(rndm)
    
    for j in range(0,number):
        rndm = random.choice(NUMBERS)
        PASSWORD.append(rndm)
    
    for k in range(0,symbol):
        rndm = random.choice(SYMBOLS)
        PASSWORD.append(rndm)

    for l in range(0,lower):
        rndm = random.choice(LOWERCASE)
        PASSWORD.append(rndm)

    random.shuffle(PASSWORD)
    PASSWORD = "".join(PASSWORD)
    CONSOLE.print(f"[green]Your password is here:[/green] [white]{PASSWORD}[/white]")

upper = int(input("Number of uppercase letters in password: "))
number = int(input("Number of numericals in password: "))
symbol = int(input("Number of symbols in password: "))
lower = int(input("Number of lowercase letters in password: "))
create_password()