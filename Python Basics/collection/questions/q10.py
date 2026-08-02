# From ((1, 8), (4, 3), (5, 6)) , print the pair with the largest total and print that total.

a=((1, 8), (4, 3), (5, 6))
print(a)
pair=a[0]
pair_total=a[0][0]+a[0][1]
for i in a:
    total=i[0]+i[1]
    if total > pair_total:
        pair=i
        pair_total=total
print("pair with the largest total:",pair)
print("total:",pair_total)