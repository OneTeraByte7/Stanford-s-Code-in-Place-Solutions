"""Question : Your task is simple: no matter the size of the world, Karel should fill it with beepers.
              Note that Karel's final position does matter. Karel should be in the top-right corner facing right. 
              You can assume that Karel always starts in the bottom-left corner, facing right. 
              Your code needs to work on more than just a 5x5 world. For example if you run your solution on the 3x4 world
    """
    
from karel.stanfordkarel import *

def main():
    while left_is_clear():
          fill_the_row()
          reset_to_next_row()
    fill_the_row()
    
def fill_the_row():
    put_beeper()
    while front_is_clear():
          move()
          put_beeper()
          
def reset_to_next_row():
    turn_around()
    while front_is_clear():
          move()
    turn_right()
    move()
    turn_right()
    
def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()