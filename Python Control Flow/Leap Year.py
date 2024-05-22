"""Question : Write a program that reads a year from the user and tells whether a given year is a leap year or not.
              A leap year (also known as an intercalary year or bissextile year) is a calendar year that contains an 
              additional day (or, in the case of a lunisolar calendar, a month) added to keep the calendar year synchronized 
              with the astronomical year or seasonal year. In the Gregorian calendar, each leap year has 366 days instead of 365, 
              by extending February to 29 days rather than the common 28.
"""

def main():
    # Get the year to check from the user
    year = int(input('Please input a year: '))

    if year % 4 == 0:  # Checking whether the provided year is evenly divisibly by 4
        if year % 100 == 0:  # Checking whether the provided year is evenly divisibly by 100
            if year % 400 == 0:  # Checking whether the provided year is evenly divisibly by 400
                print("That's a leap year!")
            else:  # (Not divisible by 400)
                print("That's not a leap year.")
        else:  # (Not divisible by 100)
            print("That's a leap year!")
    else:  # (Not divisible by 4)
        print("That's not a leap year.")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
