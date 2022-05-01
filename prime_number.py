# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 19:56:11 2021

@author: Vinayak
"""

num=17

for i in range(2,num):  
   
    if num % i==0:
        break        
      
if i >=num-1:
    print(num," is prime number...")
    
else:
    
    print("not prime number")
    