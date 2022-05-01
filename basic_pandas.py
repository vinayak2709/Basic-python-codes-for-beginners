# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 20:36:52 2021

@author: Vinayak
"""

import pandas as pd
import numpy as np
 

number_of_rows=5
number_of_col=3

matrix_value=np.random.randn(number_of_rows, number_of_col)




df = pd.DataFrame(matrix_value, index=['row_1', 'row_2', 'row_3', 'row_4',
'row_5'],columns=['one_column', 'two_column', 'three_column'])






list_1=[45,7,2,"name"]
df_list = pd.DataFrame(list_1)




dictionary={'one_col':[10,20,30], 'two_col':[1000,0,30]}
# dictionary=[{'one_col':10, 'two_col':1000},{'one_col':20 ,'two_col':0},{'one_col':30 ,'two_col':30}]

df = pd.DataFrame(dictionary)

print(df.replace({1000:10,2000:60}))








#import the pandas library

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

print(df)

