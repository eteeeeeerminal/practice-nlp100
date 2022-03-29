import sys
file_path = sys.argv[1]
with open(file_path, 'r') as f:
    file_data = f.read()

file_data = [
    [elm for elm in line.split("\t")]
    for line in file_data.split("\n") if line
]

sorted_list = sorted(list(set(map(lambda x: x[0], file_data))))
print("\n".join(sorted_list))