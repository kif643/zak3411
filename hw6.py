result = []
def divider(a, b):
 if a < b:
    raise ValueError
 if b > 100:
     raise IndexError
 return a/b
try:
    data = {10: 2, 2: 5, 123: 4, 18: 1, (): 15, 8: 4}
except TypeError:
    print('Напишіть щось в дужках!')
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ValueError:
        print(f'Пропущен елемент через помилку значення!')
    except TypeError:
        print(f'Пропущено і за несумісних типів порівнянь!')


print(result)