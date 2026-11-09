#Find the element that occurs the maximum number of times.

a = [2, 5, 2, 8, 5, 2, 8, 8, 8]

i = 0
max_count = 0
element = 0

while i < len(a):
    j = 0
    count = 0

    while j < len(a):
        if a[i] == a[j]:
            count += 1
        j += 1

    if count > max_count:
        max_count = count
        element = a[i]

    i += 1

print("Most frequent element:", element)
print("Frequency:", max_count)