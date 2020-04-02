import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error as rmse
from DataEngineering import *

df = pd.read_csv('Burmasupermarket_sales.csv')
df = dataEngineering(df)

X = df.drop(columns=['GrandTotal'])
y = df['GrandTotal']

kf = KFold(n_splits=5)
lr_acc = []
svr_acc = []
dt_acc = []

lr_rmse =[]
svr_rmse =[]
dt_rmse= []

counter = 1
for train_index, test_index in kf.split(df):
	X_train, X_test = X.iloc[train_index,:], X.iloc[test_index,:]
	y_train, y_test = y.iloc[train_index], y.iloc[test_index]
	
	lr = LinearRegression().fit(X_train, y_train)
	lr_acc.append(lr.score(X_test, y_test))
	lr_rmse.append(rmse(y_test, lr.predict(X_test)))

	svr = SVR().fit(X_train, y_train)
	svr_acc.append(svr.score(X_test, y_test))
	svr_rmse.append(rmse(y_test, svr.predict(X_test)))

	dt = DecisionTreeRegressor().fit(X_train, y_train)
	dt_acc.append(dt.score(X_test, y_test))
	dt_rmse.append(rmse(y_test, dt.predict(X_test)))

print(lr_acc, np.mean(lr_acc))
print(lr_rmse, np.mean(lr_rmse))
print(svr_acc, np.mean(svr_acc))
print(svr_rmse, np.mean(svr_rmse))
print(dt_acc, np.mean(dt_acc))
print(dt_rmse, np.mean(dt_rmse))