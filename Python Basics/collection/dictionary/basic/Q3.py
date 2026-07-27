#From {"math": 85, "science": 72, "english": 90}, find the subject with the highest mark.

marks={
    "math":85,
    "science":72,
    "english":90
}
print(marks)
a=list(marks.keys())
i=0
high=marks[a[0]]
while i<len(a):
    if marks[a[i]]>high:
        high=marks[a[i]]
    i=i+1
i=0
while i<len(a):
    if marks[a[i]]==high:
        print("subject with the highest mark:",a[i])
    i=i+1