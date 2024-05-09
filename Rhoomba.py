"""Question : Pick up every beeper in the world. At the end Karel should be facing East at the top right corner of a world with zero beepers left."""


from karel.stanfordkarel import *

def main():
   
    while left_is_clear(): 
        clear_row()
        reset_to_next_row()
   
    clear_row()
    
    
def clear_row():
    
    while front_is_clear():  
        clear_corner()  
        move()
    
    clear_corner()
    
    
def clear_corner():
   
    if beepers_present():
        pick_beeper()
        
        
def reset_to_next_row():
    turn_around()
    move_to_wall()
    turn_right()
    move()
    turn_right()
    

def move_to_wall():
    while front_is_clear():
        move()
    
    
def turn_right():
    for i in range(3):
        turn_left()
        
        
def turn_around():
    turn_left()
    turn_left()




if __name__ == '__main__':
    main()
