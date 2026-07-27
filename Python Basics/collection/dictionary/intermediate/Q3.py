#A dictionary stores marks: {"Anu": 78, "Ravi": 45, "Meera": 92, "John": 60}. 
# Find the average and print students above the average

marks={
    "Anu":78, 
    "Ravi":45, 
    "Meera":92, 
    "John":60
    }
a=list(marks.keys())
total=0
i=0
while i<len(a):
    total=total+marks[a[i]]
    i=i+1
avg=total/len(a)
print("average:",avg)
i=0
while i<len(a):
    if marks[a[i]]>avg:
        print(a[i],marks[a[i]])
    i=i+1