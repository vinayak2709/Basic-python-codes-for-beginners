# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:54:38 2022

@author: Vinayak
"""

"""
prime numberbetween 2 to 50

"""
number=27


if number %2==0:
    print(number ,"not prime")
elif number % 3==0 :
    print(number ,"not prime")
elif number% 5==0:
    print(number ,"not prime")
elif number% 7==0:
    print(number ,"not prime")
else:
    print(number ,"prime")
    
    
    
    
for i in [2,3,5,7]:
        
    if number %i==0:
        print(number ,"not prime")
        break
else:
    print(number ,"prime")
    
  


""" for all number"""

number=31
count=1
for i in range(2,number):
    
    if number %i==0:
        break
    count+=1

if count>=number-1:
    print(number,"prime number..")
else:
    print(number,"not prime number..")







"""
or"""


number=27

for i in range(2,number):
    
    if number %i==0:
        print(number,"not prime number..")

        break
    count+=1

else:
    print(number," prime number..")
    
        
    """ or """
    
    
    

count=1
number=31
if number==4:
    print(number,"not prime number..")
else:
    for i in range(2,int(number/2)):
        
        if number %i==0:
            print(number,"not prime number..")
            break
        count+=1
    
    else:
        print(number," prime number..")
        
        


