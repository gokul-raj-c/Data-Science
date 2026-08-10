#Write a function count_vowels(word) that returns the number of vowels in a word, and a function vowel_report(words) 
# that returns a dictionary mapping each word to its vowel count. Test it with ["python", "loop", "list", "code"].

def count_vowels(word):
    c=0
    for w in word:
        if w in "aeiou":
            c=c+1
    return c

def vowel_report(words):
    vowels={}
    for word in words:
        vowels[word]=count_vowels(word)
    return vowels

a=["python", "loop", "list", "code"]
print(a)
res=vowel_report(a)
print(res)