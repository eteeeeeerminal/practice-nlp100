python 18.py popular-names.txt > sorted.txt
sort popular-names.txt -g -k 3 -s -r > sorted_by_command.txt
diff sorted.txt sorted_by_command.txt