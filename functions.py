# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 19:08:10 2021

@author: Vinayak
"""

"""def function_name(arguments):
    statements
    
    
    """
glob_var=4
def cube(number):
    global glob_var
    glob_var=7

    local_var=number
    cube_value=number * number * number
    print(local_var,"local var always work only inside of function...")
    print(glob_var, "global var inside of function...")

    return cube_value


value=cube(3) 


""" no accesible outside function """
# print(local_var,"local var always work only inside of function...")

print(glob_var, " outside of function...")


print(cube(9))
    


""" home work """


""" 
factorial

1! =1
2! =2 *1 =2
3! =3 *2 *1 =6
4! =4 *3*2*1=24
5!=5*4*3*2*1=120 

"""
"""factorial function .... if factorial(3) should give 6

 """


"""

exponential(base,power)

exponential(2,3)

should give you 8.

hint : user 2**3  gives 8 logic 


"""


var=3**2

    
sorted_list=None

# user defined function

def sorting(list2):
        
    for i in range(len(list2)):
        for j in range(i+1,len(list2)):
           print(i,j)
    
           if list2[i]>list2[j]:
                list2[i],list2[j]=list2[j],list2[i]
           print("after_swaP :",list2)
    return list2




list2222 = [1,3,4,5,6,8,9,4,356,89,2,5678,2,2]

sorted_list=sorting(list2222)


# internal function
list2222.sort()






def sorting_function(test_list):
    
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
    return test_list
    
            
      
           
test_list2=9      


test_list2=[1234,6,8,234,0,67834,7346,3,6,5,34,34,67,2]
sorted_list2=sorting_function(test_list2)







