# -*- coding: utf-8 -*-
"""
Created on Sun May  1 10:26:16 2022

@author: Vinayak
"""


""" 
# string formatting

name="Ashwini"
print(f"my name is {name}")

print("my name is {}".format(name))
"""



class Computer:

    def __init__(self):
        print("computer_constructor called ")
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(2000)
c.sell()


