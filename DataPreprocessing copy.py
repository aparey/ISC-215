# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:59:45 2023
Lab 2 Data Preprocessing in Python



@author: tcullen
"""

#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import dataset

dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
z = dataset.iloc[:,1:2].values

#Replace missing Data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer.fit(x[:,1:-1])
x[:,1:-1] = imputer.transform(x[:,1:-1])

#Encode Categorical Data

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
x = np.array(ct.fit_transform(x))

