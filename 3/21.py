import re

with open("britain.txt") as f:
    data_lines = f.readlines()

category_pattern = re.compile(r"\[\[Category:([^\|])+\|?([^\|])*\]\]")
data_lines = list(filter(lambda x: category_pattern.match(x) is not None, data_lines))

print("".join(data_lines))
