# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 15:42:00 2021

@author: Vinayak
"""
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df.loc['b']) # index lable
print(df.iloc[1]) # index
print(df[1:4])   # index

print(df["one"])
