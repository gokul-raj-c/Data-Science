#A dictionary stores marks: {"Anu": 78, "Ravi": 32, "Meera": 55, "John": 29} . 
# Print "Pass" or "Fail" for each student, taking 35 as the pass mark, and print how many passed and how many failed.

marks={
    "Anu": 78, 
    "Ravi": 32, 
    "Meera": 55, 
    "John": 29
    }

pass_count=0
fail_count=0
for i in marks:
    if marks[i] >= 35:
        print(i,"-> Pass") 
        pass_count=pass_count+1
    else:
        print(i,"-> Fail")
        fail_count=fail_count+1
print("pass count",pass_count)
print("fail count",fail_count)