"""Question : Since it's springtime, Karel will make the "flowers" bloom! Each flower is comprised of four beepers and 
              goes directly on top of each stem, so that the end result for this world looks like this 
              (note that Karel should end up in the bottom right corner)
"""

from karel.stanfordkarel import *

def main():
    for i in range(2):
        move_to_wall()
        bloom_flower()
    move_to_wall()

def bloom_flower():
    climb_stem()
    make_bloom()
    move_to_wall()
    turn_left()

def climb_stem():
    turn_left()
    while right_is_blocked():
        move()

def make_bloom():
    put_beeper()
    move()
    for i in range(2):
        put_beeper()
        turn_right()
        move()
    put_beeper()

def move_to_wall():
    while front_is_clear():
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()