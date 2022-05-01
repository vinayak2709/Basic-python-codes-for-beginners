# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 18:55:24 2021

@author: Vinayak
"""

class Bird:
    
    def __init__(self):
        print("bird init")
    
    def intro(self):
        print("There are many types of birds.")
  
    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
       
    def __init__(self):
        print("sparrow init")
 
    
    def flight(self):
        print("Sparrows can fly.")
  
    
class ostrich(Bird):
       
    def __init__(self):
        print("ostrich init")
 
  
    def flight(self):
        print("Ostriches cannot fly.")
  
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
  
obj_bird.intro()
obj_bird.flight()
  
obj_spr.intro()
obj_spr.flight()
  
obj_ost.intro()
obj_ost.flight()
