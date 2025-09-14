# label to numerical value.

# importing the dependies

import pandas as pd
from sklearn.preprocessing import labelEncoder


# Label encoding of breasr cancer dataset



# Loading the data from csv file to pandas dataframe

cancer_data=pd.read_csv('file path')
cancer_data.head()

# finding the count of different labels

cancer_data['diagnosis'].value_counts() # male=321 female=342  diagnosis=column name

# Load the labelEncoder function

label_encode=labelEncoder()

labels=label_encode.fit_transform(cancer_data.diagnosis) # diagnosis=column name


# appending the labels to the DataFrame

cancer_data['target']=labels
cancer_data.head() # 0,1,2,.. etc will be assigned according to the alphabetical order.

cancer_data['target'].value_counts()