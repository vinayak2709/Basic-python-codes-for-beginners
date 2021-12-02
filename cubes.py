# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 18:35:20 2021

@author: Vinayak
"""
cubes=[]

for count in range(0,101):
    print('The count is:', count)
    cube_value= count*count*count
    print("value : ", count, "cube value : ",cube_value)
    print("******")
    cubes.append(cube_value)
        
  
 
squares=[]
for count in range(0,101):
    print('The count is:', count)
    sq_value= count*count
    print("value : ", count, "cube value : ",sq_value)
    print("******")
    squares.append(sq_value)