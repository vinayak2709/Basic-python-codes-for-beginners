# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 19:42:47 2021

@author: Vinayak
"""

""" 
Calculator with operator input and number input
"""

input_1 =int(input("please enter 1st number : "))

input_2 =int(input("please enter 2Nd number : "))

# # addition

# addition_value=input_1+input_2

# # subtraction

# sub=input_1-input_2


# # multiply

# mult=input_1*input_2

# # division

# div=input_1/input_2

operation_input =input("""please enter operation ,for addition enter a , 
                       for sub enter s , 
                       for multiplication enter m , 
                       for division enter d : """)



if operation_input=="a":
    # addition
    
    addition_value=input_1+input_2
    print("Addition is :", addition_value)

elif  operation_input=="s":
    # subtraction
    sub=input_1-input_2
    print("Sub is :", sub)

elif  operation_input=="m":
    # multiply
    mult=input_1*input_2
    print("Mult is :", mult)


elif  operation_input=="d":
    # division
    div=input_1/input_2  
    print("Div is :", div)

    
else:
    print("invalid operation input")



