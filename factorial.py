# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 19:41:29 2021

@author: Vinayak
"""

""" 
factorial

1! =1
2! =2 *1 =2
3! =3 *2 *1 =6
4! =4 *3*2*1=24
5!=5*4*3*2*1=120 

"""




count=5
factorial=1
while(count>1):
    factorial=factorial * count
    count=count-1
    
print(factorial)







factorial_2=1
count=1
number=3

while(count<=number):

    factorial_2=factorial_2*count
    count+=1
    
print(factorial_2)





# recursive function


def fact(number):    
    if number ==1:
        return 1
    else:
        return number*fact(number-1)
    
fact(4)




number=3

def fact_func(number):
    
    factorial_2=1
    count=1
    
    while(count<=number):
    
        factorial_2=factorial_2*count
        count+=1
        
    print(factorial_2)
    return factorial_2
    



fact_func(3)