"""Question : Karel has picked up a new hobby: doing puzzles! Karel is trying to complete this puzzle made up of beepers. 
    When complete the puzzle should look like this:Karel is almost done but not finished yet. 
    Below is the current state of Karel's world. The beeper in the bottom most row represents the last piece of the puzzle!
    Write a program which will get Karel to pick up the last piece, put it in place, and move Karel back to the bottom left corner 
    of the world facing East so she can admire the completed puzzle.
    """
    
from karel.stanfordkarel import *




def main():
    move()
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    move()
    put_beeper()
    for i in range(2):
        turn_left()
    move()
    move()
    for i in range(3):
        turn_left()
    for i in range(3):
        move()
    for i in range(2):
        turn_left()
    


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()