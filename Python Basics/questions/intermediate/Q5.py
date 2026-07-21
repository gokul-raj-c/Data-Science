#Print all Armstrong numbers between 100 and 999 (e.g., 153 → 1³ + 5³ + 3³ = 153).

a=100
while a<=999:
    c=0

    temp=a
    while temp>0:
        c=c+1
        temp=temp//10

    temp=a
    summ=0
    while temp>0:
        d=temp%10
        summ=summ+(d**c)
        temp=temp//10

    if summ==a:
        print(a)
    a=a+1