#! /bin/bash
# http://www.cl.ecei.tohoku.ac.jp/nlp100/#ch2

# 10.
wc -l hightemp.txt

# 11.
tr '\t' ' ' < hightemp.txt

# 12.
cut -f 1 hightemp.txt > col1.txt
cut -f 2 hightemp.txt > col2.txt

# 13.
paste col1.txt col2.txt

# 14.
head -4 hightemp.txt

# 15.
tail -4 hightemp.txt

# 16.
split -l 3 hightemp.txt hoge

# 17.
cut -f 1 hightemp.txt | sort | uniq # -c | sort -nr

# 18.
cut -f 3 hightemp.txt | sort

# 19.
cut -f 1 hightemp.txt | sort | uniq -c | sort -nr
