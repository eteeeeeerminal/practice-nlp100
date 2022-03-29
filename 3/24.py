import re

with open("britain.txt") as f:
    data = f.read()

media_pattern = re.compile(r"([^\[\]\|\n\r\f]+\.[a-zA-Z][a-zA-Z\d]{2,3})")
r = media_pattern.findall(data)
r = filter(lambda x: "http" not in x, r)
r = filter(lambda x: "<" not in x and ">" not in x, r)
r = filter(lambda x: ".Corn" not in x, r)
media_pattern = re.compile(r"([^\[\]\|\n\r\f:]+\.[a-zA-Z][a-zA-Z\d]{2,3})")
r = media_pattern.findall("\n".join(r))
print("\n".join(r))