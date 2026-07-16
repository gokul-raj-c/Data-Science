#Print all prime numbers between 1 and 50.

i=1
while i<=50:
    if i>1:
        j=2
        flag=0
        while j<i:
            if i%j==0:
                flag=1
            j=j+1
        if flag==0:
            print(i)
    i=i+1