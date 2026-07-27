#A dictionary stores marks: {"Anu": 80, "Ravi": 35, "Meera": 60, "John": 28}. 
# Count how many students passed and failed. Passing mark is 40.

marks={
    "Anu":80,
    "Ravi":35,
    "Meera":60,
    "John":28
    }
a=list(marks.keys())
pass_count=0
fail_count=0
i=0
while i<len(a):
    if marks[a[i]]>=40:
        pass_count=pass_count+1
    else:
        fail_count=fail_count+1
    i=i+1
print(marks)
print("no of students passed:",pass_count)
print("no of students failed:",fail_count)