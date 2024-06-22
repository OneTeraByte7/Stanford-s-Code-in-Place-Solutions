"""Question : Implement the following function which takes in 3 integers as parameters:"""

def in_range(n, low, high):
    if n >= low and n <= high:
        return True

    return False

def main():
	n = input("n: ")
	low = input("low: ")
	high = input("high: ")
	if in_range(n, low, high):
		print("n is in range!")
	else:
		print("n is not in range...")


if __name__ == '__main__':
    main()