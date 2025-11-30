import random
import colorama
from colorama import Fore
print(Fore.RED+'HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!!!!!!!!!!!!')
print(random.randint(0,99999999999999999999999999999999999999))
print(Fore.GREEN)
try:
    a=int(input("a:"))
    b=int(input("b:"))
    print(a/b)
except ZeroDivisionError:
    print("Ділити на нуль не можна!!!")
except ValueError:
    print("Не можна ставити букви!!!")
print(Fore.BLUE)
a=int(random.randint(0,9999999999999999999999999999))
b=int(random.randint(0,9999999999999999999999999999))
print(a/b)
print(Fore.YELLOW)
a=int(random.randint(0,9999999999999999999999999999))
b=int(random.randint(0,9999999999999999999999999999))
print(a+b)
print(Fore.CYAN)
a=int(random.randint(0,9999999999999999999999999999))
b=int(random.randint(0,9999999999999999999999999999))
print(a-b)
print(Fore.MAGENTA)
a=int(random.randint(0,9999999999999999999999999999))
b=int(random.randint(0,9999999999999999999999999999))
print(a*b)
print(Fore.WHITE+'BYE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

