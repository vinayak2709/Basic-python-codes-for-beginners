# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 19:54:14 2021

@author: Vinayak
"""



""" 
Calculator with operator input and number input -loop operation
"""

input_1 =int(input("please enter 1st number : "))

input_2 =int(input("please enter 2Nd number : "))

while(True):   
    
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
    
    print("Do you want to continue for new operation...?")
    
    ans=input("Please enter yes/no : ")
    
    if ans=="yes":
        pass
    elif ans=="no":
        break
    else:
        print("please enter right string value")
        
        

    
    
    
