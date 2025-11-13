try:
    a = int(input("a:"))
    b = int(input("b:"))

    print(a/b)
except ZeroDivisionError:
    print("Ділити на нуль не можна!")
except ValueError:
    print('Некоректне значення!')
print('exit')
try:
    path=input("path to file:")
    file=open(path,"r",encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    print('Файл не знайдено! ')
    print('exit')
def register():
    age=int(input("age:"))
    if age<0:
        raise ValueError('Менше нуля не можна ставити вік!!!!!!!')
    else:
        print('IT IS OK!!!!!!!!!')
try:
    register()
except ValueError:
    print('Не можна ставити вік менше 0')







