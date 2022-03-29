def load(file_path) -> str:
    with open(file_path, 'r') as f:
        return f.read()

def save(file_path, data):
    with open(file_path, 'w') as f:
        f.write(data)

col1 = load("col1.txt").split("\n")
col2 = load("col2.txt").split("\n")

lines = ["\t".join((c1, c2)) for c1, c2 in zip(col1, col2) if c1]
save("col1-2.txt", "\n".join(lines)+"\n")