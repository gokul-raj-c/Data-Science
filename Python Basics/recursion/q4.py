# using recursion check a element is found in the list

def home(a,i,v):
    if i==len(a):
        return False
    if a[i]==v:
        return True
    else:
        return home(a,i+1,v)

a=[1,2,3,4,5]
print(home(a,0,9))