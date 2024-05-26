"""Question : Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() 
              function for you which asks the user for a number, calls your code for double(num) , and prints the result.
"""

def double(num):
    return num * 2

def main():
    num = int(input("Enter a number: "))
    num_times_2 = double(num)
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()