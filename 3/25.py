import re

with open("britain.txt") as f:
    data = f.read()

# 基礎情報の抜き出し
base_info_pattern = re.compile(r"\{\{基礎情報 国([\s\S]+)\n\}\}")
base_info = base_info_pattern.search(data)[1]

# 各フィールド抜き出し
fields_text = base_info.split("\n|")

fields_pattern = re.compile(r"([^=]+)\s*=\s*([\s\S]+)")
fields_match = [fields_pattern.match(f) for f in fields_text]

# dictに箱詰め
base_info_dict = {}
for f_match in fields_match:
    if f_match is None:
        continue
    base_info_dict[f_match[1]] = f_match[2]


print(base_info_dict)
