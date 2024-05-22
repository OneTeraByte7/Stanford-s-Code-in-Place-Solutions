"""Question : Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.")
              until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are 
              resilient, capable, and strong; this little Python program may be able to help!
"""

AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input()  
    while user_feedback != AFFIRMATION:  
        
        print("That was not the affirmation.")

        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    print("That's right! :)")

if __name__ == '__main__':
    main()
