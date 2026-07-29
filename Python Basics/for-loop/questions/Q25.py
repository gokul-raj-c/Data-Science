#Find all factors of a given number.

a=int(input("enter number: "))
print("factors of",a)
for i in range(1,a+1):
    if a%i==0:
        print(i)