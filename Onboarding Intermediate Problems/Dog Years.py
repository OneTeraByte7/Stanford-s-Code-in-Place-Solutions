"""Question : Dogs have different lifespans than humans. 
                  Thus there age is sometimes reported in "dog years" which are scaled to be comparable to human ages. 
                  On average every calendar year is equal to 7.18 dog years. To convert 3 calendar years to dog years, 
                  you multiply 3 * 7.18 to get 21.54 dog years. That means, if your dog is 3 years old, they're past their teenage years!
"""

#One Year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18  

def main():
    num1 = float(input("Enter an age in calendar years:"))
    years = num1 * DOG_YRS_MULTIPLIER
    print("That's", years ,"in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()