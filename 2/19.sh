python 19.py popular-names.txt > most_common_col1.txt
cut -f 1 popular-names.txt | sort -s | uniq -c | sort -s -k 1 -g -r > most_common_col1_by_command.txt