# Find the GCD of three numbers using while loops.

a=int(input("enter number 1: "))
b=int(input("enter number 2: "))
c=int(input("enter number 3: "))

small=a
if b<small:
    small=b
if c<small:
    small=c

gcd=1
i=1

while i<=small:
    if a%i==0 and b%i==0 and c%i==0:
        gcd=i
    i=i+1
print(gcd)