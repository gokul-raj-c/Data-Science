# Write a function grade(mark) that returns the grade for one mark, and a function report(marks) 
# that uses it to return a list of grades and the number of students who passed (40 and above).
# Test it with [78, 45, 92, 60, 33]. 
# 90 and above: "A" 
# 75 to 89: "B" 
# 60 to 74: "C" 
# 40 to 59: "D" 
# Below 40: "Fail"

def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "Fail"

def report(marks):
    count=0
    mark_grades=[]
    for m in marks:
        mark_grades.append(grade(m))
        if m >= 40:
            count=count+1
    return mark_grades,count

a=[78, 45, 92, 60, 33]
print(a)
grades,pass_count = report(a)
print("grades:", grades)
print("no of students passed:",pass_count)