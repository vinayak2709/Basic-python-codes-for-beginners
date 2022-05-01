# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 20:16:04 2022

@author: Vinayak
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 19:42:47 2021

@author: Vinayak
"""

""" 
Calculator with operator input and number input
"""


while(True):
    try:
    
        
        try:
            input_1 =int(input("please enter 1st number : "))
    
        except ValueError:
            print("please enter valid number...")
            input_1 =int(input("please enter 1st number : "))
            
        try:
            input_2 =int(input("please enter 2Nd number : "))
            
            
            try:
                if input_2<1:
                    print("inside zero check")
                    raise Exception("Sorry, no numbers below zero")
            except Exception:
                print("please enter positive non zero number...")
                input_2 =int(input("please enter 2Nd number : "))
    
    
            try:
                 if input_2>1000:
                     raise MemoryError("Sorry, no numbers above 1000")
            except MemoryError:
                 print("please enter number below 1000...")
                 input_2 =int(input("please enter 2Nd number : "))
    
                
        except ValueError:
             print("\nplease enter valid number...")
             input_2 =int(input("please enter 2Nd number : "))
    
            
    
            
     
        
        operation_input =input("""please enter operation ,for addition enter '+' , 
                               for sub enter '-' , 
                               for multiplication enter '*' , 
                               for division enter '/' : """)
        
        
        
        if operation_input=="+":
            # addition
            
            addition_value=input_1+input_2
            print("Addition is :", addition_value)
        
        elif  operation_input=="-":
            # subtraction
            sub=input_1-input_2
            print("Sub is :", sub)
        
        elif  operation_input=="*":
            # multiply
            mult=input_1*input_2
            if mult>1000:
                raise MemoryError("Sorry, multiplication is above memory limit above 1000")
          
            print("Mult is :", mult)
        
        
        elif  operation_input=="/":
            # division
            div=input_1/input_2  
            print("Div is :", div)
        
            
        else:
            print("invalid operation input")
        
        
        
    except:
        print("something went wrong...")
        pass