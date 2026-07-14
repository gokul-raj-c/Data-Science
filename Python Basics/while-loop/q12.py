#print numbers btwn two limit that have last digit 3  

n1=int(input("enter first number: "))
n2=int(input("enter second number: "))
while n1<=n2:
    if n1%10==3:
        print(n1)
    n1=n1+1