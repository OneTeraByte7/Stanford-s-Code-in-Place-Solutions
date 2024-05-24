"""Question : A haiku is a kind of poem which is comprised of 3 lines of 5, 7, and 5 syllables respectively. 
              Here's a famous haiku, “An Old Silent Pond” by Bashō:
              An old silent pond...  
              A frog jumps into the pond,  
              splash! Silence again.
"""

from graphics import Canvas

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
FIRST_LINE_LEFT_X = 50
FIRST_LINE_TOP_Y = 50
FONT_SIZE = 24

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    canvas.create_text(FIRST_LINE_LEFT_X, FIRST_LINE_TOP_Y,
        "An old silent pond...",
        color="blue",
        font="Courier",
        font_size=FONT_SIZE)

    canvas.create_text(FIRST_LINE_LEFT_X, FIRST_LINE_TOP_Y + FONT_SIZE, 
        "A frog jumps into the pond,", 
        color="blue", 
        font="Courier", 
        font_size=FONT_SIZE)

    canvas.create_text(FIRST_LINE_LEFT_X, FIRST_LINE_TOP_Y + 2 * FONT_SIZE, 
        "splash! Silence again.", 
        color="blue", 
        font="Courier", 
        font_size=FONT_SIZE)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()