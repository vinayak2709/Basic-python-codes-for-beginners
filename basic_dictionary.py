# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 16:55:44 2021

@author: Vinayak
"""

sample=[None]
sample2=[]

test_dictionary={}
test_dictionary={1:"1st","V":"Vinayak"}

test_dictionary["V"]

test_dictionary.get("y")




if test_dictionary.get("V"):
    print("present")
    
else:
    print("key absent")
    
    
    
    
    
# adding or changing the values

test_dictionary["A"]="Amar"

test_dictionary["V"]="Victor"



print(test_dictionary)


print(type(test_dictionary))


# test_dictionary.keys()


keys=list(test_dictionary.keys())


print(type(keys))




# test_dictionary.values()


values=list(test_dictionary.values())


print(type(values))




# table




""" students -> columns - name , studentid , school , percentage_marks"""

students=[{"name": "vinayak"     , "studentid":   "3"  , "school " : "sharda" ,"percentage_marks":"80%"   } ,
          
          {"name": "Arvind"     , "studentid":   "5"  , "school " : "sharda" ,"percentage_marks":"80%"   },
          {"name": "Tejal"     , "studentid":   "7"  , "school " : "lord" ,"percentage_marks":"90%"   }]
       