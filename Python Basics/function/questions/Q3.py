#Write a function remove_duplicates(items) that returns a new list with duplicates removed, keeping the original order. 
# Test it with [1, 3, 1, 5, 3, 7, 5] (answer: [1, 3, 5, 7]).

def remove_duplicates(items):
    new_list=[]
    for i in range(0,len(items)):
        f=0
        for j in range(0,i):
            if items[i]==items[j]:
                f=1
        if f==0:
            new_list.append(items[i])
    return new_list

a=[1, 3, 1, 5, 3, 7, 5]
print(a)
res=remove_duplicates(a)
print("list after removing duplicates:",res)