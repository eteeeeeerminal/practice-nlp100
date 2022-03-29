import re

with open("britain.txt") as f:
    data_lines = f.readlines()

category_pattern = re.compile(r"\[\[Category:([^\|]+)(\|[^\|]*)?\]\]")
categories = filter(lambda x: category_pattern.match(x) is not None, data_lines)
categories = list(map(lambda x: category_pattern.match(x)[1], categories))

print("\n".join(categories))

