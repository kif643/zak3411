class Product:
    def __init__(self,price,quantity,bestbeforedate):
        self.price = price
        self.quantity = quantity
        self.bestbeforedate = bestbeforedate
    def print_info(self):
        print(f':{self.price})')
        print(f':{self.quantity})')
        print(f':{self.bestbeforedate})')
Spagetti=Product("1 euro","5","28.04.2027")
print(f'Spagetti price: {Spagetti.price}')
print(f'Spagetti quantity: {Spagetti.quantity}')
print(f'Spagetti bestbeforedate: {Spagetti.bestbeforedate}')
Tomatos=Product("0.8 euro","10","5.12.2025")
print(f'Tomatos price: {Tomatos.price}')
print(f'Tomatos quantity: {Tomatos.quantity}')
print(f'Tomatos bestbeforedate: {Tomatos.bestbeforedate}')
Sweets=Product("1.20 euro","2","7.01.2025")
print(f'Sweets price: {Sweets.price}')
print(f'Sweets quantity: {Sweets.quantity}')
print(f'Sweets bestbeforedate: {Sweets.bestbeforedate}')
Pivo=Product("1.30 euro","0","20.01.2025")
print(f'Pivo price: {Pivo.price}')
print(f'Pivo quantity: {Pivo.quantity}')
print(f'Pivo bestbeforedate: {Pivo.bestbeforedate}')
Milk=Product("0.90 euro","1","20.11.2025")
print(f'Milk price: {Milk.price}')
print(f'Milk quantity: {Milk.quantity}')
print(f'Milk bestbeforedate: {Milk.bestbeforedate}')
class Cart:
    def __init__(self):
        self.buy=[]
    def add(self):
        name_input = input(' Name of the product ')
        quantity_input = input(' Quantity of the product ')
        price_input = input(' Price of the product ')
        bestbeforedate_input = input(' Best beforedate of the product ')



    def print_all_products(self):
        for product in self.buy:
            product.print_info()
Cart=Cart()
while True:
    choose = input(f'Menu:\n[1]-add product\n[2]-display all products\n[3]-exit\nEnter your choice: ')
    if choose == '1':
        Cart.add()
    if choose == '2':
        Cart.print_all_products()
    if choose == '3':
        break
    else:
        print('Make your choice: ')




