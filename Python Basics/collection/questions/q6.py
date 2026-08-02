#From (5, 12, 7, 3, 20, 9) , count how many values are even and how many are odd, then print which group has more.

a=(5, 12, 7, 3, 20, 9)
even_count=0
odd_count=0
for i in a:
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print(a)
print("even count:",even_count)
print("odd count:",odd_count)