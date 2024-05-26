from graphics import Canvas
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = CANVAS_WIDTH
N_ROWS = 8
N_COLS = N_ROWS
SIZE = CANVAS_WIDTH / N_ROWS

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    for r in range(N_ROWS):
        for c in range(N_COLS):
            draw_square(canvas, r, c)
            
def draw_square(canvas, r, c):
    
    print(r, c)
    
    color = get_color(r, c)  # Get the square's color based on the row and column
    x = c * SIZE  # Calculate left_x
    y = r * SIZE  # Calculate top_y
    end_x = x + SIZE  # Calculate right_x
    end_y = y + SIZE  # Calculate bottom_y
    
    canvas.create_rectangle(x, y, end_x, end_y, color, 'black')  # Draw the rectangle
            
        
def get_color(r, c):
    if is_even(r + c):
        return "green"
    else:
        return "beige"
        
def is_even(value):
    return value % 2 == 0

if __name__ == '__main__':
    main()