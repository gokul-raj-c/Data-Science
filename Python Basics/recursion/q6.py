#prime number using recursion

# def check_prime(num):
#     if num < 2:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
   


def check_prime(num,i=2):
    if num < 2:
        return False
    if num % i==0:
        return False
    if i > num//2:
        return True
    return check_prime(num,i+1)

n=int(input("enter number: "))
print(check_prime(n))