#take a string print index values that are multiples of 3

a=input("enter a string: ")
str1=""
i=0
while i<len(a):
    if i%3==0:
        str1=str1+a[i]
    i=i+1
print(str1)