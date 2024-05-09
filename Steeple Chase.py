"""Question : The program that Mehran works through in assignment 2. 
              This program allows Karel to run a "Steeple Chase" (like a hurdles race, but with arbitrarily large hurdles) where: 
              Karel starts at position (1, 1), facing East (aka right). 
              The steeple chase is guaranteed to be 9 columns long. 
              There can be arbitrarily many hurdles that can be of arbitrary size, located between any two corners in the world. 
              Karel should "jump" each hurdle one at a time. For example, if you were to execute the SteepleChase program, 
              you would see something like the following before-and-after diagram
"""

from karel.stanfordkarel import *


def main():
    for i in range(8):
        if front_is_clear():  
            move()
        else: 
            jump_hurdle()


def jump_hurdle():
    ascend_hurdle()
    move()
    descend_hurdle()


def ascend_hurdle():
    turn_left()  
    
    while right_is_blocked():
        move()
        
    turn_right()  


def descend_hurdle():
    turn_right()  
    move_to_wall()  
    turn_left()  


def move_to_wall():
    while front_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()