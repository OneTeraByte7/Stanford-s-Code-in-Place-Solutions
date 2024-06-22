"""Question : To familiarize yourself with this concept, we have already provided three different doors and a function 
              to open them. All we need to know is which door to open! Fill out the get_door_clicked(...) which checks 
            to see which door to open based on where you click the mouse.
"""

from graphics import Canvas
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
DOOR_WIDTH = CANVAS_WIDTH * 0.25  # Each door takes up 1/4 of of the canvas's width
DOOR_HEIGHT = CANVAS_HEIGHT * 0.4 # Each door takes up 2/5 of the canvas's height
DOOR_GAP = (CANVAS_WIDTH - (3 * DOOR_WIDTH)) // 4

def get_door_clicked(canvas):
    x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
    overlapping = canvas.find_overlapping(x, y, x, y)
    if len(overlapping) > 0:  # Checks to see if there are any overlapping shapes
        return overlapping[0]
    
    return None

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    door_1 = make_door(canvas, DOOR_GAP, "1", color="red")
    door_2 = make_door(canvas, DOOR_WIDTH + 2 * DOOR_GAP, "2", color="blue")
    door_3 = make_door(canvas, DOOR_WIDTH * 2 + 3 * DOOR_GAP, "3", color="yellow")
    
    while True:
        click = canvas.get_last_click()
        if click:
            door_clicked = get_door_clicked(canvas)
            
            if door_clicked:
                open_door(canvas, canvas.get_left_x(door_clicked))

def make_door(canvas, left_x, door_number, color="black"):
    door = canvas.create_rectangle(left_x,
                                   CANVAS_HEIGHT - DOOR_HEIGHT,
                                   left_x + DOOR_WIDTH,
                                   CANVAS_HEIGHT,
                                   color=color)
    
    font_size = 24
    door_text = canvas.create_text(left_x + DOOR_WIDTH/2 - font_size/4, 
                                   CANVAS_HEIGHT - DOOR_HEIGHT - font_size,
                                   text=str(door_number),
                                   font_size=font_size)
    
    return door

def open_door(canvas, left_x):
    door_frame_size = DOOR_WIDTH * 0.15
    canvas.create_rectangle(left_x + door_frame_size,
                            CANVAS_HEIGHT - DOOR_HEIGHT + door_frame_size,
                            left_x + DOOR_WIDTH - door_frame_size,
                            CANVAS_HEIGHT,
                            color="white")


if __name__ == '__main__':
    main()