# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:03:16 2022

@author: Vinayak
"""


import argparse
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-p", "--password", required=True, help="password argument for calculator")



args = vars(ap.parse_args())
print(args)

count=1

password=os.environ.get("USERNAME")

if args.get("password"):
    while(count <4):
        if args.get("password") != password :
            print("invalid password please enter correct password... : ")
            password_value =input()
            count+=1
            
            if password_value==password:
                break
        
    else:
        print("maximum password count exceeded..")
        exit(0)
        
        