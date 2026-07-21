#Print all numbers from 1 to 60 that are divisible by both 2 and 3.

i=1
while i<=60:
    if i%2==0 and i%3==0:
        print(i)
    i=i+1