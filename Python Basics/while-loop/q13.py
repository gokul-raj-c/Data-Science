#check prime

a=int(input("enter number: "))
if a<=1:
    print("not prime")
else:
    i=2
    flag=0
    while i<a:
        if a%i==0:
            flag=1
        i=i+1
    if flag==1:
        print("not prime")
    else:
        print("prime")