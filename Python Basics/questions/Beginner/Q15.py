# Ask the user for a word and a letter, and count how many times that letter appears in the word using a while loop.

w=input("enter a word: ")
l=input("enter a letter: ")
c=0
i=0
n=len(w)-1
while i<=n:
    if w[i]==l:
        c=c+1
    i=i+1
print("letter count:",c)