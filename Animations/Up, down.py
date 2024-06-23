"""Question: Write code to make the square square move up until its upper edge is at or past UPPER_BOUND and then 
             down until its bottom edge is at or past LOWER_BOUND.
"""

from graphics import Canvas
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SQUARE_SIZE = 40
VELOCITY = 2
DELAY = 0.01
UPPER_BOUND = 100
LOWER_BOUND = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    start_x = CANVAS_HEIGHT / 2 - SQUARE_SIZE / 2
    start_y = CANVAS_HEIGHT / 2 - SQUARE_SIZE / 2
    square = canvas.create_rectangle(start_x, start_y,
                    start_x + SQUARE_SIZE,
                    start_y + SQUARE_SIZE)

    #up                
    while (start_y > UPPER_BOUND):
        start_y -= VELOCITY
        canvas.moveto(square, start_x, start_y)
        time.sleep(DELAY)
    
    # down
    while (start_y + SQUARE_SIZE < LOWER_BOUND):
        start_y += VELOCITY
        canvas.moveto(square, start_x, start_y)
        time.sleep(DELAY)


if __name__ == '__main__':
    main()
