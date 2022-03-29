from typing import List

from utils import Morph, Chunk

with open("ai.ja.txt.parsed", 'r') as f:
    parsed_text = f.read()

# 文ごとに分割
parsed_sents = parsed_text.split("EOS")
parsed_sents = filter(lambda x: len(x) > 1, parsed_sents)

sents_data = list(map(Chunk.from_cabocha_format, parsed_sents))
print(sents_data[1])