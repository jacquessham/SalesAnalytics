import pandas as pd
import numpy as py
from sklearn.ensemble import RandomForestRegressor


class Store:
	def __init__(self, store_num, df, features, label, df_sales):
		self.store_num = store_num
		self.df = df.dropna() # To prevent nan in y_train
		self.X_train = self.df[features] # Pandas DataFrame
		self.y_train = self.df[label] # Pandas DataFrame
		self.df_sales = df_sales
		self.deptDisb = self.deptDisb()
		self.dt = self.modeltraining()
		self.X_pred = None
		self.y_pred = None
		self.y_pred_dept = None

	def deptDisb(self):
		dept_list = self.df_sales['Dept'].unique().tolist()
		dept_proportion = {}
		total_sales = self.df_sales['Weekly_Sales'].sum()
		for dept in dept_list:
			df_temp = self.df_sales[self.df_sales['Dept']==dept]
			dept_proportion[dept] = df_temp['Weekly_Sales'].sum()/total_sales
		return dept_proportion

	def modeltraining(self):
		dt = RandomForestRegressor()
		dt = dt.fit(self.X_train, self.y_train)
		return dt

	def predict(self, df_X):
		self.X_pred = df_X
		date = df_X.Date.tolist()
		X = df_X.drop('Date',axis=1)
		y_pred = self.dt.predict(X)
		# Save store prediction
		self.y_pred = pd.DataFrame({'Date':date, 'Weekly_Sales':y_pred})
		# Calculate and save department sales
		self.y_pred_dept = self.predict_dept()

	def predict_dept(self):
		date_list = self.y_pred.Date.unique()
		dept_list = self.deptDisb.keys()
		prediction = {'Store':[], 'Dept':[],'Date':[],
		              'Weekly_Sales':[], 'IsHoliday':[]}
		df_pred = self.getYPred()
		for dept in dept_list:
			dept_proportion = self.deptDisb[dept]
			for date in date_list:
				df_pred_currDept = df_pred[df_pred['Date']==date]
				weekly_sales = df_pred_currDept['Weekly_Sales'].tolist()[0]
				weekly_sales = round(weekly_sales*dept_proportion,2)
				isHoliday = self.X_pred[self.X_pred['Date']==date] \
				                       ['IsHoliday'].tolist()[0]

				prediction['Store'].append(self.store_num)
				prediction['Dept'].append(dept)
				prediction['Date'].append(date)
				prediction['Weekly_Sales'].append(weekly_sales)
				prediction['IsHoliday'].append(isHoliday)

		return pd.DataFrame(prediction)

	# Getter function of getting store-wide weekly sales
	def getYPred(self):
		result = self.y_pred
		rows = result.shape[0]
		result['Store'] = [self.store_num for _ in range(rows)]
		return result

	def getXPredYPred(self):
		result = self.X_pred.merge(self.y_pred, on='Date', how='inner')
		rows = result.shape[0]
		result['Store'] = [self.store_num for _ in range(rows)]
		return result

	def getDeptPred(self):
		result = self.y_pred_dept
		rows = result.shape[0]
		result['Store'] = [self.store_num for _ in range(rows)]
		return result
