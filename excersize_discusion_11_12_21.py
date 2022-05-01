# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 18:31:08 2021

@author: Vinayak
"""

for i in range(1,10):
    for j in range(1,i):
        print(j,end= '')
    print("")
    
    
    
for row in range(1,10):
    for column in range(row):
        print(column,end= '')
    print("")
    
    
    
 
    
for row in range(1,10):
    for column in range(10):
        print(column,end= '')
    print("***")



for row in range(1,10,3):
    print(row)


list_value=list(range(1,20))
print(list_value)

list_value[-1::-1]
list_value.reverse()






number=5346

number_string=str(number)

number_string_list=list(number_string)

int(number_string[-1::-1])










