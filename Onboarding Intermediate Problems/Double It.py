"""Question : Write a program that asks a user to enter a number. 
              Your program will then double that number and print out the result. 
              It will repeat that process until the value is 100 or greater.
"""

def main():
    
    number = int(input("Enter a number: "))
    while number * 2 <= 200: 
        number *= 2 
        print(number) 
    

if __name__ == '__main__':
    main()