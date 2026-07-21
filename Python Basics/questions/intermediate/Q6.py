# Print all Fibonacci numbers less than 1000 (0, 1, 1, 2, 3, 5, 8, ... 987).

a=0
b=1
while a<=1000:
    print(a,end=" ")
    c=a+b
    a=b
    b=c

