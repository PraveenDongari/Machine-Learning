# Data Standardization : The process of standardizing the data to a common format and common range.



import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


# loading  the dataset

dataset=sklearn.datasets.load_breast_cancer

print(dataset) # dataframe




# loading the data to a pandas dataframe


df=pd.DataFrame(dataset.data,columns=dataset.feature_names)

df.head()

df.shape()

X=df
Y=dataset.target
print(X)
print(Y)


# Spliting data into Training Data and Test Data

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=3) # test_size=20% of the total data.

print(X.shape,X_train.shape,X_test.shape)

print(dataset.data.std()) # Standard deviation

scaler=StandardScaler()

scaler.fit(X-X_train)

X_train_Standardized=scaler.transform(X_train)

print(X_train_Standardized)



