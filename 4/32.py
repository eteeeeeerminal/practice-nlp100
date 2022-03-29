import json

with open("neko.json", "r") as f:
    neko_data = json.load(f)

verb_list = filter(lambda x: x["pos"]=="動詞", neko_data)
verb_surfaces = map(lambda x: x["base"], verb_list)

print(*verb_surfaces)