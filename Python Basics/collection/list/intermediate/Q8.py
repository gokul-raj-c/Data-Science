#Forthe list of words ["python", "loop", "list", "code"], count the number of vowels in each word and 
# print the result as word-> vowel count

a=["python", "loop", "list", "code"]
i=0
while i<len(a):
    c=0
    j=0
    while j<len(a[i]):
        if a[i][j]=="a" or a[i][j]=="e" or a[i][j]=="i" or a[i][j]=="o" or a[i][j]=="u":
            c=c+1
        j=j+1
    print(a[i],"-> ",c)
    i=i+1