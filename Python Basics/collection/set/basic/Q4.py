#From the word "education", create a set of vowels that appear in the word.

w="education"
vowels=set()
i=0
while i<len(w):
    if w[i]=="a" or w[i]=="e" or w[i]=="i" or  w[i]=="o" or w[i]=="u":
        vowels.add(w[i])
    i=i+1
print(vowels)