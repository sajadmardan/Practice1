print('hello git')

products = []
while len(products) < 3:
    while True:
        name = input('Enter product name: ')
        if name in[n['name'] for n in products]:
            print('product already exists')
            continue
        break
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
