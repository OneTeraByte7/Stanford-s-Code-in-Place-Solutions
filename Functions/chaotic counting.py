"""Question : Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch. 
              We've written a done() function which returns True with likelihood DONE_LIKELIHOOD -- at each number, 
              before printing the number, you should call done() and check if it returns True or not. If done() returns 
              True, we're done counting, and you should use a return statement to end the chaotic_counting() function 
              execution and resume execution of main(), which will print "I'm done.
"""

import random

DONE_LIKELIHOOD = 0.3

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return
        print(curr_num)
    
def done():
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()