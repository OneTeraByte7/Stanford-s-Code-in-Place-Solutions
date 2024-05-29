"""Question : Write a program that has Karel draw four small waves. Each wave is a triangle made up of three beepers. 
              There is a gap between each wave.his is the state of Karel's world when Karel starts:
"""

from karel.stanfordkarel import *

def turn_back():
    for i in range(2):
        turn_left()

def main():
    while front_is_clear():
        put_beeper()
        move()
        put_beeper()
        turn_left()
        move()
        put_beeper()
        turn_back()
        move()
        turn_left()
        if front_is_clear():
            for i in range(2):
                move()
        
if __name__ == '__main__':
    main()