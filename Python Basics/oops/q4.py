class Student:
    def __init__(self,a):
        self.name=a
    def home(self):
        print("hello",self.name)
x=Student("jk")
y=Student("suii")
print(x.name)
print(y.name)
x.home()
y.home()