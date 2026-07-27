# From the list ["apple", "sky", "orange", "try", "ice"], count how many words contain at least one vowel.

a=["apple","sky","orange","try","ice"]
c=0
i=0
while i<len(a):
    j=0
    flag=0
    while j<len(a[i]):
        if a[i][j]=="a" or a[i][j]=="e" or a[i][j]=="i" or a[i][j]=="o" or a[i][j]=="u":
            flag=1
            break
        j=j+1
    if flag==1:
        c=c+1
    i=i+1
print("no of words that contain at least one vowel:",c)