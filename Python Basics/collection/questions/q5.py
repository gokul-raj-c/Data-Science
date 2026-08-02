#Check whether [3, 8, 6, 12, 15] is arranged in increasing order. 
# Print True or False , and if it is False , print the first place where the order breaks.

a=[3, 8, 6, 12, 15]
f=0
for i in range(1,len(a)):
    if a[i]<a[i-1]:
        f=1
        print("False")
        print(i+1)
        break
if f==0:
    print("True")