from karel.stanfordkarel import *

def main():
    while left_is_clear():
        even_beeper()
        back_and_row_change()
        odd_beeper()
        if left_is_clear():
            back_and_row_change()
        if left_is_blocked():
            if no_beepers_present():
                back_and_row_change()
                even_beeper()
    reset_position()

def even_beeper():
    if front_is_clear():
        checkerboard_pattern()
    else:
        put_beeper()

def odd_beeper():
    if front_is_clear():
    	move()
    checkerboard_pattern()

def checkerboard_pattern():
    while front_is_clear():
            put_beeper()
            if front_is_clear():
                move()
                if front_is_clear():
                    move()
                    if front_is_blocked():
                        put_beeper()

def back_and_row_change():
    if left_is_clear():
        turn_around()
        move_to_wall()
        turn_around()
        turn_left()
        move()
        turn_right()

def turn_around():
    for _ in range(2):
        turn_left()

def turn_right():
    for _ in range(3):
        turn_left()

def reset_position():
    face_west()
    move_to_wall()
    turn_left()
    move_to_wall()
    face_east()

def face_west():
    while not_facing_west():
        turn_left()

def face_east():
    while not_facing_east():
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()

if __name__ == '__main__':
    main()