# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 15:25:18 2021

@author: Vinayak
"""
import sys
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
type(data)
s = pd.Series(data)

# custom index
print(s)

s = pd.Series(data,index=[100,101,102,103])
print(s)

# Dict

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print(s)




# NAN

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print(s)



# accessing

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first element
print(s[0])
print(s[:3])
print(s['a'])




# Series - size fix , data mutable ,size immutable 
# Dataframe - size dynamic , data mutable ,size mutable 


# data frame use

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)



