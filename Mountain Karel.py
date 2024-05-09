"""Question : Make Karel climb a mountain of any size and plants a beeper on top. You may assume that Karel starts facing the base of the mountain."""

from karel.stanfordkarel import *


def main():
    climb_mountain()
    put_beeper()
    descend_mountain()
    

def climb_mountain():
    while front_is_blocked():
        step_up()
        
        
def descend_mountain():
    while front_is_clear():
        step_down()


def step_down():
    move()
    turn_right()
    move()
    turn_left()
    
    
def step_up():
    turn_left()
    move()
    turn_right()
    move()


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    main()