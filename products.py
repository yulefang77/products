# read a file with name 'z-products.csv'
products = []
with open('z-products.csv', 'r', encoding='utf=8') as f:
	for line in f:
		if '商品,價格' in line:
			continue # skip this time, not break this loop
		name, price = line.strip('\n').split(',')
		products.append([name, price])
print(products)

# add product's name and price
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = []
	# p.append(name); p.append(price)
	# p = [name, price]
	products.append([name, price])

#　print product's content
print(products)
for p in products:
	print(p[0], '的價格是', p[1], '。')

# write a file with name 'z-products.csv'
with open('z-products.csv', 'w', encoding='utf=8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')