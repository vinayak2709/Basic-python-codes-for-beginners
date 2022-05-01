# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 20:02:06 2021

@author: Vinayak
"""

class A:
    
    def __init__(self):
        self.name="A"
        self.att="A's attribute"
        self.a="pass a"
        print("THis is ",self.name)
        
        

class B:
    
    def __init__(self):
        self.name="B"
        self.att="B's attribute"
        self.b="pass b"

        print("THis is ",self.name)
        
        
        
        
        
        
        


class C(A): # single 
    
    def __init__(self):
        self.name="C"
        self.att="Cs attribute"
        print("THis is ",self.name)
 
    
class D(C): # multi level
      def __init__(self):
          self.name="D"
          self.att="Ds attribute"
          print("THis is ",self.name)
   
      


class M(A,B): # Multiple
    
    def __init__(self):
        self.name="C"
        self.att="Cs attribute"
        print("THis is ",self.name)
    
    

a_obj=A()
obj=C()

obj.att
