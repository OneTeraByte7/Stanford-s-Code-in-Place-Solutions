from karel.stanfordkarel import *

# this program executes in a special function called main
def main():
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    for i in range(3):
        turn_left()
    move()
    put_beeper()
    move()

if __name__ == '__main__':
    main()
