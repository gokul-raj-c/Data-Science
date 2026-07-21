#Check whether two numbers are co-prime (their GCD is 1, e.g., 8 and 15 are co-prime).

a=int(input("enter number 1: "))
b=int(input("enter number 2: "))
i=1
gcd=1
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        gcd=i
    i=i+1

if gcd==1:
    print("two numbers are co-prime")
else:
    print("two numbers are not co-prime")
