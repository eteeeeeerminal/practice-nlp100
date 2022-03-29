import re
from typing import AnyStr

with open("britain.txt") as f:
    data_lines = f.readlines()

section_patterns = []
for i in range(5):
    equal_pattern = "===" + "{" + f"{i},{i}" + "}"
    regex_text = equal_pattern + "\s*([^=]+)\s*" + equal_pattern
    section_patterns.append(re.compile(regex_text))

def regex_section(section_patterns, line: str):
    for i, sp in enumerate(section_patterns):
        m = sp.match(line)
        if m:
            print(f"{i+1} {m[1]}")

for line in data_lines:
    regex_section(section_patterns, line)