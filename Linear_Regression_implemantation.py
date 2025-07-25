#Linear_Regression_implemantation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files

df = pd.read_csv('taxi_trip_pricing.csv')

df = pd.get_dummies(df, columns=['Time_of_Day'], prefix='TD')
df = pd.get_dummies(df, columns=['Day_of_Week'], prefix='DW')
df = pd.get_dummies(df, columns=['Traffic_Conditions'], prefix='Tc')
df = pd.get_dummies(df, columns=['Weather'], prefix='W')
df['Trip_Distance_km'].fillna(df['Trip_Distance_km'].dropna().median(), inplace=True)
df['Per_Minute_Rate'].fillna(df['Per_Minute_Rate'].dropna().median(), inplace=True)
df['Trip_Duration_Minutes'].fillna(df['Trip_Duration_Minutes'].dropna().median(), inplace=True)
df['Base_Fare'].fillna(df['Base_Fare'].dropna().median(), inplace=True)
df['Passenger_Count'].fillna(df['Passenger_Count'].dropna().median(), inplace=True)
df['Per_Km_Rate'].fillna(df['Per_Km_Rate'].dropna().median(), inplace=True)
df['Trip_Price'].fillna(df['Trip_Price'].dropna().median(), inplace=True)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(df)
df_scaled = pd.DataFrame(scaler.transform(df), columns=df.columns)

y = df_scaled['Trip_Price']
x = df_scaled.drop('Trip_Price', axis=1)
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(x, y, test_size=0.2, random_state=42)

class LinearRegression:
  def __init__(self, learning_rate=0.1, numb_iterations=1000 ):
    self.lr=learning_rate
    self.n_iters=numb_iterations
    self.weights=None
    self.bias=None
  def fit(self, X, y):
    n_samples, n_fitures= X.shape
    self.weights=np.zeros(n_fitures)
    self.bias=0

    for i in range(self.n_iters):
      y_pred=np.dot(X, self.weights)+self.bias

      dw=(1/n_samples)*np.dot(y_pred-y, X)
      db=(1/n_samples)*np.sum(y_pred-y)

      self.weights=self.weights- self.lr*dw
      self.bias=self.bias- self.lr*db


  def predict(self, X):
      y_pred=np.dot(X , self.weights)+self.bias
      return y_pred

lr= LinearRegression()
lr.fit(X_train, y_train)
prediction=lr.predict(X_test)

from sklearn.metrics import r2_score

r2 = r2_score(y_test, prediction)
print("R² Score:", r2)
print(f'R2 Score = {int(r2_score(y_test, prediction) * 100)}%')

#R² Score: 0.7968318756263855
#R2 Score = 79%