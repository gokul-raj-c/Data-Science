#Ask the user for numbers until they enter 0. Store the numbers in a list, then print the average and largest number entered.

a=1
num=[]
while a!=0:
    a=int(input("enter number: "))
    if a!=0:
        num.append(a)
print(num)
if len(num)==0:
    print("null")
else:
    i=0
    large=num[0]
    s=0
    n=len(num)
    while i<n:
        if num[i]>large:
            large=num[i]
        s=s+num[i]
        i=i+1
    print("average:",s/n)
    print("largest:",large)