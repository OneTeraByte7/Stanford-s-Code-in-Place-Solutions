"""Question : You may have noticed that when we make graphical objects, we can add color to them by adding an optional color argument 
              when we make a shape. For example, the below code would make a red circle.
              canvas.create_oval(x1, y1, x2, y2, color="red")
"""

from graphics import Canvas
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    canvas.create_oval(CANVAS_WIDTH/2 - 75, 225, CANVAS_WIDTH/2 + 75, 375, color="#FFFFFF")
    
    canvas.create_oval(25, 25, 175, 175, color="#990000")
    
    # For plus sign
    canvas.create_line(190, 100, 210, 100)
    canvas.create_line(200, 90, 200, 110)
    
    # Draw a blue circle
    canvas.create_oval(CANVAS_WIDTH/2 + 25, 25, CANVAS_WIDTH/2 + 175, 175, color="#000099")
    
    # Draw an arrow
    canvas.create_line(200, 170, 200, 210)
    canvas.create_line(200, 210, 190, 190)
    canvas.create_line(200, 210, 210, 190)

    #For puprle circle
    canvas.create_oval(CANVAS_WIDTH/4 + 20, 225, CANVAS_WIDTH/4 + 180, 375, color="#A020F0")
    

if __name__ == '__main__':
    main()