"""Question : Write the helper function print_divisors(num), which takes in a number and prints all of its 
              divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is 
              no remainder to the division). Don't forget to call your function in main()!
"""

def print_divisor(num):
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)

def main():
    num = int(input("Enter a number: "))
    print_divisor(num)
    
if __name__ == '__main__':
    main()