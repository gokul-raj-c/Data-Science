#reverse a list

a=[11,22,33,44,55,66]
print(a)
i=len(a)-1
while i>=0:
    print(a[i],end=" ")
    i=i-1




# a=[2,5,2,8,5,2]
# i=0
# while i<len(a):
#     j=0
#     f=0
#     while j<i:
#         if a[i]==a[j]:
#             f=1
#         j=j+1
#     if f==0:
#         c=0
#         j=0
#         while j<len(a):
#             if a[i]==a[j]:
#                 c=c+1
#             j=j+1
#         print(a[i],"appears",c,"times")
#     i=i+1