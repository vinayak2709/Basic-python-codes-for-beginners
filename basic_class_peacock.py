# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 17:48:09 2021

@author: Vinayak
"""

class Peacock:
    colour="blue"

    def __init__(self,wings_value=False,feathers_value=False,hieght_value=0):
        self.wings=wings_value
        self.feathers=feathers_value
        
        self.hieght=hieght_value
        
        
    
    def details(self):
        print("wings ::: ",self.wings)
        print("feathers ::: ",self.feathers)
        print("hieght ::: ",self.hieght)


    
flying_bird=Peacock()
crawling_bird=Peacock()
child=Peacock()


print(child.hieght)


crawling_bird.hieght=10
print(crawling_bird.hieght)

flying_bird.wings=True
flying_bird.feathers=True
flying_bird.hieght=20
print(flying_bird.wings)



flying_bird.details()

crawling_bird.details()
child.details()




""" OR """



    
flying_bird=Peacock(wings_value=True,feathers_value=True,hieght_value=20)
crawling_bird=Peacock(hieght_value=10)
child=Peacock()



flying_bird.hieght=30

flying_bird.details()

crawling_bird.details()
child.details()

