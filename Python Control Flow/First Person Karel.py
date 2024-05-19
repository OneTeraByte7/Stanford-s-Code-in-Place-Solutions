"""Question : Write a program that lets you play Karel in a rectangular world (moving and turning left and not walking off of the world, 
              all that good stuff)!Have you ever wanted to be Karel, wandering about a nice rectangular world, not a worry in the world, 
              just moving and turning left whenever you'd like? You can emulate this feeling by writing a console-based first person Karel 
              program! For simplicity, assume that beepers and painting are out of the question, and the world has no walls. 
"""


N_COLS = 3
N_ROWS = 3

def main():
    print("Welcome to first person Karel! You're at row 1, column 1, facing East (facing column " + str(N_COLS) + ")")
    
    
    facing_direction = 'East'  
    curr_col = 1 
    curr_row = 1  
    
    action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
    
    while action != '':  
        if action == "move":
            if facing_direction == 'East' and curr_col < N_COLS:
                curr_col += 1
                print("You moved one step forward and now you're at row " + str(curr_row) + " column " + str(curr_col) + ".")
            
            elif facing_direction == 'West' and curr_col > 1:
                curr_col -= 1
                print("You moved one step forward and now you're at row " + str(curr_row) + " column " + str(curr_col) + ".")
            
            elif facing_direction == 'North' and curr_row < N_ROWS:
                curr_row += 1
                print("You moved one step forward and now you're at row " + str(curr_row) + " column " + str(curr_col) + ".")
            
            elif facing_direction == 'South' and curr_row > 1:
                curr_row -= 1
                print("You moved one step forward and now you're at row " + str(curr_row) + " column " + str(curr_col) + ".")
            
            else:
                print("You can't move forward!")

        elif action == "turn left":
            if facing_direction == 'East':
                facing_direction = 'North'
            
            elif facing_direction == 'North':
                facing_direction = 'West'
            
            elif facing_direction == 'West':
                facing_direction = 'South'
            
            elif facing_direction == 'South':
                facing_direction = 'East'
            print("You turned left and are now facing " + facing_direction + ".")

        action = input("What would you like to do? You can move and turn left. Press enter to finish. ")

    print("You've ended up at row " + str(curr_row) + " and column " + str(curr_col) + " facing " + facing_direction + ".")

if __name__ == '__main__':
    main()