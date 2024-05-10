"""Question : Make Karel paint a rainbow! Karel will start in the left corner of a world with 1 row and 6 columns,
              Karel should paint the squares with, in order: the colors "red" , "orange", "yellow", "green", and "blue", 
              and then Karel should move to end in the rightmost spot. 
"""

from karel.stanfordkarel import *

def main():
    paint_corner('red')
    move()
    paint_corner('orange')
    move()
    paint_corner('yellow')
    move()
    paint_corner('green')
    move()
    paint_corner('blue')
    move()
    
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()