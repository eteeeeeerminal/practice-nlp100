from typing import List

from utils import Morph, Chunk

with open("test.parsed", 'r') as f:
    parsed_text = f.read()

# 文ごとに分割
parsed_sents = parsed_text.split("EOS")
parsed_sents = filter(lambda x: len(x) > 1, parsed_sents)

sents_data = list(map(Chunk.from_cabocha_format, parsed_sents))

def extract_path(start_i: int, sent_data: List[Chunk]) -> str:
    path = [start_i]
    dst = sent_data[start_i].dst
    while dst != -1:
        path.append(dst)
        dst = sent_data[dst].dst

    path_node_strs = map(lambda i: sent_data[i].to_str_without_sign(), path)
    return " -> ".join(path_node_strs)

def extract_all_path_noun_to_root(sent_data: List[Chunk]) -> str:
    all_path = []
    for i, c in enumerate(sent_data):
        if not c.include_specific_pos("名詞"):
            continue
        path = extract_path(i, sent_data)
        all_path.append(path)

    return "\n".join(all_path)


print("\nEOS\n".join(map(lambda s: extract_all_path_noun_to_root(s), sents_data)))
