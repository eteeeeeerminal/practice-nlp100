import json

# 形態素解析の結果を読み込み
with open("neko.txt.mecab", 'r') as f:
    mecab_result_row = f.read()

# できれば返り値はdataclassとかにしたいけど後回し
def load_mecab_result_dict(line: str):
    surface, others  = line.split("\t")
    others = others.split(",")
    base = others[7] if len(others) > 7 else surface
    base = base if base else surface
    pos = others[0]
    pos1 = others[1]

    return {
        "surface": surface,
        "base": base,
        "pos": pos,
        "pos1": pos1
    }

# tab のない行はハズレ
data = [load_mecab_result_dict(l) for l in mecab_result_row.split("\n") if "\t" in l]

with open("neko.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
