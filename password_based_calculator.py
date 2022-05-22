# -*- coding: utf-8 -*-
"""
Created on Sun May 22 10:49:01 2022

@author: Vinayak
"""


""" 
Calculator with operator input and number input -loop operation
"""


import argparse
import os
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-p", "--password", required=True, help="password argument for calculator")


ap.add_argument("-f", "--first", required=True, help="1st number argument for calculator")

ap.add_argument("-s", "--second", required=False, help="2nd number argument for calculator")

args = vars(ap.parse_args())
print(args)

count=1
password=os.environ.get("USERNAME")

if args.get("password"):
    while(count <4):
        if args.get("password") != password :
            print("invalid password please enter correct password... : ")
            password_value =input()
            count+=1
            
            if password_value==password:
                break
        
    else:
        print("maximum password count exceeded..")
        exit(0)
        
        

while(True): 
    
    input_1 =int(args.get("first"))
    try:
        
        input_2 =int(args.get("second"))
    except:
        
        input_2=1
        print(input_2)
        
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
        
        

    
    
    
