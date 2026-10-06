"""
 0 0 0 0 0 
 0 0 0 0 0 
 0 0 0 0 0 
 0 0 0 0 0 
 0 0 0 0 0 
 
 [[3],
  [4],
  [2],
  [4]
  [1],
  ]   
                       
 0 0 0 1 1 
 0 0 0 0 1 
 0 0 1 1 1 
 0 0 0 0 1 
 0 1 1 1 1
"""

import numpy as np
arr=np.zeros((5,5),dtype=int)
index=np.array([3,4,2,4,1]).reshape(5,1)
print(arr)
print(index)
