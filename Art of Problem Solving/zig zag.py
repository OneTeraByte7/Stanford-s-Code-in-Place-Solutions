"""Question : Karel will be in a blank world at the bottom left corner. 
              Karel should place a zig zag pattern of beepers such that all odd columns 
              have beepers in row 1 and all even columns have beepers in row 2. 
              The world will always have 2 rows and an even number of columns. 
              Karel should end up in the bottom right corner of the world.
"""

from karel.stanfordkarel import *

def main():
    while front_is_clear():
        zig_one_zag()
        move_to_next_zigzag_spot()

def zig_one_zag():
    put_beeper()
    turn_left()
    move()
    turn_right()
    if front_is_clear():
        move()
        put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

def move_to_next_zigzag_spot():
    turn_right()
    move()
    turn_left()
    if front_is_clear():
        move()


if __name__ == '__main__':
    main()