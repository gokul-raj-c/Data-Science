def sum_of_list(arr,val):
    s=0
    for i in arr:
        if i%val==0:
            s=s+i
    return s

a=[1,2,3,4,5,6,7,8,9]
print(a)
r=sum_of_list(a,3)
print(r)