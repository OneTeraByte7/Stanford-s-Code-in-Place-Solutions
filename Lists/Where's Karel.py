"""Question : Fill in the function find_karel(roster) which takes in a list, roster, and prints "Karel is here!" if 'karel' is an element in roster, 
              or prints "Karel isn't here." if 'karel' isn't an element in roster. You can assume all elements in roster will be lowercase.
"""

def find_karel(roster):
    if 'karel' in roster:
        print("Karel is here!")
    else:
        print("Karel isn't here.")
def get_list():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem.lower())
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    roster = get_list()
    find_karel(roster)

if __name__ == '__main__':
    main()