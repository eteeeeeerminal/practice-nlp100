import sys

def save(file_path, data):
    with open(file_path, 'w') as f:
        f.write(data)

file_path = sys.argv[1]
with open(file_path, 'r') as f:
    lines = f.read().split("\n")

N = int(sys.argv[2])
line_n = len(lines)-1
block = int(line_n/N)
i_list = [block for _ in range(N)]
for i in range(line_n % block):
    i_list[i] += 1

i = 0
start = 0
for length in i_list:
    save(f"16/splited{i:0>2}", "\n".join(lines[start:start+length])+"\n")
    start += length
    i += 1
