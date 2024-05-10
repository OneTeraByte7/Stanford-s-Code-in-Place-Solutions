"""Question : Your job is to make Karel pick up the beeper, move to the top of the world, 
              put the beeper down at the top of column 2, and then end up in the top right corner, 
              so that the end result looks like this:
"""

from karel.stanfordkarel import *

def main():
    move()
    pick_beeper()
    turn_left()
    for i in range(2):
        move()
    put_beeper()
    for i in range(3):
        turn_left()
    move()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()