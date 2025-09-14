# Dataset=Training Data + Testing Data.



# importing the libraries


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


# loading the diabetes dataset to a pandas Dataframe


diabetes_dataset=pd.read_csv('File path')
diabetes_dataset.head()
diabetes_dataset.shape
diabetes_dataset.describe() # getting the statistical measures of the data
diabetes_dataset['column-name'].value_counts() # 0=500,1=268 ,0=> non-diabetic and 1=> diabetic
diabetes_dataset.groupby('column-name').mean()

# seperating the data and labels

X=diabetes_dataset.drop(columns='Outcome',axis=1) # Outcome=> Column name
Y=diabetes_dataset['Outcome']

print(X) # X does not contain the column(Outcome)
print(Y) # Y only contains Column(Outcome)


# Standardization (need to learn-After)


# Spliting the data into training data and testing data


X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=2) # test_size => size of test dataset

print(X.shape,X_train.shape,X_test.shape) # (768,8) => (614,8) (154,8)

