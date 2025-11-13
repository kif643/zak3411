import inspect
import sys
import random
from colorama import Fore

from les4 import GameComputer
from les5 import PC

print(Fore.GREEN+ 'This text is red')
print(f'{inspect.currentframe().f_code.co_name}')
print(f'{inspect.ismethod}')
print(f'{inspect.isfunction}')
print(f'{inspect.isdatadescriptor}')
print(f'{inspect.iscode}')
print(f'{inspect.isroutine}')
print(f'{inspect.signature}')
print(f'{inspect.signature.__doc__}')
print(Fore.RED+ 'EROR')
print(inspect.getsourcelines(GameComputer)[0])
print(sys.argv)
print(Fore.YELLOW)
print(sys.executable)
print(Fore.BLUE)
print(f'platform is {sys.platform}')
class PC:
    print(f'random is module-{inspect.ismodule(random)}')
    print(f'random is method-{inspect.ismethod(random)}')
    print(f'PC is class?-{inspect.isclass(PC)}')
    print(f'platform is {sys.platform}')
print(Fore.GREEN+ 'GOODBYE!!!!!!!!!!!!')
print(inspect.findsource(PC)[0])
print(inspect.isawaitable(PC))
print(inspect.signature(PC))
print(inspect.signature(PC).parameters)
print(Fore.BLACK)
print(inspect.classify_class_attrs(cls=PC))
print(inspect.BufferFlags)
print(inspect.CO_GENERATOR)
print(random.SystemRandom)
print(Fore.CYAN+'B')
print(Fore.RED+'Y')
print(Fore.LIGHTMAGENTA_EX+'E')



