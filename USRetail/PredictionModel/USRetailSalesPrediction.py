import pandas as pd
import numpy as np
import MacroPrediction as mp
import Store


# Read all data and join the data 
data_features = pd.read_csv('../Data/Refined/features_dataset_refined.csv')
data_sales = pd.read_csv('../Data/Original/sales_dataset.csv')
df_sales = data_sales[['Store','Date','Weekly_Sales']] \
                     .groupby(['Store','Date']).sum().reset_index()

df = data_features.merge(df_sales[['Store','Date','Weekly_Sales']] \
	                             .groupby(['Store','Date']).sum() \
	                             .reset_index(),on=['Store','Date'],
	                             how='left')
df_holiday = pd.read_csv('../Data/Refined/IsHoliday.csv')



# Obtain the store labels from the data set
features = ['Temperature','Fuel_Price','CPI','Unemployment','IsHoliday']
label = 'Weekly_Sales'
columns_pred = ['Temperature','Fuel_Price','CPI','Unemployment']



model_dict = {}
stores_list = df['Store'].unique().tolist()
for store in stores_list:
	df_currStore = df[df['Store']==store]
	df_currStore = df_currStore[['Date']+features+[label]]
	df_currStore['Date'] = pd.to_datetime(df_currStore['Date'], format='%d/%m/%Y')
	data_sales_currStore = data_sales[data_sales['Store']==store]


	currStore = Store.Store(store, df_currStore, features, label, data_sales_currStore)
	# Extract the available Macro Data of the prediction period
	X_pred = df_currStore[['Date','Weekly_Sales']+features]
	X_pred = X_pred[X_pred['Weekly_Sales'].isnull()]
	# Predict the unknown Macro Data
	X_pred2 = mp.predictColumns(df_currStore.drop('IsHoliday', axis=1), columns_pred,
		                       2014, df_holiday)
	X_pred = pd.concat([X_pred, X_pred2])
	X_pred = X_pred[['Date']+features].sort_values(by='Date')
	# Make prediction
	currStore.predict(X_pred)
	# Store the result in model_dict
	model_dict[store] = currStore

# Gather results
features_future = [] # Feature data (Macro data)
prediction_dept = [] # Department wide
prediction_store = [] # Store wide
for store in stores_list:
	features_future.append(model_dict[store].getXPredYPred())
	prediction_dept.append(model_dict[store].getDeptPred())
	prediction_store.append(model_dict[store].getYPred())

# Save Feature data
features_future = pd.concat(features_future)
features_future.to_csv('Results/features_prediction.csv', index=False)

# Save department wide weekly sales
prediction_dept = pd.concat(prediction_dept)
prediction_dept.to_csv('Results/sales_prediction.csv', index=False)

# Save Store wide weekly sales
prediction_store = pd.concat(prediction_store)
prediction_store.to_csv('Results/sales_store_prediction.csv', index=False)
