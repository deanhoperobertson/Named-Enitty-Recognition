import pandas as pd

w = open("words.txt",encoding='utf-8')
f = open("embeddings.txt",encoding='utf-8')

words_list = []
for word in w:
    words_list.append(word)

i=0
values =[]
for line in f:
    values.append(str(words_list[i].strip("\n")) +" "+line)
    i+=1

with open('SENNA.txt', 'w') as f:
    for item in values:
        f.write("%s" % item)