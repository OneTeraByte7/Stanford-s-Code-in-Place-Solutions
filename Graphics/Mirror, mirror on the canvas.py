"""Question : The line represents a "mirror" -- your job is to draw a blue rectangle on the other side of the canvas which is the mirror 
              image of the red rectangle. (That is, the left edge of the blue rectangle is the same distance from the line in the middle 
              as the right edge of the red rectangle, and the left edge of the red rectangle is the same distance from the left edge of 
              the canvas as the right edge of the blue rectangle is from the right edge of the canvas!) 
"""
from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    
    canvas.create_line(
        CANVAS_WIDTH // 2, 
        0, 
        CANVAS_WIDTH // 2, 
        CANVAS_HEIGHT)
    
    
    rect_left_x = 20
    rect_top_y = 50
    rect_width = 100
    rect_height = 200
    canvas.create_rectangle(
        rect_left_x, 
        rect_top_y, 
        rect_left_x + rect_width, 
        rect_top_y + rect_height, 
        'red')
    
    canvas.create_rectangle(
        CANVAS_WIDTH - rect_left_x - rect_width,
        rect_top_y,
        CANVAS_WIDTH - rect_left_x,
        rect_top_y + rect_height,
        'blue'
    )


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()