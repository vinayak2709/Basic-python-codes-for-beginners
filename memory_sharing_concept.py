# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 20:25:11 2021

@author: Vinayak
"""


"""
# Memory sharing

"""
var=2
var2=2


var2=3

id(var2)
id(var)


sample_dictionary2={"test":1,"test2":2,"test3":3}


# shallow copy

sample_dictionary3=sample_dictionary2


sample_dictionary2["add_value"]=9

print(sample_dictionary3)
print(sample_dictionary2)

id(sample_dictionary3)
id(sample_dictionary2)




# deep copy


sample_dictionary4=sample_dictionary2.copy()

sample_dictionary2["add__extra_value"]=99

