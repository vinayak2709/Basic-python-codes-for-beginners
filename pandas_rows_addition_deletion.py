# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 15:49:12 2021

@author: Vinayak
"""

import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])





dictionary={'one_col':[10,20,30], 'two_col':[1000,0,30]}

df = pd.DataFrame(dictionary)

dictionary2=[{'one_col':10000, 'two_col':10456546},{'one_col':2034 ,'two_col':23235},{'one_col':323520 ,'two_col':230}]

df2 = pd.DataFrame(dictionary2)


df3 = df.append(df2)
print(df3)
df3=df3.reset_index()

df5 = df3.drop(0)   # 1,2 and 5,6 dropped



