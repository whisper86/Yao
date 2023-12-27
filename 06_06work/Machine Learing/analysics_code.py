import warnings

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import model_selection, linear_model, metrics

warnings.filterwarnings("ignore")
# Import data
data = pd.read_csv("archive3/Titanic-Dataset.csv")
# print(data.head())

# Selecting the target column and the feature matrix
y = data['Survived']
X = data.drop(['Survived', 'PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)

# print(X.head())

# print(X.info())

# Separating the feature matrix according to numeric and categorical features

num_feat = X.select_dtypes('number').columns.values
cat_feat = X.select_dtypes('object').columns.values
X_num = X[num_feat]
X_cat = X[cat_feat]
# print(X_num)
# print(X_num.mean())
# print(X_num.std())
# print("\n\n")
# Scaling the numeric features using standardization
X_num = (X_num - X_num.mean()) / X_num.std()
# print(X_num.head().mean())
X_num = X_num.fillna(0.103320)
# print(X_num)


# Encoding the categorical features using one_hot encoding
X_cat = pd.get_dummies(X_cat)
 

# Combining processed numeric and categorical features in one feature matrix
X = pd.concat([X_num, X_cat], axis=1)
# print(X)

# Splitting the final dataset into training and testing datasets
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, random_state=0)
cabinDf = pd.DataFrame()

data['Cabin'] = data['Cabin'].map(lambda c: c[0])

cabinDf = pd.get_dummies(data['Cabin'], prefix='Cabin')

print(cabinDf.head())
