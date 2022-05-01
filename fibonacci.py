# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:19:07 2022

@author: Vinayak
"""

"""
0 1 2 3 4 5 6

1 1 2 3 5 8 13 21 ....

"""





# Recursive function
def fibonacci(n):
    if n <= 1:
    	return n
    else:
    	return(fibonacci(n-1) + fibonacci(n-2))
    
    n_value = 10
    
  
    for i in range(n_value):
    	print(fibonacci(i))






fibonacci(7)










































