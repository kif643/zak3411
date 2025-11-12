class Product:
    def __init__(self,name,price,quantity,bestbeforedate):
        self.name=name
        self.price = price
        self.quantity = quantity
        self.bestbeforedate = bestbeforedate
    def print_info(self):
        print(f'name:{self.name}')
        print(f'price:{self.price}')
        print(f'quantity:{self.quantity}')
        print(f'bestbefordate:{self.bestbeforedate}')
Spagetti=Product("Spagetti","1 euro","5","28.08.2026")
print(f'Spagetti name: {Spagetti.name}')
print(f'Spagetti price: {Spagetti.price}')
print(f'Spagetti quantity: {Spagetti.quantity}')
print(f'Spagetti bestbeforedate: {Spagetti.bestbeforedate}')
Tomatos=Product("Tomato","0.8 euro","2","30.11.2025")
print(f'Tomatos name: {Tomatos.name}')
print(f'Tomatos price: {Tomatos.price}')
print(f'Tomatos quantity: {Tomatos.quantity}')
print(f'Tomatos bestbeforedate: {Tomatos.bestbeforedate}')
Sweets=Product("Sweets","1.20","10","01.01.2026")
print(f'Sweets name: {Sweets.name}')
print(f'Sweets price: {Sweets.price}')
print(f'Sweets quantity: {Sweets.quantity}')
print(f'Sweets bestbeforedate: {Sweets.bestbeforedate}')
Pivo=Product("Pivo","1.30","0","16.04.2026")
print(f'Pivo name: {Pivo.name}')
print(f'Pivo price: {Pivo.price}')
print(f'Pivo quantity: {Pivo.quantity}')
print(f'Pivo bestbeforedate: {Pivo.bestbeforedate}')
Milk=Product("Milk","0.60","2","26.11.2025")
print(f'Milk name: {Milk.name}')
print(f'Milk price: {Milk.price}')
print(f'Milk quantity: {Milk.quantity}')
print(f'Milk bestbeforedate: {Milk.bestbeforedate}')
class Cart:
    def __init__(self):
        self.buy=[]
    def add(self,good):
       self.buy.append(good)
        # self.name_input = input(' Name of the product ')
        # self.quantity_input = input(' Quantity of the product ')
        # self.price_input = input(' Price of the product ')
        # self.bestbeforedate_input = input(' Best beforedate of the product ')



    def print_all_products(self):
        for product in self.buy:
            product.print_info()
Cart=Cart()
while True:
    choose = input(f'Menu:\n[1]-add product\n[2]-display all products\n[3]-exit\nEnter your choice: ')
    if choose == '1':
        product=Product(input('price:'),input('quantity:'),input('bestbeforedate:'),input('name:'))
        Cart.add(product)
    if choose == '2':
        Cart.print_all_products()
    if choose == '3':
        break
    else:
        print('Make your choice: ')




