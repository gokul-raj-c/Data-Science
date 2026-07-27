#A dictionary stores marks: {"Anu": 78, "Ravi": 35, "Meera": 92, "John": 60}. 
# Print the grade for each student: 90 and above "A", 75 to 89 "B", 40 to 74 "C", below 40 "Fail"

marks={
    "Anu":78, 
    "Ravi":35, 
    "Meera":92, 
    "John":60
    }
print(marks)
a=list(marks.keys())
i=0
while i<len(a):
    if marks[a[i]]>=90:
        print(a[i],"-> A")
    elif marks[a[i]] >=75:
        print(a[i],"-> B")
    elif marks[a[i]] >=40:
        print(a[i],"-> C")
    else:
        print(a[i],"-> Fail")
    i=i+1