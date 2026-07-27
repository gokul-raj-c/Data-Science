#From the sentence "python is easy and python is powerful", create one set of unique words and another set of repeated words

sentence="python is easy and python is powerful"
words=list(sentence.split())
unique=set()
repeated=set()
i=0
while i<len(words):
    if words[i] in unique:
        repeated.add(words[i])
    else:
        unique.add(words[i])
    i=i+1
print(sentence)
print(words)
print("unique words:",unique)
print("repeated words:",repeated)