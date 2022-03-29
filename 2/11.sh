python 11.py popular-names.txt > spaced.txt
cat popular-names.txt | sed 's/\t/ /g' > spaced_by_sed.txt
diff spaced.txt spaced_by_sed.txt
