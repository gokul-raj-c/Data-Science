#largest among 3 num

# a=10
# b=20
# c=12
# if a > b and a >  c:
#     print(a)
# elif b > c:
#     print(b)
# else:
#     print(c)

a = 10
b = 20
c = 12

# largest = a if a > b else b
# largest = largest if largest > c else c

# print(largest)

large=a
if b>large:
    large=b
if c>large:
    large=c
print(large)