#import home  #module
# s=home.add_numbers(10,3)
# print(s)

#to import a particular function in module
from home import add_numbers,sub_numbers
#import all functions in the module
#from home import * 
print(add_numbers(5,6))
print(sub_numbers(5,2))