#Find the sum of the prime digits of a number (prime digits are 2, 3, 5, 7 — e.g., 4729 → 7 + 2 = 9).

a=int(input("enter number: "))
temp=a
summ=0
while temp>0:
    d=temp%10
    if d>1:
        flag=0
        i=2
        while i<d:
            if d%i==0:
                flag=1
            i=i+1
        if flag==0:
            summ=summ+d

    temp=temp//10
print(summ)