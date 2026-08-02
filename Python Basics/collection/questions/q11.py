#Two students listed their favourite numbers: [2, 5, 8, 9] and [1, 5, 9, 10] . Use sets to print the numbers both of them chose.

a=[2, 5, 8, 9]
b=[1, 5, 9, 10]
for x in a:
    if x in b:
        print(x)

# a = [2, 5, 8, 9]
# b = [1, 5, 9, 10]
# set1 = set(a)
# set2 = set(b)
# print(set1 & set2)