"""Question : As an exercise in solving algorithmic problems, you will program to find the midpoint of 1st Street. 
              Say Karel starts in the 5x5 world. Karel should end in the center of 1st row.
              Karel starts at bottom left corner of the world, facing east.
              The initial state of the world includes no interior walls or beepers.
              The world need not be square, but you may assume that it is at least as tall as it is wide.
              If the width of the world is odd, Karel must put the beeper in the center square. 
              If the width is even, Karel must drop a beeper on the left most of the two squares.
"""

from karel.stanfordkarel import *

def main():
    row_midpoint()

def row_midpoint():
    put_beepers_until_wall()

    reset()

    while beepers_present():
        pick_beeper_from_opposite_end()

    if front_is_clear():
        turn_around()
        safe_move()
    put_beeper()
    face_east()
    
    

def pick_beeper_from_opposite_end():
    while beepers_present():
        safe_move()
        if front_is_blocked():
            if beepers_present():
                pick_beeper()
                turn_around()
                safe_move()
            
    turn_around()
    safe_move()
    safe_pick_beeper()

    safe_move()


def put_beepers_until_wall():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


def safe_move():
    if front_is_clear():
        move()

def safe_put_beeper():
    if no_beepers_present():
        put_beeper()

def safe_pick_beeper():
    if beepers_present():
        pick_beeper()

def turn_around():
    for _ in range(2):
        turn_left()

def turn_right():
    for _ in range(3):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()

def face_north():
    while not_facing_north():
        turn_left()

def face_east():
    while not_facing_east():
        turn_left()

def face_south():
    while not_facing_south():
        turn_left()

def face_west():
    while not_facing_west():
        turn_left()

def reset():
    face_west()
    move_to_wall()
    turn_left()
    move_to_wall()
    turn_left()

if __name__ == '__main__':
    main()