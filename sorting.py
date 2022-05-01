# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 18:30:48 2021

@author: Vinayak
"""




"""swap """
a=10
b=7

temp=a
a=b
b=temp


import time
# 


prev=time.time()
i=0

test_list=[2,3,5,7,9,1,456,788,23,6,8456,456,346,346,7,8567,13]
sorted_list=[]
i=4


for j in range(len(test_list)):
    
    for i in range(len(test_list)):
        
        if i>=len(test_list)-1:
            break
        if test_list[i]<test_list[i+1]:  
            pass     
        else:
            temp=test_list[i]
            test_list[i]=test_list[i+1]
            test_list[i+1]=temp
        print(test_list)
        
        
# prev=time.time()
# test_list.sort()
 
# after=time.time()

# print((after-prev)*10000000)       



print((time.time()-prev)*100000)






list2 = [1,3,42,5,6,8,9,4]
for i in range(len(list2)):
    for j in range(i+1,len(list2)):
       print(i,j)

       if list2[i]>list2[j]:
            list2[i],list2[j]=list2[j],list2[i]
       print("after_swaP :",list2)
print(list2)

