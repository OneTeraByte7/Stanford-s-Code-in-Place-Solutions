""" Question : Write a program that prints out the calls for a spaceship that is about to launch. 
               Countdown from 10 to 1 and then output Liftoff!


"""

def main():
    for i in range(10, 0, -1):
        print(i)
    
    print("Liftoff!")

# Python file to call the main() function.
if __name__ == '__main__':
    main()