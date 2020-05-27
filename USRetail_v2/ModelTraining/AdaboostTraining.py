import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error as rmse
from sklearn.model_selection import train_test_split


# Read all data and join the data 
data_features = pd.read_csv('../../USRetail/Data/Refined/features_dataset_refined.csv')
data_features = data_features.drop(['MarkDown1','MarkDown2','MarkDown3',
	                                'MarkDown4','MarkDown5'],axis=1)
data_sales = pd.read_csv('../../USRetail/Data/Original/sales_dataset.csv')
data_sales = data_sales[['Store','Dept','Date','Weekly_Sales']] \
                       .groupby(['Store','Date']).sum().reset_index()
df = data_features.merge(data_sales[['Store','Date','Weekly_Sales']] \
	                               .groupby(['Store','Date']).sum() \
	                               .reset_index(),on=['Store','Date'],
	                               how='left').fillna(0)
# Try all stores
stores = df['Store'].unique()
kf = KFold(n_splits=10, shuffle=True, random_state=42)
acc_list = []
rmse_list = []

for store in stores:
	df_currstore = df[df['Store']==store]
	# Split data to features and label                       
	X = df_currstore.drop(['Weekly_Sales','Date','Store'], axis=1)
	y = df_currstore['Weekly_Sales']
	for train_index, test_index in kf.split(df_currstore):
		X_train, X_test = X.iloc[train_index,:], X.iloc[test_index,:]
		y_train, y_test = y.iloc[train_index], y.iloc[test_index]
		# Using default hyperparameter
		adaboost = AdaBoostRegressor(random_state=42).fit(X_train, y_train)
		adaboost_acc = adaboost.score(X_test, y_test)
		adaboost_rmse = rmse(y_test, adaboost.predict(X_test))
		acc_list.append(adaboost_acc)
		rmse_list.append(adaboost_rmse)

# Print result in R-squ
print('The R-square is:', np.mean(acc_list))
# Print result in RMSE if needed
print('The RMSE is:', np.mean(rmse_list))

