# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 17:33:23 2021

@author: Vinayak
"""

""" count each character occurance and print for each :
    
    input = "we are learning..." 
    """
    
  
import time


prev_time=time.time()    
  
input_1= "we are learning..." 

occurance_dictionary={}

# for i in input_1:
#     occurance_dictionary[i]=0

for i in input_1:
    print(i)
    
    # print(occurance_dictionary.get(i))
    if occurance_dictionary.get(i):
    
        occurance_dictionary[i]=occurance_dictionary[i]+1
        
    else:
        # print("yes",i)
        occurance_dictionary[i]=1
        print(occurance_dictionary)
        
           
print(occurance_dictionary)


after_execution_time=time.time()   


final=after_execution_time-prev_time

print(final*10000)

 
