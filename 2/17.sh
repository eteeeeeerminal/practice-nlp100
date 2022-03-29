python 17.py popular-names.txt > col1_set.txt
cut -f 1 popular-names.txt | sort | uniq > col1_set_by_command.txt
diff col1_set.txt col1_set_by_command.txt