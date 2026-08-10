# Write a function filter_words(words, min_len=4) that returns only the words whose length is at least min_len. 
# Test it with ["sun", "python", "sky", "loop", "code"].

def filter_words(words, min_len=4):
    new_list=[]
    for i in words:
        if len(i) >= min_len:
            new_list.append(i)
    return new_list

a=["sun", "python", "sky", "loop", "code"]
print(a)
res=filter_words(a)
print(res)