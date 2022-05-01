# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 17:50:01 2021

@author: Vinayak
"""

sample_list = [1,3,5,7,8]

sample_list_9 = [980,8]


sample_list_2 = ["a","v","t"]

sample_list_3= ["a",4,9.5]

print("l1",sample_list)
print("l2",sample_list_2)
print("l3",sample_list_3)



sample_list_2[-1]


sample_list.append(100)


sample_list[4]

# list_name.insert(index,value)
sample_list.insert(4,2000)

# list_name.pop(index)
sample_list.pop(4)

# del list_name[index]
del sample_list[4]

# list_name.remove(value)

sample_list.remove(2000)


input3_0="sadf_"

output_addition=sample_list_9+sample_list
print(output_addition)


sample_list.index(2000)




summation=sum(output_addition)


list3=["Vinayak","Mahesh","arvind","Aparna","Anirudh"]

length_of_list3=len(list3)



range_list=list(range(0,100))

for i in range(0,len(sample_list)):
    print("index : ", i)
    print("value : ",sample_list[i])
    


sample_list.reverse() # reverse lsit itself

sample_list[::-1]   # outputs revserse


sample_list.sort() # sort list itself
