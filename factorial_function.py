# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 18:46:50 2021

@author: Vinayak
"""

"""
4! =1*2*3*4
"""

def fact_func(number):
    
    factorial_2=1
    count=1
    
    while(count<=number):
    
        factorial_2=factorial_2*count
        count+=1
        
    print(factorial_2)
    return factorial_2
    

number=3
fact_func(number)
