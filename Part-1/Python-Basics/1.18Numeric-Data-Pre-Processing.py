# importing the dependies

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


# data collecction and pre-processing



# loading the data from csv file to a pandas dataframe

diabetes_data=pd.read_csv('file path')
diabetes_data.head()

# number of rowa and columns

diabetes_data.shape

diabetes_data.describe() # statistical measures of the dataframe

# spliting the data into feature and target

X=diabetes_data.drop(columns='Column-name',axis=1) # 0 for row, 1 for column.
Y=diabetes_data['column-name']


print(X)
print(Y)


# Standidaization (transforming all the values in a common range)

scaler=StandardScaler()
standardized_data=scaler.fit_transform(X) # transforming all the values in a common range
print(standardized_data)


X=standardized_data
print(X)

# spliting dataset into training data and testing data

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=2)
print(X.shape,X_train.shape,X_test.shape)
print(Y.shape,Y_train.shape,Y_test.shape)