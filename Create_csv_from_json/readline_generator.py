from typing import Generator
import sys 

def ReadLineGenerator(file_path: str) -> Generator[str, None, str]:
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
    return "End of file reached."

def main() -> None:

    read_line_gen: Generator[str, None, str] = ReadLineGenerator('data_v2.csv')
    while True:
        try:
            lines = []            
            for i in range (0,5):
                line = next(read_line_gen)
                lines.append(line)
            print(lines)
            print("##########################")
        except StopIteration as e:
            print(e.value)  # Print the return value from the generator
            sys.exit()
        
    
if __name__ == "__main__":
    main()