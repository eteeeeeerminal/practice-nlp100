import sys
file_path = sys.argv[1]
with open(file_path, 'r') as f:
    file_data = f.read()

def replace_tab2space(text: str) -> str:
    return text.replace("\t", " ")

print(replace_tab2space(file_data), end="")