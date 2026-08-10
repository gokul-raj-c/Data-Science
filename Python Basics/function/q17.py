#define a function, pass a list as argument, find its sum

def sum_of_list(a):
    s=0
    for i in a:
        s=s+i
    return s

arr=[10,20,30,40,50]
print(arr)
b=sum_of_list(arr)
print("list sum:",b)