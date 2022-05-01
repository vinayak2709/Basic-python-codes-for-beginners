# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 17:07:57 2021

@author: Vinayak
"""


class Student:
    Total_marks=100   # class var/ static var
    my_school="abc high school"   # static var
    static_var="success"

    def __init__(self,name_value="Vinayak",roll_value="INd1245"):  # by default call when obj is created - constructor
        self.name=name_value # instance var
        self.roll=roll_value
      
    
    
    def function_0():  # static method
        print("function_0_method")
 
      
    def function_1(self):  # instance
    
        self.test="passed"
        print("function_1_method")
        
        
       
test_obj=Student("Vinayak",235)        
obj_2=Student(roll_value=12913,name_value="Arvind")
print(type(obj_2))

obj_2.my_school

obj_2.name

obj_2.roll

obj_2.function_1()

""" error after below statement  """
# obj_2.function_0()

"""No error after below statement  """
Student.function_0()


obj_2.test

""" error after below statement  """
# Student.function_1()

""" No error after below statement  """
obj_2.function_1()


obj_2.test

obj_2.Total_marks


obj_3=Student("Seema",32346)

obj_3.function_1()

obj_3.test



Student.Total_marks=200  # changing class variable to all


Student.name="ani"   # will not work

obj_3.Total_marks

obj_2.name


Student.function_0()
Student.function_0.static_var



class Motorola:
    
    def __init__(self,display_size,cpu="basic"):
        self.display_size=display_size
        self.cpu=cpu
        print("constructor called")
        
    def show_details(self):
        print(self.display_size,self.cpu)
        
moto_obj_g3=Motorola("5.5")

moto_obj_g3.show_details()



moto_obj_g5=Motorola("6",cpu="snapdragon")

moto_obj_g5.show_details()



class MotoG3(Motorola):
    
    def __init__(self):
        
        super().show_details


a=MotoG3()
