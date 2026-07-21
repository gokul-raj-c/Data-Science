#Convert a decimal number to octal using a while loop (e.g., 25 → 31).

a=int(input("enter number: "))
oct=""
while a>0:
    r=a%8
    oct=str(r)+oct
    a=a//8
print(oct)