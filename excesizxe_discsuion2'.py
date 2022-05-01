# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 16:11:07 2021

@author: Vinayak
"""
""" To make any number of list element to print name with just 1st letter input from user"""


name_list=["amar","vinayak","meena","lalit","hitesh","rohit","prashant"]

user_input="l"


def list_initial_search(name_list):
          
    while(True):
        
        user_input=input("please enter initial alphabet of the name you want to print... : ")
        print(user_input)
        
        count=0
        for name in name_list:
           # print(name)   
           
           if name[0].lower()==user_input.lower():             
               print(name)
               break           
           count+=1
    
        if count>=len(name_list):   
            print("invalid input..")
            break
            
        user_input2=input("Do you want to continue ? : yes/no : ")
        
        if user_input2=="yes":
            pass
        
        else:
            break
    
        
list_initial_search(name_list)   
