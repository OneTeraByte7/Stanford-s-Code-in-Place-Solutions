"""Question : Write a program which takes as input the number of sides on a dice.  
             Then, simulate rolling a dice with that many sides. Print the outcome of the roll.
             If a dice has 8 sides, rolling the dice should produce one of the following values: 
             1, 2, 3, 4, 5, 6, 7, 8
             If the dice had only 4 sides, it could result one of the following values:
             1, 2, 3, 4
             Recall that python has a special function random.randint(...) which takes in two numbers: a minimum value and a maximum value. 
             randint will return back a random whole number which is greater than or equal to the min, and less than or equal to the max:
              
"""

import random

def main():
    x = int(input("How many sides does your dice have?"))

    y = random.randint(0,x)

    print(y)


if __name__ == '__main__':
    main()