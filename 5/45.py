from typing import List

from utils import Morph, Chunk

with open("ai.ja.txt.parsed", 'r') as f:
    parsed_text = f.read()

# 文ごとに分割
parsed_sents = parsed_text.split("EOS")
parsed_sents = filter(lambda x: len(x) > 1, parsed_sents)

sents_data = list(map(Chunk.from_cabocha_format, parsed_sents))

def extract_predicate(c: Chunk) -> str:
    for m in c.morphs:
        if m.pos == "動詞":
            return m.base

    return ""

def extract_pp(c: Chunk) -> str:
    for m in reversed(c.morphs):
        if m.pos == "助詞":
            return m.base
    return ""

predicate_and_kaku = []
for sent in sents_data:
    for c in sent:
        verb = extract_predicate(c)
        if verb == "":
            continue

        kaku_list = list(filter(lambda x:x,
            map(lambda i: extract_pp(sent[i]), c.srcs)
        ))
        kaku_list.sort()

        predicate_and_kaku.append((verb, kaku_list))

for p_k in predicate_and_kaku:
    kk = " ".join(p_k[1])
    print(f"{p_k[0]}\t{kk}")