import json
import collections

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = "MS Gothic"

with open("neko.json", "r") as f:
    neko_data = json.load(f)

base_list = map(lambda x: x["base"], neko_data)
c = collections.Counter(base_list)
top10 = c.most_common()[:10]

x = list(map(lambda x: x[0], top10))
y = list(map(lambda x: x[1], top10))

plt.bar(x, y)
plt.savefig("36.png")