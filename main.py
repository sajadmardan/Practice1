print('hello git')

products = []
while len(products) < 3:
    name = input('Enter product name: ')
    price = float(input('Enter product price: '))
    products.append({'name': name, 'price': price})
print(products)
