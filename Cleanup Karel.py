"""Question : Karel is so good at cleaning up beepers that they decided to not just clean up one spot, 
              but all of the spots! Lots of beepers have been spread across the world and Karel wants to clean them all up.
              Luckily, someone wrote a program that helps us do this task. However, it has not been decomposed at all and can be a bit hard to read. 
              We've provided their code below. Try to decompose their code into helper functions to make the main() function easier to read!
"""

from karel.stanfordkarel import *

def main():
   
    while left_is_clear():
        while front_is_clear():
            if beepers_present():
                pick_beeper()
            move()
            
        if beepers_present():
            pick_beeper()
        
        for i in range(2):
            turn_left()
        
        while front_is_clear():
            move()

        for i in range(3):
            turn_left()
        move()
    
        for i in range(3):
            turn_left()
    
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        move()
    
    if beepers_present():
        pick_beeper()
        

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()