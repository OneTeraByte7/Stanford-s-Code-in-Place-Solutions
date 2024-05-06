"""Question : Your job is to write code which gets Karel over the obstacles and puts beepers 
              in the squares directly to the right of the walls, and moves Karel to the bottom right corner of the world.
              Karel starts in the bottom left corner of a world with three "obstacles" 
"""

from karel.stanfordkarel import *

def main():
    move()
    turn_left()
    move()
    for i in range(3):
        turn_left()
    move()
    for i in range(3):
        turn_left()
    move()
    put_beeper()

    for i in range(2):
        turn_left()
    move()

    for i in range(3):
        turn_left()
    move()
    for i in range(3):
        turn_left()
    move()
    put_beeper()

    for i in range(2):
        turn_left()
    move()

    for i in range(3):
        turn_left()
    move()
    for i in range(3):
        turn_left()
    move()
    put_beeper()
    turn_left()

    for i in range(2):
        move()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()