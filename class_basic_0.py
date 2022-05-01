# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 16:44:24 2021

@author: Vinayak
"""

# OOP -Object oriented Programming

class Student:
    marks=100   # class var
    name="Vinayak"
    roll="IND1234"
    
    
    
obj1=Student()

obj2=Student()  
  

print(type(obj1))
obj1.marks
obj2.marks

obj2.marks=400
obj1.marks=4000

Student.marks


# object & class

""" motorola company - class   - only one
 motorola G3 mobile - Object   -Many copies  """
 
 
var=12   # object of class int
var_str="vin"
print(type(var))

print(type(var_str))

    

str_int="5"

print(type(str_int))

int2=int(str_int)
    
print(type(int2))

