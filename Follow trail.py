"""Question : Karel starts off in a world where there is a mysterious trail of beepers. 
              Karel starts off standing on a beeper. Help Karel follow the trail of beepers (picking up beepers as she goes) 
              until the end! We guarantee that the trail will never lead Karel to a spot that is adjacent to a wall. 
              In the world we've provided, we expect Karel to end up in the third cell down from the top right corner, facing East.
"""

from karel.stanfordkarel import *

def main():
    while beepers_present():
        follow_straight_trail()
        step_backwards()
        turn_left()
        move()

        if no_beepers_present():
            step_backwards()
            turn_around()
            move()

def follow_straight_trail():
    while beepers_present():
        pick_beeper()
        move()

def step_backwards():
    turn_around()
    move()
    turn_around()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()