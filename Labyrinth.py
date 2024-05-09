"""Question : According to Wikipedia, "maze refers to a complex branching multicursal puzzle with choices of path and direction, 
              while a unicursal labyrinth has only a single path to the center. A labyrinth in this sense has an unambiguous route 
              to the center and back and presents no navigational challenge."
              We've designed a labyrinth Karel world -- Karel will start in one dead end, and so long as Karel moves forwards through the labyrinth, Karel will eventually end up at the other dead end
"""

from karel.stanfordkarel import *

def main():
    while front_is_clear():
        move_to_wall()
        find_direction()
def find_direction():
    if left_is_clear():
        turn_left()
    if right_is_clear():
        turn_right()

def turn_right():
    for i in range(3):
        turn_left()
    
def move_to_wall():
    while front_is_clear():
        move()

   

if __name__ == '__main__':
    main()