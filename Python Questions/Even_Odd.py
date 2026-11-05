#Create two separate lists containing even and odd numbers

arr=[1,2,3,4,5,6,7,8,9,10]
even_arr=[]
odd_arr=[]
for i in arr:
    if i % 2 == 0:
        even_arr.append(i)
    else:
        odd_arr.append(i)
print(arr)
print(even_arr)
print(odd_arr)