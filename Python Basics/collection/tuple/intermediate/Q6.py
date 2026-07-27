# From (123, 45, 900, 72), create a list containing the sum of digits of each number.

a=(123,45,900,72)
print(a)
a=list(a)
sum_list=[]
i=0
while i<len(a):
    s=0
    while a[i]>0:
        d=a[i]%10
        s=s+d
        a[i]=a[i]//10
    sum_list.append(s)
    i=i+1
print(sum_list)