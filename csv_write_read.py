# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 16:05:12 2021

@author: Vinayak
"""
# csv read

import pandas as pd 
   
# list of name, degree, score
nme = ["Vinayak", "pankaj", "sudhir", "Geeku"]
deg = ["Mtech", "BCA", "M.Tech", "MBA"]
scr = [80, 40, 80, 98]
   
# dictionary of lists 
dict_1 = {'name': nme, 'degree': deg, 'score': scr} 
     
df = pd.DataFrame(dict_1)
  
# saving the dataframe
df.to_csv('C://Users//Vinayak//Desktop/Extra//file2.csv')




# csv read

df2=pd.read_csv('file2.csv')
print(df2)






# excel write


import pandas as pd

# dataframe Name and Age columns
df = pd.DataFrame({'Name': ['A', 'B', 'C', 'D'],
                   'Age': [10, 0, 30, 50]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('C://Users//Vinayak//Desktop/Extra//vinayak_demo.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1', index=False)



# Close the Pandas Excel writer and output the Excel file.
writer.save()