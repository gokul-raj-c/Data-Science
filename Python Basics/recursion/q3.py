# def list_sum(a,i):
#     if i==len(a):
#         return 0
#     return a[i] + list_sum(a,i+1)

# a=[11,9,13,17,5]
# s=list_sum(a,0)
# print(s)


def list_sum(a):
    if len(a)==0:
        return 0
    return a[0] + list_sum(a[1:])

a=[11,9,13,17,5]
s=list_sum(a)
print(s)


# def home(arr,i,val):
#     if i==len(arr):
#         return False
#     if arr[i]==val:
#         return True
#     else:
#         return home(arr,i+1,val)

# a=[11,2,9,0,3]
# print(home(a,0,9))