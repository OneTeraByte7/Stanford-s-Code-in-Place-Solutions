"""Question : Write a program that asks the user to enter a sequence of "non-decreasing" numbers one at a time. 
              Numbers are non-decreasing if each number is greater than or equal to the last.When the user enters 
              a number which is smaller than their previously entered value, the program is over. Tell the user 
              how long their sequence was.
"""

def main():
  numbers = []

  while True:
    num = float(input("Enter num: "))

    if len(numbers) > 0 and num < numbers[-1]:
        break

    numbers.append(num)
  print("Thanks for playing! \nSequence length:",len(numbers))

if __name__ == "__main__":
  main()