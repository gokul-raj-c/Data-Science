a={
    "name":"gokul",
    "age":23,
    "place":"ernakulam",
}
print(a)
print(a["name"])
print(a["age"])
print(a["place"])

#another method to retrieve value 
y=a.get("name")
print(y)

#print(a["gokul"])  #KeyError: 'gokul'

#update values in dictionary
a["name"]="abcd"
print(a)

a["friend"]="thomas"  #here new key get added to dictionary with its value
print(a)
#no duplicate keys allowed in dictionary

#to delete a value 
a.pop("age")
print(a)

#delete all items from dictionary
a.clear()
print(a)