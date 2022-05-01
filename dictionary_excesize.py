# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:05:23 2022

@author: Vinayak
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 16:11:07 2021

@author: Vinayak
"""
""" To make any number of list element to print name with just 1st letter input from user"""


list_dicionary=[{"name":"vinayak","age":29},{"name":"lalit","age":39},{"name":"hitesh","age":49},{"name":"rohit","age":19}]

user_input="l"


def list_initial_search(list_dicionary):
          
    while(True):
        
        user_input=input("please enter initial alphabet of the name you want to print... : ")
        print("\n",user_input)
        
        count=0
        for element in list_dicionary:
            # print(name)   
           
            if element["name"][0].lower()==user_input.lower():             
                print("\n",element)
                break           
            count+=1
    
        if count>=len(list_dicionary):   
            print("invalid input/ alphabet not in names..")
            break
            
        user_input2=input("Do you want to continue ? : yes/no : ")
        
        if user_input2=="yes":
            pass
        
        else:
            break
    
        
list_initial_search(list_dicionary)   
