# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 1:02 pm
Adi Parey
Lab1

@author: aparey
"""

#This will be the program that interfaces

import converter
temp = int(input("Enter a temperature to convert:"))
print("Enter c for Celsius or f for Fahrenheit")
scale = input("Enter the scale you want to convert")

newTemp = converter.convertTemp(temp,scale)
print("The new temperature is: "+ str(newTemp))

 

