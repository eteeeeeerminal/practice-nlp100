from typing import List

from utils import Morph, Chunk

with open("ai.ja.txt.parsed", 'r') as f:
    parsed_text = f.read()

# 文ごとに分割
parsed_sents = parsed_text.split("EOS")
parsed_sents = filter(lambda x: len(x) > 1, parsed_sents)

sents_data = list(map(Chunk.from_cabocha_format, parsed_sents))

def extract_predicate(c: Chunk) -> str:
    if len(c.morphs) == 1 and c.morphs[0].pos == "動詞":
        return c.morphs[0].base

    return ""

def extract_pp(c: Chunk) -> str:
    for m in reversed(c.morphs):
        if m.pos == "助詞":
            return m.base
    return ""

def is_target_kaku(c: Chunk) -> bool:
    if len(c.morphs) != 2:
        return False
    if c.morphs[0].pos == "名詞" and c.morphs[0].pos1 == "サ変接続" \
        and c.morphs[1].pos == "助詞" and c.morphs[1].base == "を":
        return True
    return False

predicate_and_kaku = []
for sent in sents_data:
    for i, c in enumerate(sent):
        verb = extract_predicate(c)
        if verb == "":
            continue

        srsc_c = list(map(lambda i: sent[i], c.srcs))
        kaku_list = list(filter(lambda c: c.include_specific_pos("助詞"), srsc_c))
        target_kaku_list = list(filter(lambda c: is_target_kaku(c), srsc_c))
        if not target_kaku_list:
            continue

        if target_kaku_list[-1] != srsc_c[-1]:
            continue

        verb = f"{target_kaku_list[-1].to_str_without_sign()}{verb}"
        kaku_list.remove(target_kaku_list[-1])

        kaku_list.sort(key=extract_pp)
        predicate_and_kaku.append((verb, kaku_list))

for p_k in predicate_and_kaku:
    kk = " ".join(map(extract_pp, p_k[1]))
    terms = " ".join(map(lambda x: x.to_str_without_sign(), p_k[1]))
    print(f"{p_k[0]}\t{kk}\t{terms}")