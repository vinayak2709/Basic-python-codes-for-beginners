# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:27:00 2022

@author: Vinayak
"""


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

if "apple" in fruits:
    print("present")


newlist=[]
for element in fruits:
    if "a" in element:
        newlist.append(element)


"""
or by list comprehension

"""

newlist2 = [element for element in fruits if "a" in element]

print(newlist)







number_list=list(range(1,100))
even_list=[]

for i in number_list:
    # print(i)
    if i%2==0:
        print(i,"even")
        even_list.append(i)
        
        
        
even_list2=[i for i in number_list if i%2==0]

five_table=[i for i in number_list if i%5==0]


primenumbers=[i for i in number_list if i in [2,3,5,7,11,13,17,19]]
