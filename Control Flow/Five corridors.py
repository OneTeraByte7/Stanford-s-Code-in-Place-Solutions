"""Question : Get Karel to traverse each corridor (essentially, each row, until a wall blocks her path). 
              At the end of each corridor (they may be different lengths!), if a beeper isn't already there, put a beeper down. 
              Karel should end up at the beginning of the topmost corridor (highest row number), 
              and each corridor should have a beeper at the end of it
"""


from karel.stanfordkarel import *

def main():
    while front_is_clear():
        move()
    if no_beepers_present():
        put_beeper()

    for i in range(2):
        turn_left()
    while front_is_clear():
        move()
    for i in range(3):
        turn_left()
    move()

    for i in range(3):
        turn_left()
    while front_is_clear():
        move()
    if no_beepers_present():
        put_beeper()
    while front_is_clear():
        move()
    if no_beepers_present():
        put_beeper()

    for i in range(2):
        turn_left()
    while front_is_clear():
        move()
    for i in range(3):
        turn_left()
    move()

    for i in range(3):
        turn_left()
    while front_is_clear():
        move()
    if no_beepers_present():
        put_beeper()

    for i in range(2):
        turn_left()
    while front_is_clear():
        move()
    for i in range(3):
        turn_left()
    move()

    for i in range(3):
        turn_left()
    while front_is_clear():
        move()
    if no_beepers_present():
        put_beeper()

    for i in range(2):
        turn_left()
    while front_is_clear():
        move()
    for i in range(3):
        turn_left()
    move()
    
    for i in range(3):
        turn_left()
    while front_is_clear():
        move()
    if no_beepers_present():
        put_beeper()

    for i in range(2):
        turn_left()
    while front_is_clear():
        move()
    for i in range(2):
        turn_left()