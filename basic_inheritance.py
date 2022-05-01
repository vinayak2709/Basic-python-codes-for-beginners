# -*- coding: utf-8 -*-
"""
Created on Sun May  1 10:26:41 2022

@author: Vinayak
"""

# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("may or may not Swim")
        
    def feathers(self):
        print("have feathers")
        
    def fly(self):
        print("mostly all fly")
        
    
    def run(self):
         print("just walk or Run")
    
   

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        # super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")
    def fly(self):
        print("can not fly")
   

    def run(self):
        print("Run faster")
    def swim(self):
        print("Swim faster")

#
        

# child class
class Ostrich(Bird):

    def __init__(self):
        # call super() function
        # super().__init__()
        print("Ostrich is ready")

    def whoisThis(self):
        print("Ostrich")

    def run(self):
        print("Run faster")
    
    def fly(self):
        print("can not fly")
        
    def swim(self):
        print("Do not swim")


class Peacock(Bird):
    
     def __init__(self):
         # call super() function
         # super().__init__()
         print("Peacock is ready")
    
     def whoisThis(self):
         print("Peacock")
            
     def swim(self):
         print("Do not swim")



peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
peggy.feathers()
peggy.fly()




oggy = Ostrich()
oggy.whoisThis()
oggy.swim()
oggy.run()
oggy.feathers()
oggy.fly()



peacky=Peacock()
peacky.whoisThis()
peacky.swim()
peacky.run()
peacky.feathers()
peacky.fly()

