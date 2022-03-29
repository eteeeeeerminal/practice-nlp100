import sys
file_path = sys.argv[1]
with open(file_path, 'r') as f:
    lines = f.read().split("\n")

N = int(sys.argv[2])
print("\n".join(lines[len(lines)-N-1:]), end="")
