# using recursion check a element is found in the list

def home(arr,i,val):
    if i==len(arr):
        return False
    if arr[i]==val:
        return True
    return home(arr,i+1,val)

a=[11,2,9,0,3]
print(home(a,0,9))