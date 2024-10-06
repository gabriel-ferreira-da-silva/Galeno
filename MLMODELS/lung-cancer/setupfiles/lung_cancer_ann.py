# -*- coding: utf-8 -*-
"""lung-cancer-ann.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xXaouBT1Rzw5MRN-t3auGJjPFvj7p4OO
"""

import pandas as pd

df = pd.read_csv('lung-cancer-dataset.csv')

df.head()

import seaborn as sns
import matplotlib.pyplot as plt


df['GENDER'] = df['GENDER'].map({'M': 1, 'F': 0})
df['LUNG_CANCER'] = df['LUNG_CANCER'].map({'YES': 1, 'NO': 0})

nc_df = df[df['LUNG_CANCER'] == 0]

num_no_cancer= (df['LUNG_CANCER']==0).sum()
num_has_cancer= (df['LUNG_CANCER']==1).sum()
times = int (num_has_cancer / num_no_cancer)

for i in range(times):
  df = pd.concat([df, nc_df], ignore_index=True)

correlation= df.corr()
plt.figure(figsize=(10, 8))

sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)


"""# ANN training"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV

x = df.drop('LUNG_CANCER', axis=1)
y = df['LUNG_CANCER']

x = x[sorted(df.columns)]

trainX, testX, trainY, testY = train_test_split(x, y, test_size = 0.2,random_state=42)

sc=StandardScaler()

scaler = sc.fit(trainX)
trainX_scaled = scaler.transform(trainX)
testX_scaled = scaler.transform(testX)

mlp_clf = MLPClassifier(hidden_layer_sizes=(5,2), max_iter = 300,activation = 'relu', solver = 'adam')

mlp_clf.fit(trainX_scaled, trainY)

y_pred = mlp_clf.predict(testX_scaled)

print('Accuracy: {:.2f}'.format(accuracy_score(testY, y_pred)))

print(classification_report(testY, y_pred))

import pickle

with open('lung-cancer-mlp.pkl', 'wb') as file:
    pickle.dump(mlp_clf, file)

with open('lung-cancer-scaler.pkl', 'wb') as file:
    pickle.dump( scaler, file)
