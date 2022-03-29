python 12.py popular-names.txt
cut -f 1 popular-names.txt > col1_by_cut.txt
cut -f 2 popular-names.txt > col2_by_cut.txt
diff col1.txt col1_by_cut.txt
diff col2.txt col2_by_cut.txt