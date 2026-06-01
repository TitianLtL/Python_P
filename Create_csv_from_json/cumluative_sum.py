from typing import Generator

def cumulative_sum() -> Generator[float, float, None]:
    total: float = 0.0
    while True:
        value: float = yield total
        total += value
        
        
def main() -> None:
    cum_sum_gen: Generator[float, float, None] = cumulative_sum()
    next(cum_sum_gen)  # Start the generator
    while True:
        try:
            user_input: str = input("Enter a number to add to the cumulative sum (or 'exit' to quit): ")
            value: float = float(user_input)
            current_sum: float = cum_sum_gen.send(value)
            print(f"Cumulative Sum: {current_sum}")
        except ValueError:
            print("Please enter a valid number or 'exit' to quit.")

if __name__ == "__main__":
    main()        