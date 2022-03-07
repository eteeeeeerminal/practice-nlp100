from typing import List
import re
import random

# 1
STRESSED = "stressed"
rev_stressed = ''.join(list(reversed(STRESSED)))
print(rev_stressed)

# 2
PTTKKS = "パタトクカシーー"
PTK = ''.join([c for i, c in enumerate(PTTKKS) if i % 2 == 0])
print(PTK)

# 3
PI_STR = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
normalized_str = PI_STR.replace(",", "").replace(".", "")
words = normalized_str.split(" ")
pi_list = [len(w) for w in words]
print(pi_list)

# 4
ATOM_STR = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
normalized_str = ATOM_STR.replace(",", "").replace(".", "")
words = normalized_str.split(" ")

one_chr = [1, 5, 6, 7, 8, 9, 15, 16, 19]
atom_dict = {}
for i, word in enumerate(words):
    i += 1
    if i in one_chr:
        atom_dict[word[0]] = i
    else:
        atom_dict[word[:2]] = i
print(atom_dict)

# 5
def n_gram(target: List[str], n: int):
    target_n = len(target)
    return [target[i:i+n] for i in range(target_n-n+1)]

def word_n_gram(target: str, n: int):
    return n_gram(target.split(" "), n)

def char_n_gram(target: str, n: int):
    return n_gram(target, n)

TARGET = "I am an NLPer"
print(word_n_gram(TARGET, 2))
print(char_n_gram(TARGET, 2))

# 6
PARADISE = "paraparaparadise"
PAR = "paragraph"
X = set(char_n_gram(PARADISE, 2))
Y = set(char_n_gram(PAR, 2))
print(X)
print(Y)
print(X | Y)
print(X & Y)
print(X - Y)
print("se" in X)
print("se" in Y)

# 7
def temp(x, y, z) -> str:
    return f"{x}時の{y}は{z}"
print(temp(12, "気温", 22.4))

# 8
def cipher(target: str) -> str:
    ciphered = ""
    for c in target:
        m = re.match(r"[a-z]", c)
        if m:
            # アルファベットなら
            c = chr(219 - ord(c))
            ciphered += c
        else:
            ciphered += c
    return ciphered

TARGET = "I am an NLPer"
ciphered = cipher(TARGET)
print(ciphered)
print(cipher(ciphered))

# 9
TARGET = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def shuffle_char(word: str) -> str:
    if len(word) <= 4:
        return word
    should_shuffle = list(word[1:-1])
    random.shuffle(should_shuffle)
    return word[0] + ''.join(should_shuffle) + word[-1]

shuffled = " ".join([shuffle_char(w) for w in TARGET.split(" ")])
print(shuffled)
