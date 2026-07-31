#Write a function print_area(length, width) that computes the area of a rectangle and prints Area: <result>

def print_area(lenght,width):
    result=lenght*width
    print("area:",result)

x=int(input("enter length: "))
y=int(input("enter width: "))
print_area(x,y)