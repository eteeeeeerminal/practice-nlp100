from json import load
from typing import List

from utils import Morph, Chunk

with open("ai.ja.txt.parsed", 'r') as f:
    parsed_text = f.read()

# 文ごとに分割
parsed_sents = parsed_text.split("EOS")
parsed_sents = filter(lambda x: len(x) > 1, parsed_sents)

sents_data = list(map(Chunk.from_cabocha_format, parsed_sents))

def print_chunks(chunks: List[Chunk]):
    for c in chunks:
        if c.dst == -1:
            continue
        if c.include_specific_pos("名詞") and chunks[c.dst].include_specific_pos("動詞"):
            print(f"{c.to_str_without_sign()}\t{chunks[c.dst].to_str_without_sign()}")

    print("EOS")

list(map(print_chunks, sents_data))