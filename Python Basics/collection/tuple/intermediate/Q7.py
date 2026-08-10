# From (1, 1, 2, 2, 2, 3, 1, 1), find the longest continuous streak of the same value

a = (1, 1, 2, 2, 2, 3, 1, 1)

current = 1
longest = 1

for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        current = current + 1
    else:
        current = 1

    if current > longest:
        longest = current

print("Longest continuous streak:", longest)