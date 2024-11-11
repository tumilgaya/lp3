# -*- coding: utf-8 -*-
"""Untitled34.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pYePnIAEb_Zp9qD5ZS0_z7f7P6_Ky95K
"""

import pandas as pd
import numpy as np

df = pd.read_csv('Churn_Modelling.csv')

df.head()

df.isna().sum()

df.head()

x = df[['CreditScore','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary']]
y = df['Exited']

from sklearn.preprocessing import StandardScaler
model = StandardScaler()
x = model.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.neural_network import MLPClassifier
model = MLPClassifier(hidden_layer_sizes=(100,100,100),max_iter=100 , random_state=12 ,activation='relu')
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

from sklearn.metrics import ConfusionMatrixDisplay
ConfusionMatrixDisplay.from_predictions(y_test,y_pred)

