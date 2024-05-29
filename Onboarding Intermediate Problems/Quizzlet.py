"""Question : Write a program that loops over a dictionary of words and quizzes the user for their corresponding 
              Spanish translations, keeping count of how many the user gets correct! Separate each question and 
              answer with a blank line to help with visual clarity.
"""

def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    QUESTIONS = [
    ("What is the Spanish translation for hello?", "hola", "hello"),
    ("\nWhat is the Spanish translation for dog?", "perro", "dog"),
    ("\nWhat is the Spanish translation for cat?", "gato", "cat"),
    ("\nWhat is the Spanish translation for well?", "bien", "well"),
    ("\nWhat is the Spanish translation for us?", "nos", "us"),
    ("\nWhat is the Spanish translation for nothing?", "nada", "nothing "),
    ("\nWhat is the Spanish translation for house?", "casa", "house"),
    ("\nWhat is the Spanish translation for time?", "tiempo", "time"),

]
    score = 0
    for question, correct_answer, num in QUESTIONS:
        answer = input(f"{question}")
        if answer == correct_answer:
            print("That is correct!")
            score += 1
        else:
            print(f"That is incorrect, the Spanish translation for {num} is {correct_answer}.")
        
    print("\n"f"You got {score!r}/8 words correct, come study again soon!")

if __name__ == '__main__':
    main()