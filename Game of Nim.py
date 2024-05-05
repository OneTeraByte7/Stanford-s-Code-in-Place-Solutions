"""Qustion : Start with 20 stones. Repeat the process of removing stones and printing out how many stones are left until there are zero.
            Don't worry about whose turn it is. Don't worry about making sure only one or two stones are removed. 
            Use the method int(input(msg)) which prints msg and waits for the user to enter a number and casts it to an integer. 
            Add an empty print() function between removals to make  tracking turns easier.
    """


start = 20

def main():
    Milestone1()
    Milestone2()
    Milestone3()

def Milestone1():
    remaining = start
    while remaining > 0:
        print("There are" + str(remaining) +"stones left.")
        take = int(input("Would you like to remove 1 or 2 stones"))
        remaining -= take
    
def Milestone2():
    remaining = start
    turn = 1
    while remaining > 0:
        print("There are" + str(remaining) +"stones left.")
        take = int(input("Player" + str(turn) + ", would you like to remove 1 or 2 stones"))
        remaining -= take

        if turn == 1:
            turn = 2
        else:
            turn = 1

def Milestone3():
    remaining = start
    turn = 1
    while remaining > 0:
        print("There are" + str(remaining) +"stones left.")
        take = int(input("Player" + str(turn) + ", would you like to remove 1 or 2 stones"))
        while take < 1 or take > 2:
            take = int(input("Please enter 1 or 2: "))
        remaining -= take

        if turn == 1:
            turn = 2
        else:
            turn = 1

    print("Player" + str(turn) + " wins!")