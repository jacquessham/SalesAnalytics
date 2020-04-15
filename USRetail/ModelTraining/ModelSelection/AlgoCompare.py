import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor as Dtr
from sklearn.ensemble import RandomForestRegressor as Rfr
from sklearn.metrics import mean_squared_error as rmse


# Read all data and join the data 
data_features = pd.read_csv('../../Data/Refined/features_dataset_refined.csv')
data_sales = pd.read_csv('../../Data/Original/sales_dataset.csv')
data_sales = data_sales[['Store','Dept','Date','Weekly_Sales']] \
                       .groupby(['Store','Date']).sum().reset_index()
df = data_features.merge(data_sales[['Store','Date','Weekly_Sales']] \
	                               .groupby(['Store','Date']).sum() \
	                               .reset_index(),on=['Store','Date'],
	                               how='left').fillna(0)
# Try Store 1 only
df = df[df['Store']==1]


# Split data to features and label
print(df.columns)                         
X = df.drop(['Weekly_Sales','Date','Store'], axis=1)
y = df['Weekly_Sales']


kf = KFold(n_splits=10, shuffle=True, random_state=42)
lr_acc = []
lr_rmse = []
svr_acc = []
svr_rmse = []
dt_acc = []
dt_rmse = []
rf_acc = []
rf_rmse = []

# Train and test the model
for train_index, test_index in kf.split(df):
	X_train, X_test = X.iloc[train_index,:], X.iloc[test_index,:]
	y_train, y_test = y.iloc[train_index], y.iloc[test_index]

	lr = LinearRegression().fit(X_train, y_train)
	lr_acc.append(lr.score(X_test, y_test))
	lr_rmse.append(rmse(y_test, lr.predict(X_test)))
	svr = SVR().fit(X_train, y_train)
	svr_acc.append(svr.score(X_test, y_test))
	svr_rmse.append(rmse(y_test, svr.predict(X_test)))
	dt = Dtr(random_state=42).fit(X_train, y_train)
	dt_acc.append(dt.score(X_test, y_test))
	dt_rmse.append(rmse(y_test, dt.predict(X_test)))
	rf = Rfr(random_state=42).fit(X_train, y_train)
	rf_acc.append(rf.score(X_test, y_test))
	rf_rmse.append(rmse(y_test, rf.predict(X_test)))	


print('Linear Regression')
print(lr_acc, np.mean(lr_acc))
print(lr_rmse, np.mean(lr_rmse))
print('SVC')
print(svr_acc, np.mean(svr_acc))
print(svr_rmse, np.mean(svr_rmse))
print('Decision Tree Regressor')
print(dt_acc, np.mean(dt_acc))
print(dt_rmse, np.mean(dt_rmse))
print('Random Forest')
print(rf_acc, np.mean(rf_acc))
print(rf_rmse, np.mean(rf_rmse))