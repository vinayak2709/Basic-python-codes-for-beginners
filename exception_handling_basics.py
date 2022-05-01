# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 18:35:50 2022

@author: Vinayak
"""

x="1"
try:
    sum2=x+2
except:
   
    sum2=0

        
    
print(sum2)

# multiple excepts

value=2
# divisor=0

try:
    value+="6"
    value/divisor

except ZeroDivisionError:
    print("pls take non zero divisor..")

except NameError:
    print("please define variable")
    
except TypeError:
    print("please check the type of variable")

except:
    print("Any other error")