# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 18:01:31 2022

@author: Vinayak
"""
x=0

try:
  print("Hello")
  x+="5"
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")



try:
  print(x)
  x+="5"
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
  
  
  
  
try:
  print(x)
  x+="5"
except:
  print("Something went wrong")
print("The 'try except' is finished")
  
    
  
  
  
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
  
  
  
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")