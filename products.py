import os # operating system

# check if the file exists
def read_file(filename):
	with open(filename, 'r', encoding='utf=8') as f:
		products = []	
		for line in f:
			if '商品,價格' in line:
				continue # skip this time, not break this loop
			name, price = line.strip('\n').split(',')
			products.append([name, price])
	print(products)
	return products

# add product's name and price
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		products.append([name, price])
	#　print product's content
	print(products)
	p = []
	for p in products:
		print(p[0], '的價格是', p[1], '。')
	return products

# write a file
def write_file(filename, products):
	with open(filename, 'w', encoding='utf=8') as f:
		f.write('商品,價格\n')
		p = []
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'z-products.csv'
	if os.path.isfile(filename):
		print('yeah！找到檔案了！')
		products = read_file(filename)
		products = user_input(products)
		write_file(filename, products)
	else:
		print('找不到檔案。')

main()