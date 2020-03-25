import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from DataEngineering import *


df = pd.read_csv('Burmasupermarket_sales.csv')
df = dataEngineering(df)


X = df.drop(columns=['InvoiceID','UnitPrice','Quantity',
	                 'Datetime','Total','GrandTotal','Rating'])
y = df['GrandTotal']

print(X.info())

kf = KFold(n_splits=5)
lr_acc = []
svr_acc = []
dt_acc = []
counter = 1
for train_index, test_index in kf.split(df):
	X_train, X_test = X.iloc[train_index,:], X.iloc[test_index,:]
	y_train, y_test = y.iloc[train_index], y.iloc[test_index]
	
	lr = LinearRegression().fit(X_train, y_train)
	lr_acc.append(lr.score(X_test, y_test))

	svr = SVR().fit(X_train, y_train)
	svr_acc.append(svr.score(X_test, y_test))

	dt = DecisionTreeRegressor().fit(X_train, y_train)
	dt_acc.append(dt.score(X_test, y_test))

print(lr_acc)
print(svr_acc)
print(dt_acc)

