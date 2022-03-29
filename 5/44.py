from typing import List

from graphviz import Digraph

from utils import Morph, Chunk

with open("ai.ja.txt.parsed", 'r') as f:
    parsed_text = f.read()

# 文ごとに分割
parsed_sents = parsed_text.split("EOS")
parsed_sents = filter(lambda x: len(x) > 1, parsed_sents)

sents_data = list(map(Chunk.from_cabocha_format, parsed_sents))

def chunk_to_node_str(chunk_id: int, c: Chunk) -> str:
    return f"{chunk_id}: {c.to_str_without_sign()}"

def sent_to_dg(chunks: List[Chunk]) -> Digraph:
    dg = Digraph(format='png')

    for i, c in enumerate(chunks):
        dg.node(str(i), chunk_to_node_str(i, c))

    for i, c in enumerate(chunks):
        dg.edge(str(i), str(c.dst))

    return dg

sent_to_dg(sents_data[1]).view()
