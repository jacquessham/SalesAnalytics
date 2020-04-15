import pandas as pd
import numpy as py
from sklearn.tree import DecisionTreeRegressor


depth = 3
n_estimator = 10

class Store:
	def __init__(self, df, features, label, df_sales):
		self.df = df.dropna()
		self.X_train = self.df[features]
		self.y_train = self.df[label]
		self.df_sales = df_sales
		self.deptDisb = self.deptDisb()
		self.dt = self.modeltraining()
		self.pred_store = None

	def deptDisb(self):
		dept_list = self.df_sales['Dept'].unique().tolist()
		dept_proportion = {}
		total_sales = self.df_sales['Weekly_Sales'].sum()
		for dept in dept_list:
			df_temp = self.df_sales[self.df_sales['Dept']==dept]
			dept_proportion[dept] = self.df_sales['Weekly_Sales'].sum()/total_sales
		return dept_proportion

	def modeltraining(self):
		dt = DecisionTreeRegressor(max_depth=depth)
		dt = dt.fit(self.X_train, self.y_train)
		return dt

	def predict(self, df_X):
		date = df_X.Date.tolist()
		X = df_X.drop('Date',axis=1)
		pred = self.dt.predict(X)
		self.pred = pd.DataFrame({'Date':date, 'Weekly_Sales':pred})

	def getPred(self):
		return self.pred
