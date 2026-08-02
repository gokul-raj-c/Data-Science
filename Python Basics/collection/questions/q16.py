#Count how many times each letter appears in the word "banana" using a dictionary, 
# then print only the letters that appear more than once.

word="banana"
word_set={}
for i in word:
    if i not in word_set:
        word_set[i]=1
    else:
        word_set[i]=word_set[i]+1
print(word_set)
for i in word_set:
    if word_set[i] > 1:
        print(i)