"""Question : A Zebra crossing, or crosswalk, is a series of black and white stripes across a road indicating where a pedestrian can cross
              In the interests of road safety, Karel has been asked to make Zebra crossings. In the world of Karel, a Zebra crossing is defined 
              as a pattern beginning with a 2-square wide column of beepers, followed by repeating pairs of a 3-square wide gap and a 2-square 
              wide column of beepers. 
"""

from karel.stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()

def beeper_stripe():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
        
def draws_stripe():
    turn_left()
    beeper_stripe()
    turn_right()
    move()
    turn_right()
    beeper_stripe()
    turn_left()

def main():
    draws_stripe()
    while front_is_clear():
        for i in range(4):
            move()
        draws_stripe()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()