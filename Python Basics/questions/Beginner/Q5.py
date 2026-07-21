#Ask the user for a word and count its vowels and consonants separately using a while loop and an index.

a=input("enter a word: ")
n=len(a)-1
i=0
v_count=0
c_count=0
while i<=n:
    if a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u":
        v_count=v_count+1
    else:
        c_count=c_count+1
    i=i+1
print("vowels count:",v_count)
print("consonants count",c_count)