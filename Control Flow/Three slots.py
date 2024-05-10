

from karel.stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def main():
    
    turn_right()
    move()
    put_beeper()
    for j in range(2):
        turn_left()
    move()
    for k in range(3):
        turn_left()
    move()

    turn_right()
    move()
    put_beeper()
    for j in range(2):
        turn_left()
    move()
    for k in range(3):
        turn_left()
    move()

    turn_right()
    move()
    put_beeper()
    for j in range(2):
        turn_left()
    move()
    for k in range(3):
        turn_left()
    
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()