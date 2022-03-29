import json
import collections

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = "MS Gothic"

with open("neko.json", "r") as f:
    neko_data = json.load(f)

base_list = map(lambda x: x["base"], neko_data)
c = collections.Counter(base_list)

tf = list(map(lambda x: x[1], c.most_common()[:100]))

plt.hist(tf, bins=len(set(tf)))
plt.savefig("38.png")
