#Find all pairs of elements whose sum equals a given target.

a=[2,4,3,5,7,8]
target=10

a = [2, 4, 3, 5, 7, 8]
target = 10

i = 0

while i < len(a):
    j = i + 1

    while j < len(a):
        if a[i] + a[j] == target:
            print(a[i], a[j])

        j = j + 1

    i = i + 1