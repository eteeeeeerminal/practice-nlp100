import json

with open("neko.json", "r") as f:
    neko_data = json.load(f)

noun_list = []
one_noun = []
for token in neko_data:
    if token["pos"] == "名詞":
        one_noun.append(token)
    else:
        if one_noun:
            noun_list.append(one_noun)
        one_noun = []

for noun in noun_list:
    print(*map(lambda x: x["surface"], noun))