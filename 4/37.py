from cProfile import label
import json
import collections

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = "MS Gothic"

with open("neko-sent-splited.json", "r") as f:
    neko_data = json.load(f)

keyword = "猫"
base_list = []
for sent_data in neko_data:
    # てにをはばっか計算しても意味わからんので、助詞と補助記号を消してみる
    sent_data = filter(lambda x: x["pos"] != "助詞" and x["pos"] != "補助記号", sent_data)
    # 重複を消すためにいったんset
    _bases = set(list(map(lambda x: x["base"], sent_data)))
    if keyword in _bases:
        base_list += list(_bases)

c = collections.Counter(base_list)
c.pop(keyword)
top10 = c.most_common()[:10]

x = list(map(lambda x: x[0], top10))
y = list(map(lambda x: x[1], top10))

plt.bar(x, y)
plt.savefig("37.png")