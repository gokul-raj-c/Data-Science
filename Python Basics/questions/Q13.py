#Find the GCD (HCF) of two numbers using a while loop

a=int(input("enter number 1: "))
b=int(input("enter number 2: "))
i=1
gcd=1

while i<=a and i<=b:
    if a%i==0 and b%i==0:
        gcd=i
    i=i+1
print(gcd)

