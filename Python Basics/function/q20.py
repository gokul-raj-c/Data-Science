#write a function that return a list contain prime numbers

def prime_numbers(arr):
    prime_list=[]
    for i in arr:
        if i>1:
            f=0
            for j in range(2,i):
                if i%j==0:
                    f=1
                    break
            if f==0:
                prime_list.append(i)
    return prime_list

a=[1,2,3,4,5,6,7,8,9,10]
print(a)
new_list=prime_numbers(a)
print("prime numbers in the list:",new_list)