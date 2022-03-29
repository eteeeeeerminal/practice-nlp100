import re
from typing import List
from dataclasses import dataclass

@dataclass
class Morph:
    surface: str
    base: str
    pos: str
    pos1: str

    def from_mecab_format(data_text: str):
        surface, others  = data_text.split("\t")
        others = others.split(",")
        base = others[6]
        if len(base) > 2 and base != surface and base == "*":
            base = surface
        pos = others[0]
        pos1 = others[1]

        return Morph(surface, base, pos, pos1)

    def __repr__(self) -> str:
        return self.surface

    def from_sent(parsed_sent_text: str):
        morphs_text = parsed_sent_text.split("\n")

        # 形態素解析の結果の取り出し
        morph_list = []
        for morph in morphs_text:
            if "\t" not in morph:
                continue
            morph_list.append(Morph.from_mecab_format(morph))

        return morph_list

@dataclass
class Chunk:
    morphs: List[Morph]
    dst: int
    srcs: List[int]

    # Chunk 1つ返す
    def from_chunk_text(parsed_chunk_text: str):
        lines = parsed_chunk_text.split("\n")
        chunk_info_match = re.search(r"(-?[\d]+)D", lines[0])
        dst = int(chunk_info_match[1])
        morphs = Morph.from_sent(parsed_chunk_text)
        return Chunk(morphs, dst, [])

    # Chunkのリストを返す
    def from_cabocha_format(sent_text: str):
        chunks_text = sent_text.split("\n*")
        chunks_text = filter(lambda x: x, chunks_text)
        chunks = list(map(Chunk.from_chunk_text, chunks_text))

        for i, c in enumerate(chunks):
            if c.dst == -1:
                continue
            chunks[c.dst].srcs.append(i)

        return chunks

    def to_str_without_sign(self) -> str:
        return self.to_str_replace_specific_pos("記号", "")

    def to_str_replace_specific_pos(self, pos: str, new: str) -> str:
        ret_str = ""
        is_continue = False

        for m in self.morphs:
            if m.pos == pos or m.pos == "記号":
                if not is_continue:
                    ret_str += new
                is_continue = True
            else:
                ret_str += m.surface
                is_continue = False

        return ret_str

    def include_specific_pos(self, pos: str) -> bool:
        return any(map(lambda x: x.pos == pos, self.morphs))

    def __repr__(self) -> str:
        return "".join(map(lambda x: x.surface, self.morphs)) + f":{self.dst}"