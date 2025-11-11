class PC:
    pass
pc=PC()
import inspect
import random
import sys
print(f'random is module-{inspect.ismodule(random)}')
print(f'random is method-{inspect.ismethod(random)}')
print(f'PC is class?-{inspect.isclass(PC)}')
print(f'platform is {sys.platform}')
print(sys.argv)
print(sys.executable)
print(sys.version)
for name,path in sys.modules.items():
    print(f'name:{name}, path:{path}')
# for _ in dir(sys):
#     print(_)
# a=1
# b=3.14
# c=True
# d="text"
#
# print(type(pc))
# print(f'{a} is {type (a)}')
# print(f'{b} is {type (b)}')
# print(f'{c} is {type(c)}')
# print(f'{d} is {type(d)}')
# for _ in dir(a):
#     print(_)
