"""Question : Fill out the function count_even(lst) which first populates a list by prompting the user for integers 
              until they press enter (please use the prompt "Enter an integer or press enter to stop: "), 
              and then prints the number of even numbers in the list. 
"""

def count_even(lst):
    cnt = 0
    for num in lst:
        if num % 2 == 0:
            cnt += 1
    #OR
    #for i in range(len(lst)):
    #     num = lst[i]
    #     if num % 2 == 0:
    #          cnt += 1

    print(cnt)

def get_list_of_int():
    lst = []
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("Enter an integer or press enter to stop: ")

    return lst

def main():
    lst = get_list_of_int()
    count_even(lst)
    
if __name__ == '__main__':
    main()