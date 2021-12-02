# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 21:00:01 2021

@author: Vinayak
"""

import sys


list_f=[2,4]

sample_tuple1=(2,4)
list_f=tuple(list_f)

list_f=list(list_f)
sys.getsizeof(list_f)


a=10
b=10

print(id(b))