import json

with open("neko.json", "r") as f:
    neko_data = json.load(f)

b_of_a = []
data_len = len(neko_data)
for i in range(data_len-3):
    if neko_data[i]["pos"] == "名詞" \
        and neko_data[i+1]["surface"] == "の" \
        and neko_data[i+2]["pos"] == "名詞":

        b_of_a.append(neko_data[i:i+3])

for x in b_of_a:
    print(x[0]["surface"], x[1]["surface"], x[2]["surface"])