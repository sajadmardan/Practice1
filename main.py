print('hello git')

products = []
while len(products) < 3:
    name = input('Enter product name: ')
    price = float(input('Enter product price: '))
    products.append({'name': name, 'price': price})

found = False
new_products = input('Enter products name: ')
for product in products:
    if product['name'] == new_products:
        found = True
        print('new product price:', product['price'], 'new product name:', product['name'])
if not found:
    print('product not found')
print(products)
