var=[1,1,3,2,2,1]
class Unique:
    def uniquelist(self,arr):
        uniq=[]
        for i in range(0,len(arr)):
            f=0
            for j in range(0,i):
                if arr[i]==arr[j]:
                    f=1
            if f==0:
                uniq.append(arr[i])
        return uniq
    def elementcount(self,arr):
        elements=dict()
        for i in arr:
            if i in elements:
                elements[i]=elements[i]+1
            else:
                elements[i]=1
        return elements
obj=Unique()
r1=obj.uniquelist(var)
r2=obj.elementcount(var)
print(r1)
print(r2)