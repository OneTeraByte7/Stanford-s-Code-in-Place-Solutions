"""Question : Draw a square which has dimensions THIS_BIG by THIS_BIG (each side of the square is THIS_BIG pixels long) 
              centered at CENTER_X, CENTER_Y.
"""

from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
THIS_BIG = 144
CENTER_X = 160
CENTER_Y = 160

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_rectangle(
		CENTER_X - THIS_BIG / 2,  
		CENTER_Y - THIS_BIG / 2,  
		CENTER_X + THIS_BIG / 2,  
		CENTER_Y + THIS_BIG / 2   
	)


if __name__ == '__main__':
    main()