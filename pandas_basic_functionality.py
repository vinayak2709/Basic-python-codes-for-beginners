# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 15:51:44 2021

@author: Vinayak
"""


import pandas as pd
import numpy as np


s1 = pd.Series()

s = pd.Series(np.random.randn(4))
print("The axes are:")
print(s.axes)

print(s.empty)

print(s.ndim)

print(s.size)

print(s.values)


print(s.head(2))

print(s.tail(2))


list1 = np.array(['a', 'b','c','d'])
type(list1)
b = pd.Series(list1)

# dic = {'anx': 1,'bnx': 2, 'cnx':3}
# s = pd.Series(dic)
# df = pd.DataFrame(dic)
# print(s)

s = pd.Series([1,2,3,4], index=['x','y','z', 'r'])


# data frame basic methods


# Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

# Create a DataFrame
df = pd.DataFrame(d)
print("The transpose of the data series is:")
print(df.T)

print(df.ndim) # dimension
print(df.shape) # shape
print(df.size) # total size