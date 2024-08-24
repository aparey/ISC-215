#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 11:36:22 2023

@author: parey69
"""

#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import dataset
dataset = pd.read_csv('DataSetTwo.csv')

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

#split into a test and training set
from sklearn.model_selection import train_test_split
tts =train_test_split
x_train,x_test,y_train,y_test = tts(x,y,test_size=0.2, random_state=1)

#create and train regressor
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)
predictions = regressor.predict(x_test)


#visualize test data
plt.scatter(x_train,y_train,color ='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.xlabel("Years Experience(Training set)")
plt.ylabel("Salary")
#plt.show()
plt.savefig('TrainingsetData.pdf')
