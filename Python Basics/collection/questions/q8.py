#From (12, 15, 9, 20, 6) , print the values that are divisible by 3 and print their total.

a=(12, 15, 9, 20, 6)
print(a)
total=0
for i in a:
    if i % 3==0:
        print(i)
        total=total+i
print(total)