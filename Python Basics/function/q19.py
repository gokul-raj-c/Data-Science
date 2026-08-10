#write a function that return the sum of even numbers in the list

def sum_of_even_number(arr):
    s=0
    for i in arr:
        if i%2==0:
            s=s+i
    return s

a=[1,2,3,4,5,6,7,8,9,10]
summ=sum_of_even_number(a)
print(a)
print("sum of even numbers in list:",summ)