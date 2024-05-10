"""Question : Write a program which will move Karel up and over the archway, so Karel ends up on the right side of it facing East"""

from karel.stanfordkarel import *

def main():
    turn_left()
    while front_is_clear():
        move()
    for i in range(3):
        turn_left()

    while front_is_clear():
        move()
    for i in range(3):
        turn_left()

    while front_is_clear():
        move()

    
    turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()