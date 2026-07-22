#Take the list [12,45,8,33,27] and print how many numbers are greater than 20 and how many are less than or equal to 20

a=[12,45,8,33,27]
g_count=0
le_count=0
i=0
while i<len(a):
    if a[i]>20:
        g_count=g_count+1
    else:
        le_count=le_count+1
    i=i+1
print("numbers greater than 20 =",g_count)
print("numbers less than or equal to 20 =",le_count)
