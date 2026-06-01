
from typing import Generator

def fibonacci_generator() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, (a + b)


def main () -> None: 
    fib_gen: Generator[int, None, None] = fibonacci_generator()
    n: int =  5
    line_break: str = "#" *  20 
    loop_numer : int = n 
    while True:
        inputV = input (f"Press Enter to get the next Fibonacci number or give number (default {n}): ")
        if inputV and inputV.isdigit():
            loop_numer = int(inputV) 
        print (line_break)
        for i in range (loop_numer):
            print (f'{next(fib_gen)}')   
        print (line_break)

if __name__ == "__main__":
    main()  