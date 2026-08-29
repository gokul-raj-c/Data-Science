#match 
#it is similiar to switch

x=int(input("enter num: "))
match x:
    case 1:
        print("1")
    case 2:
        print("2")
    case _:
        #default
        print("unknown")

# it has or condition that is case "amal"|"ann" but not have and case