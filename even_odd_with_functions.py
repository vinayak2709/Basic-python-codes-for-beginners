# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 19:15:20 2021

@author: Vinayak
"""


def even_odd(value):
    if int(value)%2==0:
        print(value,"  is even")
    else:
        print(value,"  is odd")
    

def even_odd_decision2(value):
    if type(value)==dict:
        for k,v in value.items():
            even_odd(v)
        
    elif type(value)==list:
        for i in value:
            even_odd(i)
    elif type(value)==int:
        even_odd(value)
    else:
        print('invalid data...')
    


def even_odd_decision(value):
    
    if type(value)==list:
        for i in value:
            even_odd(i)





# value=35

# value=[3,6,8,2,7]

value="45"

value={"num":2,"num1":3,"num4":6}
even_odd_decision(value)



######  ################   #################

def expo(base,power):
    
    return base**power


expo(2,3)


expo_lam=lambda base ,power :base**power

expo_lam(2,4)




#######  ###########   ###################

def even_odd(value):
    if int(value)%2==0:
        print(value,"  is even")
       
    else:
        print(value,"  is odd")
        
value_list=[3,6,8,2,7]
        
even_odd=lambda value : print(value,"is even") if int(value)%2==0 else print(value,"  is odd")

   
even_odd(5)



################

value_list=[3,5,6,7,9,2]

def even_list(value_list):
    even_list=[]
    odd_list=[]
    for value in value_list:
        if int(value)%2==0:
            print(value,"  is even")
            even_list.append(value)
           
       
    return even_list
        
even_values=even_list(value_list)


even_values2=list(filter(lambda value :value % 2==0 ,value_list))

######  ########## #####  ########
