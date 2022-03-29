import json

import MeCab
import unidic

with open("neko.txt", 'r') as f:
    novel_text = f.read()

tagger = MeCab.Tagger()

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

def tag_line(line_row: str):
    result = str(tagger.parse(line_row))
    # tab のない行はハズレ
    return [load_mecab_result_dict(l) for l in result.split("\n") if "\t" in l]

data = [tag_line(r) for r in novel_text.split("\n")]
data = list(filter(lambda x: x, data))

with open("neko-sent-splited.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
