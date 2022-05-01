# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 18:35:20 2021

@author: Vinayak
"""
cubes=[]

dictionary_cubes={}
dictionary_cubes2={}
for count in range(0,101):
    print('The count is:', count)
    cube_value= count*count*count
    print("value : ", count, "cube value : ",cube_value)
    print("******")
    
    # to save in list
    cubes.append(cube_value)
    
    # to save in dictionary
    dictionary_cubes[count]=count*count*count
    
    #or
    
    
    dictionary_cubes2.update({count:cube_value})
  
 
squares=[]
for count in range(0,101):
    print('The count is:', count)
    sq_value= count*count
    print("value : ", count, "cube value : ",sq_value)
    print("******")
    squares.append(sq_value)
    
    
    