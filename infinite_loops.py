# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 18:24:00 2021

@author: Vinayak
"""

# infinite loop



while(True):      
    print("infinte")
    
print("loop completed")




while(False):      
    print("in")
print("loop completed")



while(True):      
    print("infinte")
    pass  # just empty statement
    break # to break a loop
    print("after break")

print("loop completed")




while(True):      
    print("infinte")
    continue
    # skips everything below it
    print("after continue")
    
print("loop completed")
