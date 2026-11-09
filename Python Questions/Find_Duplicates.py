#Display only the elements that occur more than once.


a = [1, 2, 3, 2, 4, 3, 5, 2]

i = 0

while i < len(a):
    j = 0
    f = 0

    while j < i:
        if a[i] == a[j]:
            f = 1
        j += 1

    if f == 0:
        c = 0
        j = 0

        while j < len(a):
            if a[i] == a[j]:
                c += 1
            j += 1

        if c > 1:
            print(a[i])

    i += 1