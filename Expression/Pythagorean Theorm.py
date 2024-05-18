"""Question : Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle 
              and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!
              The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. 
              It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.
"""

import math

def main():
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    bc = math.sqrt(ab**2 + ac**2)
    print("The length of BC (the hypotenuse) is: " + str(bc))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()