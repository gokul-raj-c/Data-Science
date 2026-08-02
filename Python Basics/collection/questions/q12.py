#Using the same two lists as above, print the numbers chosen by the first student only.

# a=[2, 5, 8, 9]
# b=[1, 5, 9, 10]
# for x in a:
#     if x not in b:
#         print(x)

a = [2, 5, 8, 9]
b = [1, 5, 9, 10]
set1 = set(a)
set2 = set(b)
print(set1 - set2)