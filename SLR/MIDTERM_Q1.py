import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import dataset
dataset = pd.read_csv('DataSetOne.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

#Replace missing Data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])

#Encode Categorical Data

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
x = np.array(ct.fit_transform(x))

#Encode the dependednt variable
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

#Split into a test and training set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=1)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train[:,4:] = sc.fit_transform(x_train[:,4:])
x_test[:,4:] = sc.transform(x_test[:,4:])