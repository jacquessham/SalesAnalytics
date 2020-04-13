import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error as rmse


# Read all data and join together
data_features = pd.read_csv('../../Data/Original/features_dataset.csv')
data_sales = pd.read_csv('../../Data/Original/sales_dataset.csv')
data_stores = pd.read_csv('../../Data/Original/stores_dataset.csv')
df = data_sales.merge(data_features.drop('IsHoliday', axis=1),
                      on=['Store','Date'], how='left')
df = df.merge(data_stores, on='Store', how='left')
df = df.drop('Type', axis=1)
# Try Store 1 and Department 1
df = df[(df['Store']==1) & (df['Dept']==1)].fillna(0)

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['Month'] = df['Date'].dt.month
df = pd.concat([df,pd.get_dummies(df['Month'],prefix='Month',
                                     dtype=bool)],axis=1)
df['Day'] = df['Date'].dt.month
df = pd.concat([df,pd.get_dummies(df['Day'],prefix='Day',
                                     dtype=bool)],axis=1)

X = df.drop(['Weekly_Sales','Date'], axis=1)
y = df['Weekly_Sales']

kf = KFold(n_splits=10, shuffle=True, random_state=42)
lr_acc = []
lr_rmse =[]

for train_index, test_index in kf.split(df):
	X_train, X_test = X.iloc[train_index,:], X.iloc[test_index,:]
	y_train, y_test = y.iloc[train_index], y.iloc[test_index]

	lr = LinearRegression().fit(X_train, y_train)
	lr_acc.append(lr.score(X_test, y_test))
	lr_rmse.append(rmse(y_test, lr.predict(X_test)))


print(lr_acc, np.mean(lr_acc))
print(lr_rmse, np.mean(lr_rmse))
