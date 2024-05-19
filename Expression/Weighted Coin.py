"""Question : Write a program which will flip a weighted coin.Coin flips are usually fair, but can be cheated -- 
              a weighted coin is a coin where the probability of heads isn't 50%. Your code should use the random 
              module to "flip" coin where the probability of heads is 70% and print the outcome (heads or tails).
"""

import random

HEADS_WEIGHT = 0.7

def main():
    if random.random() < HEADS_WEIGHT:
        print("Heads!")
    else:
        print("Tails!")

if __name__ == '__main__':
    main()