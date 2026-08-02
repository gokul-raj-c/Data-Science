# A tuple stores match scores: (3, 5, 4, 7, 9, 6) . 
# For every pair of scores played one after another, print whether the score went up, went down, or stayed the same.

a=(3, 5, 4, 7, 9, 6)
for i in range(0,len(a)-1):
    if a[i] > a[i+1]:
        print("score went down")
    elif a[i] < a[i+1]:
        print("score went up")
    else:
        print("score stayed same")