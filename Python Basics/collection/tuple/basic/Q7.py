#From the tuple ("python", "loop", "if", "condition", "code"), print only the words with more than 4 letters.

a=("python","loop","if","condition","code")
print(a)
i=0
while i<len(a):
    if len(a[i])>4:
        print(a[i])
    i=i+1