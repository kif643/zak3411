import requests
# response=requests.get('https://httpbin.org/get')
# response=requests.post("https://httpbin.org/post","IT Step", headers={"h1":  "IT Step"})
response=requests.get('https://coinmarketcap.com/')
response_text=response.text
parsed=response_text.split('<span>')
coins=[]
for element in parsed:
    if element.startswith("$"):
        for price in element.split("</span>"):
            if price.startswith("$"):
                coins.append(price)
print(f'Bitcoin:{coins [0]}')
bit_coin_price=float(coins[0][1:].replace(",",""))
count=int(input("How many coins do you have?"))
print(f'You have ${count * bit_coin_price}')

