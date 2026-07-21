#Check whether a number is automorphic (its square ends with the number itself, e.g., 25 → 625, 76 → 5776).

a=int(input("enter number: "))
temp=a
c=0
while temp>0:
    c=c+1
    temp=temp//10

val=a**2

last=val%(10**c)

if last==a:
    print("automorphic")
else:
    print("not automorphic")