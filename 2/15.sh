python 15.py popular-names.txt 10 > tail_10_py.txt
tail popular-names.txt -n 10 > tail_10.txt
diff tail_10_py.txt tail_10.txt