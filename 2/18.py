import sys
file_path = sys.argv[1]
with open(file_path, 'r') as f:
    file_data = f.read()

file_data = [
    [elm for elm in line.split("\t")]
    for line in file_data.split("\n") if line
]

sorted_data = sorted(file_data, key=lambda x: int(x[2]), reverse=True)
for line in sorted_data:
    print("\t".join(line))