import json
import collections

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = "MS Gothic"

with open("neko.json", "r") as f:
    neko_data = json.load(f)

base_list = map(lambda x: x["base"], neko_data)
ranked_words = collections.Counter(base_list).most_common()

x = range(1, len(ranked_words)+1)
y = list(map(lambda x: x[1], ranked_words))

plt.plot(x, y)
plt.xscale("log")
plt.yscale("log")
plt.savefig("39.png")
