"""Question : Karel has been hired to build the columns in the Temple of Artemis in Efes. 
              In particular, there are a set of arches where the stones (represented by beepers, of course) 
              are missing from the columns supporting the arches,Karel may count on the following facts about the world, listed below:

              Karel starts at bottom left corner, facing right (aka east).

              The columns are exactly four squares apart, on the 1st, 5th, 9th, and 13th columns.

            Karel can assume that columns are always five units high.
    """
    
from karel.stanfordkarel import *



def main():
    move()
    turn_left()
    for i in range(4):
        move()

    turn_left()
    move()
    put_beeper()
    turn_left()

    for i in range(4):
        move()
        put_beeper()

    turn_left()

    for i in range(5):
        move()

    turn_left()
    for i in range(4):
        move()

    turn_left()
    move()
    put_beeper()
    turn_left()

    for i in range(4):
        move()
        put_beeper()

    turn_left()

    for i in range(5):
        move()

    turn_left()
    for i in range(4):
        move()

    turn_left()
    move()
    put_beeper()
    turn_left()

    for i in range(4):
        move()
        put_beeper()

    turn_left()
    
    for i in range(3):
        move()

    turn_left()
    move()
    move()
    move()
    move()

    for i in range(3):
        turn_left()
    move()
    for i in range(3):
        turn_left()

    for i in range(3):
        put_beeper()
        move()
    put_beeper()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    move()
    turn_left()
    move()
    put_beeper()
    
if __name__ == '__main__':
    main()