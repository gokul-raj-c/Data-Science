import numpy as np

a=[
    [1,2,3],
    [4,5,6]
]
b=[
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ],
    
]
new_a=np.array(a)
new_b=np.array(b)
print(new_a.shape)     #(2, 3)   2- no of rows ie no of list,    3- no of columns , ie no of values
print(new_b.shape)
print(new_b.size)      #12   no of values inside
print(new_b.itemsize)   #4  each element size