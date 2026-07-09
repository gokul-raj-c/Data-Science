# a=input("enter number: ")
# if len(a)==3:
#     if ( int(a[0]) + int(a[1]) + int(a[2]) ) % 2 == 0:
#         print("valid")
#     else:
#         print("invalid")
# else:
#     print("invalid")


a=int(input("enter number: "))
if len(str(a))==3:
    d1=a//100
    d2=(a//10)%10
    d3=a%10
    print(d1+d2+d3)
else:
    print("invalid")


# print(type(0>5))