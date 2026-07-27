#nested dictionary

a={
    "name":"gokul",
    "friends":["abhi","allen","joyal"],
    "address":{
        "district":"ernakulam",
        "state":"kerala",
        "pin":686667
    }
}
print(a)
print(a["name"])
print(a["friends"])
print(a["address"])
print(a["name"][0])
print(a["friends"][0])
print(a["friends"][0][0])
print(a["address"]["state"])
print(a["address"]["state"][0])



# {'name': 'gokul', 'friends': ['abhi', 'allen', 'joyal'], 'address': {'district': 'ernakulam', 'state': 'kerala', 'pin': 686667}}
# gokul
# ['abhi', 'allen', 'joyal']
# {'district': 'ernakulam', 'state': 'kerala', 'pin': 686667}
# g
# abhi
# a
# kerala
# k