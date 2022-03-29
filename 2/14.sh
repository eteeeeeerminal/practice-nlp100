python 14.py popular-names.txt 10 > head_10_py.txt
head popular-names.txt -n 10 > head_10.txt
diff head_10_py.txt head_10.txt