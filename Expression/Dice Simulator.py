"""Question : Simulate rolling two dice, three times.  
              Prints the results of each die roll.  
              This program is used to show how variable scope works.
"""

import random

NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print("Total of two dice:", total)

def main():
    
    random.seed(1)
    
    die1 = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))


if __name__ == '__main__':
    main()