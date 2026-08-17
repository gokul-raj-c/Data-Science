def list_sum(a,i):
    if i==len(a):
        return 0
    return a[i] + list_sum(a,i+1)

a=[11,9,13,17,5]
s=list_sum(a,0)
print(s)