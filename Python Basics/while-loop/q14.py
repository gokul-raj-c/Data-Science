#prime number btwn 2 limit

n1=int(input("enter limit 1: "))
n2=int(input("enter limit 2: "))
while n1<=n2:
    if n1>1:
        i=2
        flag=0
        while i<n1:
            if n1%i==0:
                flag=1
            i=i+1
        if flag==0:
            print(n1)
    n1=n1+1