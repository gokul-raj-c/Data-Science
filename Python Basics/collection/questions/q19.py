#Using the same marks dictionary, find the student with the highest mark without using max()

marks={
    "Anu": 78, 
    "Ravi": 32, 
    "Meera": 55, 
    "John": 29
    }

high_mark=marks["Anu"]
student="Anu"
for i in marks:
    if marks[i] > high_mark:
        high_mark=marks[i]
        student=i

print("top student:", student)
print("highest mark:", high_mark)
        