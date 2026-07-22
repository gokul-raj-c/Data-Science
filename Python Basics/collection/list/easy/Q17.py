#From the list ["Anu", "Ravi", "Arjun", "Meera", while "Ajay"], print only the names that start with the letter "A".

a=["Anu", "Ravi", "Arjun", "Meera", "Ajay"]
i=0
while i<len(a):
    if a[i][0]=="A":
        print(a[i])
    i=i+1