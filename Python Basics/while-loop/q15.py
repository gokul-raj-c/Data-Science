#take a string print odd index values first and even index values second

a=input("enter a string: ")
str1=""
str2=""
i=0
while i<len(a):
    if i%2!=0:
        str1=str1+a[i]
    else:
        str2=str2+a[i]
    i=i+1
print(str1+str2)