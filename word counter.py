import re
import string
from collections import Counter
import csv

frequency = {}
document_text = open('android_design.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

w_count = Counter(match_pattern)

sort_words = w_count.most_common()

f = open("android_word_count.txt", "w")

for word, num in sort_words:
	data = "%r => %r \n" % (word, num)
	f.write(data)
f.close()



with open('android_word_count.csv', 'wb') as f:
    writer = csv.writer(f)
    for row in w_count.iteritems():
        writer.writerow(row)


print len(match_pattern)