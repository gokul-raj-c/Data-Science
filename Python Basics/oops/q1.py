class Smec:
    name="arun"
    age=21
    address="kaloor"
    def exam(self):
        print(self.name,"attended the examm")

std1=Smec()
std2=Smec()
print(std1.name)
print(std2.name)
std1.name="nihal"
std2.name="ann"
print(std1.age)
print(std2.age)
std1.exam()
std2.exam()
print(std1.name)
print(std2.name)