#Check if a list is sorted

def check_list_sorted(arr,i=0):
    if i==len(arr)-1:
        return True
    if arr[i] > arr[i+1]:
        return False
    return check_list_sorted(arr,i+1)

print(check_list_sorted([1,2,3,4,5]))