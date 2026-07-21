#Remove all zeros from a number (e.g., 102030 → 123).

a=int(input("enter number: "))
p=1
numm=0

while a>0:
    d=a%10
    if d!=0:
        numm=numm+(d*p)
        p=p*10
    a=a//10
print(numm)