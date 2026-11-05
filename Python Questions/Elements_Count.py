#Count the frequency of every element in a list, displaying each element only once.

arr=[1,2,1,3,2,1,1,2]
uniq={}
for i in arr:
    if i in uniq:
        uniq[i]+=1
    else:
        uniq[i]=1
print(arr)
print(uniq)