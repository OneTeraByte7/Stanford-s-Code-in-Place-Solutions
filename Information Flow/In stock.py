"""Question : Karel has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and 
              returns how many of that fruit are in her inventory.
"""

def main():
	fruit = input("Enter a fruit: ")
	stock = num_in_stock(fruit)
	if stock == 0:
		print("This fruit is not in stock.")
	else:
		print("This fruit is in stock! Here is how many:")
		print(stock)

def num_in_stock(fruit):
	"""
	This function returns the number of fruit Karel has in stock.
	"""
	if fruit == 'apple':
		return 2
	if fruit == 'durian':
		return 4
	if fruit == 'pear':
		return 1000
	else:
		return 0


if __name__ == '__main__':
    main()