import re
import json

with open("britain.txt") as f:
    data = f.read()

# 基礎情報の抜き出し
base_info_pattern = re.compile(r"\{\{基礎情報 国([\s\S]+)\n\}\}")
base_info = base_info_pattern.search(data)[1]

# 各フィールド抜き出し
fields_text = base_info.split("\n|")

fields_pattern = re.compile(r"([^=]+)\s*=\s*([\s\S]+)")
fields_match = [fields_pattern.match(f) for f in fields_text]

# dictに箱詰め
## クリーニング用のパターン
### 強調
emphasis_pattern1 = re.compile(r"'{5,5}([\s\S]+)'{5,5}")
emphasis_pattern2 = re.compile(r"'{3,3}([\s\S]+)'{3,3}")
emphasis_pattern3 = re.compile(r"'{2,2}([\s\S]+)'{2,2}")
### 内部リンク
inter_link_pattern1 = re.compile(r"\[\[[^\|\[\]]+\|([^\[\]]+\|)?([^\[\]]+)\]\]")
inter_link_pattern2 = re.compile(r"\[\[([^\[\]]+)\]\]")
### 箇条書き
items_pattern = re.compile(r"\n\*+")
### ref, br 削除
ref_pattern = re.compile(r"\</?ref[^\<\>]*\>")
br_pattern = re.compile(r"\<br /\>")
### 多言語タグ
lang_pattern = re.compile(r"\{\{lang\|[\w]{2,3}\|([^\{\}]+)\}\}")
### 外部リンク
outer_link_pattern = re.compile(r"\[[^\[\]]+\]")
### 数字のフォーマット
num_format_pattern = re.compile(r"\{\{0\}\}")
### {{en icon}}
icon_pattern = re.compile(r"\{\{en icon\}\}")
### ファイル
file_pattern = re.compile(r"\{\{([\w]+\|)?ファイル:([^\{\}]+)\}\}")
### 仮リンク
any_link_pattern = re.compile(r"\{\{仮リンク\|[^\{\}]+\|([^\|\{\}]+)\}\}")
### cite web
cite_web_pattern = re.compile(r"\{\{Cite web\|[^\{\}]+\}\}")

base_info_dict = {}
for f_match in fields_match:
    if f_match is None:
        continue

    non_emphasis = emphasis_pattern1.sub(r"\1", f_match[2])
    non_emphasis = emphasis_pattern2.sub(r"\1", non_emphasis)
    non_emphasis = emphasis_pattern3.sub(r"\1", non_emphasis)
    non_inter_link = inter_link_pattern1.sub(r"\2", non_emphasis)
    non_inter_link = inter_link_pattern2.sub(r"\1", non_inter_link)
    non_items = items_pattern.sub(r"\n", non_inter_link)
    non_tags = ref_pattern.sub(r"", non_items)
    non_tags = br_pattern.sub(r"", non_tags)
    non_lang = lang_pattern.sub(r"\1", non_tags)
    non_outer_link = outer_link_pattern.sub(r"", non_lang)
    non_num_format = num_format_pattern.sub(r"", non_outer_link)
    non_icon = icon_pattern.sub(r"", non_num_format)
    non_file = file_pattern.sub(r"", non_icon)
    non_link = any_link_pattern.sub(r"\1", non_file)
    non_cite = cite_web_pattern.sub(r"", non_link)
    base_info_dict[f_match[1]] = non_cite.replace("}", "")


with open("britain.json", "w") as f:
    json.dump(base_info_dict, f, ensure_ascii=False, indent=4)
