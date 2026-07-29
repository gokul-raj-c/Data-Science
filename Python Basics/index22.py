a=[6,8,9,10,11]
b=[]
# i=len(a)-1
# while i>=0:
#     b.append(a[i])
#     i=i-1
# print(a)
# print(b)

# i=0
# j=len(a)-1
# print(a)
# while i<j:
#     a[i],a[j]=a[j],a[i]
#     i=i+1
#     j=j-1
# print(a)

print(a)
for i in range((len(a)-1),-1,-1):
    b.append(a[i])
print(b)