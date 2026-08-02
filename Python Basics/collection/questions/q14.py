#Check whether the list [5, 2, 9, 5, 4] contains any repeated value by comparing its length with the length of a set made from it. 
# Print a suitable message.

numbers = [5, 2, 9, 5, 4]
numbers_set=set(numbers)
if len(numbers)==len(numbers_set):
    print("No repeated values.")
else:
    print("The list contains repeated values.")