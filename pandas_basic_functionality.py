# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 15:51:44 2021

@author: Vinayak
"""


import pandas as pd
import numpy as np

"""
import pandas

s1 = pandas.Series()
"""


sample_list=[1,4,9,7,5,9,7,0,7,9 ]

nrad=np.random.randn(9)


n_array=np.array(sample_list)

s1 = pd.Series()


s = pd.Series(n_array)


s = pd.Series(np.random.randn(4))
print("The axes are:")
print(s.axes)

print(s.empty)

print(s.ndim)

print(s.size)

print(s.values)


print(s.head(6))

print(s.tail(2))


list1 = np.array(['a', 'b','c','d'])
type(list1)
b = pd.Series(list1)

# dic = {'anx': 1,'bnx': 2, 'cnx':3}
# s = pd.Series(dic)
# df = pd.DataFrame(dic)
# print(s)

s = pd.Series([12,2,33,4], index=['x','y','z', 'r'])


# data frame basic methods


d = {'Name':['Tom','James','Ricky','Vin','Steve','Smith','Jack'],
   'Age':[25,26,25,23,30,29,23],
   'Rating':[4.23,3.24,3.98,2.56,3.20,4.6,3.8]}


d["Name"][1]


# Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

# Create a DataFrame
df = pd.DataFrame(d)
print("The transpose of the data series is:")
print(df.T)
df2=df.T
print(df2.shape)
print(df.ndim) # dimension
print(df.shape) # shape
print(df.size) # total size



data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)



data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)




data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)

