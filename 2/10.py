import sys

file_path = sys.argv[1]
with open(file_path, 'r') as f:
    file_data = f.read()

def count_lines(text:str) -> int:
    return len(text.split("\n"))-1

print(count_lines(file_data))