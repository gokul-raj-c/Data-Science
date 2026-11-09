#Find all pairs of adjacent elements whose sum is greater than 10.

a = [3, 8, 5, 7, 2, 9]

i = 0

while i < len(a) - 1:
    if a[i] + a[i + 1] > 10:
        print(a[i], a[i + 1])

    i += 1