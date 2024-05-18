"""Question : Converts feet to inches. Feet is an American unit of measurement. 
              There are 12 inches per foot. Foot is the singular, and feet is the plural.
"""

INCHES_IN_FOOT = 12  

def main():
    feet = float(input("Enter number of feet: "))  
    inches = feet * INCHES_IN_FOOT  
    print("That is", inches, "inches!")
    
if __name__ == '__main__':
    main()