"""Question : Karel will be in a single row world with beepers in some positions. 
              Karel should "invert" the pattern of the row -- pick beepers from the spots with beepers 
              and place beepers from the empty spots -- and end facing East in the rightmost position. 
              There will be no more than 1 beeper in each spot. Be sure to invert the positions Karel starts and ends on!
"""

from karel.stanfordkarel import *

def main():
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
            move()

        else:
            pick_beeper()
            move()
    if no_beepers_present():
        put_beeper()
    else:
        pick_beeper()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()