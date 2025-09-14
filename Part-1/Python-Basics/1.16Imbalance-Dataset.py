# A dataset with an unequal class distribution

# importing the libraries


import numpy as np
import pandas as pd


# loading the dataset to the pandas dataframe

credit_card_data=pd.read_csv('File Path')
credit_card_data.head()
credit_card_data.tail()


# analyze the distribution of classes

credit_card_data['column-name'].value_counts() # males=>284314.female=>495  (imbalanced dataset)



# separating the legit and fraudulent transaction

legit=credit_card_data[credit_card_data.Class==0]
fraud=credit_card_data[credit_card_data.Class==1]


print(legit)
print(fraud)

print(legit.shape) # (284315,31)
print(fraud.shape) # (492,31)



# under-Sampling



legit_sample=legit.sample(n=492) # 492 random values from the dataset 'legit'
legit_sample.shape


# Concatenate the Two Dataframes

new_dataset=pd.concat([legit_sample,fraud],axis=0) # axis=>0 ,one after the other.axis=>1 one after the other.
new_dataset.head()
new_dataset.tail()
new_dataset['column-name'].value_counts() # 0=492,1=492