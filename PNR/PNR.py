#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 13:15:57 2023

@author: parey69
"""


#Import the libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Warranty_Data_Set.csv')

#Make dependent and independent variables
x = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,-1].values

#Train a linear model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x,y)

#Create a polynomial Regressor
from sklearn.preprocessing import PolynomialFeatures
Poly_Reg = PolynomialFeatures(degree=4) #We will be changing this
x_poly = Poly_Reg.fit_transform(x)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly,y)

#Visualize the linear model
plt.scatter(x,y,color = 'red')
plt.plot(x,regressor.predict(x),color = 'blue')
plt.plot("Linear Model")
plt.plot("Item covered")
plt.show()

#Visualize the polynomial models
plt.scatter(x,y,color = "purple")
plt.plot(x,lin_reg_2.predict(Poly_Reg.fit_transform(x)),color = "orange")
plt.title("Polynomial Model 4 D")
plt.xlabel("item covered")
plt.ylabel("Cost")
plt.show()


