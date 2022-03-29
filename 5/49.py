from typing import List

from utils import Morph, Chunk

with open("test.parsed", 'r') as f:
    parsed_text = f.read()

# 文ごとに分割
parsed_sents = parsed_text.split("EOS")
parsed_sents = filter(lambda x: len(x) > 1, parsed_sents)

sents_data = list(map(Chunk.from_cabocha_format, parsed_sents))

def extract_path(start_i: int, sent_data: List[Chunk]) -> List[int]:
    path = [start_i]
    dst = sent_data[start_i].dst
    while dst != -1:
        path.append(dst)
        dst = sent_data[dst].dst

    return path

def extract_all_path_noun_to_root(sent_data: List[Chunk]) -> List[List[int]]:
    all_path = []
    for i, c in enumerate(sent_data):
        if not c.include_specific_pos("名詞"):
            continue
        path = extract_path(i, sent_data)
        all_path.append(path)

    return all_path

def noun_path_str(sent_data: List[Chunk], path: List[int], tail_i: int) -> str:
    noun_chunk = [sent_data[path[0]].to_str_replace_specific_pos("名詞", "Y"), ]
    other_chunk_strs = list(map(lambda i: sent_data[i].to_str_without_sign(), path[1:tail_i]))
    return " -> ".join(noun_chunk+other_chunk_strs)

def find_all_noun_pair_path(sent_data: List[Chunk]) -> str:
    all_path = extract_all_path_noun_to_root(sent_data)

    all_path_strs = []
    for i, p in enumerate(all_path):
        # for文の中まるまる関数にくくりだすだけでも、一段ネストが下がるのでやったほうがいい
        explored = set()

        # 単純な経路を見つける
        simple_p_str = sent_data[p[0]].to_str_replace_specific_pos("名詞", "X")
        for k in p[1:]:
            c: Chunk = sent_data[k]
            if c.include_specific_pos("名詞"):
                explored.add(k)
                hoge = c.to_str_replace_specific_pos("名詞", "Y")
                all_path_strs.append(" -> ".join((simple_p_str, hoge)))

            simple_p_str = " -> ".join((simple_p_str, c.to_str_without_sign()))

        # 複雑な経路を見つける
        complex_p_str = sent_data[p[0]].to_str_replace_specific_pos("名詞", "X")
        frontier = all_path[i+1:]
        for k in p[1:]:
            c: Chunk = sent_data[k]

            for p2 in frontier:
                try:
                    fork_p = p2.index(k)
                except:
                    continue

                if p2[0] in explored:
                    continue

                complex_p2_str = noun_path_str(sent_data, p2, fork_p)

                all_path_strs.append(
                    " | ".join((
                        complex_p_str, complex_p2_str, c.to_str_without_sign()
                    ))
                )

            complex_p_str = " -> ".join((complex_p_str, c.to_str_without_sign()))

    return "\n".join(all_path_strs)


print("\nEOS\n".join(map(lambda s: find_all_noun_pair_path(s), sents_data)))
