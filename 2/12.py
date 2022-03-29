import sys
file_path = sys.argv[1]
with open(file_path, 'r') as f:
    file_data = f.read()

file_data = [
    [elm for elm in line.split("\t")]
    for line in file_data.split("\n") if line
]

def save(file_path, data):
    with open(file_path, 'w') as f:
        f.write(data)

# 1列目をcol1.txtに
save("col1.txt", "\n".join(map(lambda x: x[0], file_data))+"\n")

# 2列目をcol2.txtに
save("col2.txt", "\n".join(map(lambda x: x[1], file_data))+"\n")
