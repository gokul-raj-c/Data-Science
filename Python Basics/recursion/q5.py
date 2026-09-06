#list sum using recursion

def list_sum(arr,i=0):
    if i==len(arr):
        return 0
    return arr[i]+list_sum(arr,i+1)

a=[1,2,3,4,5]
summ=list_sum(a)
print(summ)