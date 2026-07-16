#Convert a decimal number to binary using a while loop (e.g., 10 -> 1010).

a=int(input("enter a number: "))
bin=""
while a>0:
    r=a%2
    bin=str(r)+bin
    a=a//2
print(bin)