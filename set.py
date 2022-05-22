# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 10:54:57 2022

@author: Vinayak
"""



import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--arg", required=True, help="test argument for set")
args = vars(ap.parse_args())
print(args)

dictionary={1:"f",2:"t",3:"y"}

dictionary[1]

s={1,2,3,4,5789}

set2={1,2,2,2,3,4,5,6,6,8,9,2,6}

print(set2 , args.get("arg"))

list_1=[1,2,2,2,3,4,5,6,6,8,9,2,6]

uniq_list=set(list_1)