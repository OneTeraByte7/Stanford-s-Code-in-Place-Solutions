"""QUestion : Write a program to print terms in the Fibonacci sequence up to a maximum value.In the 13th century, 
              the Italian mathematician Leonardo Fibonacci, as a way to explain the geometric growth of a population 
              of rabbits, devised a mathematical sequence that now bears his name. The first two terms in this sequence, 
              Fib(0) and Fib(1), are 0 and 1, and every subsequent term is the sum of the preceding two. 
              Thus, the first several terms in the Fibonacci sequence look like this:
                    Fib(0) = 0
                    Fib(1) = 1
                    Fib(2) = 1 = 0 + 1
                    Fib(3) = 2 = 1 + 1
                    Fib(4) = 3 = 1 + 2
                    Fib(5) = 5 = 2 + 3
"""

max_value = 10000

def main():
    currt = 0
    nextt = 1
    while currt <= max_value:
        print(currt)
        term_after = currt + nextt
        currt = nextt
        nextt = term_after

if __name__ == '__main__':
    main()