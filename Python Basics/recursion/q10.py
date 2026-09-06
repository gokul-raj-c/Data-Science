#Find the maximum element

def find_maximun(arr,i=0):
    if i==len(arr):
        return arr[i-1]
    maximum=find_maximun(arr,i+1)
    if arr[i] > maximum:
        return arr[i]
    else:
        return maximum

print(find_maximun([2,8,9,10,4]))