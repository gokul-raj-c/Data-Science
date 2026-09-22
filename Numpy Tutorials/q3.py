import numpy as np

a=[1,2,3,4]
b=[
    [1,6,8],
    [2,7,8],
]
c=[
    [
        [1,6,8],
        [2,7,8],
    ],
    [
        [1,6,8],
        [2,10,8], 
    ]       
]
d=[
    [
        [
            [1,2,3,4]
        ],
        [
            [5,6,7,8]
        ],
    ]
]

new_a=np.array(a)
new_b=np.array(b)
new_c=np.array(c)
new_d=np.array(d)
print(new_a)
print(new_b)
print(new_c)

print(new_a[1])
print(new_b[1,1])   # to take a value in numpy array use [1,1]  
print(new_c[1,1,1])
print(new_c.ndim)   #to find the dimension 
print(new_d.ndim)

print(np.shape(new_d))    

#dimension - no of axis used to find a value in a list