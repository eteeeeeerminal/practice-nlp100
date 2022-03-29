from re import L
import sys
from collections import Counter

file_path = sys.argv[1]
with open(file_path, 'r') as f:
    file_data = f.read()

file_data = [
    [elm for elm in line.split("\t")]
    for line in file_data.split("\n") if line
]

col1_counter = Counter(map(lambda x: x[0], file_data)).most_common()
for data in col1_counter:
    print(f"    {data[1]: >3} {data[0]}")