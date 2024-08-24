#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 12:58:32 2023

@author: parey69
"""
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import dataset
dataset = pd.read_csv('Startup_Data_Set.csv')


#Split the dataset into dependent and independent variables
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[3])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

#Avoid the dummy variable trap
x = x[:,1:]

#Split the dataset into a training set and a test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 1)

#Train the regressor
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

profit_predictions = regressor.predict(x_test)

np.set_printoptions(precision=2)
print(np.concatenate((profit_predictions.reshape(len(profit_predictions),1),y_test.reshape(len(y_test),1)),1))

#Add constants at the beginning
import statsmodels.api as sm
x = np.append(arr = np.ones((50,1)).astype(int),values =x,axis =1)

x_optimal = x[:,[0,1,2,3,4,5]]
x_optimal = x_optimal.astype(np.float64)

regressor_Opt = sm.OLS(endog = y,exog=x_optimal).fit()
regressor_Opt.summary()

#Second iteration
x_optimal = x[:,[0,1,3,4,5]]
x_optimal = x_optimal.astype(np.float64)

regressor_Opt = sm.OLS(endog = y,exog=x_optimal).fit()
regressor_Opt.summary()

#Third iteration
x_optimal = x[:,[0,3,4,5]]
x_optimal = x_optimal.astype(np.float64)

regressor_Opt = sm.OLS(endog = y,exog=x_optimal).fit()
regressor_Opt.summary()

#Fourth iteration
x_optimal = x[:,[0,3,5]]
x_optimal = x_optimal.astype(np.float64)

regressor_Opt = sm.OLS(endog = y,exog=x_optimal).fit()
regressor_Opt.summary()
