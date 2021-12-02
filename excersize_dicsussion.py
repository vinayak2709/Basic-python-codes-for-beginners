# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 15:43:58 2021

@author: Vinayak
"""

name_list=["amar","vinayak","meena","lalit"]

user_input="l"

for name in name_list:
    # print(name)   
    
    if name[0]==user_input:             
        print(name)
########################################

while(True):
    user_input=input("please enter initial alphabet of the name you want to print... : ")
    print(user_input)

    if user_input=="a":
        
        for name in name_list:
            if name[0]==user_input:             
                print(name_list[0])
    elif user_input=="v":
        print(name_list[1])
     
    elif user_input=="m":
        print(name_list[2])
    
    elif user_input=="l":
        print(name_list[3])
        
    else:
        print("invalid input")
        break
    
    user_input2=input("Do you want to continue ? : yes/no : ")
    
    if user_input2=="yes":
        pass
    
    else:
        break

    

