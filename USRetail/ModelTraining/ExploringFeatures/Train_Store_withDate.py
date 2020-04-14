import pandas as pd
import numpy as np
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error as rmse
from sklearn.model_selection import train_test_split


# Read all data and join the data 
data_features = pd.read_csv('../../Data/Original/features_dataset.csv')
data_sales = pd.read_csv('../../Data/Original/sales_dataset.csv')
data_sales = data_sales[['Store','Dept','Date','Weekly_Sales']] \
                       .groupby(['Store','Date']).sum().reset_index()
df = data_features.merge(data_sales[['Store','Date','Weekly_Sales']] \
	                               .groupby(['Store','Date']).sum() \
	                               .reset_index(),on=['Store','Date'],
	                               how='left').fillna(0)
# Try Store 1 only
df = df[df['Store']==1]
df_noDate = df

# Split date to month and day columns
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['Month'] = df['Date'].dt.month
df = pd.concat([df,pd.get_dummies(df['Month'],prefix='Month',
                                     dtype=bool)],axis=1)
df['Day'] = df['Date'].dt.month
df = pd.concat([df,pd.get_dummies(df['Day'],prefix='Day',
                                     dtype=bool)],axis=1)
# Train model with Date as features
# Split data to features and label                       
X = df.drop(['Weekly_Sales','Date','Store'], axis=1)
y = df['Weekly_Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1,
	                                                random_state=42)
adaboost = AdaBoostRegressor(random_state=42).fit(X_train, y_train)
adaboost_acc = adaboost.score(X_test, y_test)
adaboost_rmse = rmse(y_test, adaboost.predict(X_test))
print(adaboost_acc)
print(adaboost_rmse)

# Train model without Date as features
# Split data to features and label
X_noDate = df_noDate.drop(['Weekly_Sales','Date','Store'], axis=1)
y_noDate = df_noDate['Weekly_Sales']  
train_test_split_noDate_index =  train_test_split(X_noDate, y_noDate,
	                                              test_size=0.1,
	                                              random_state=42)
X_train_noDate, X_test_noDate, \
y_train_noDate, y_test_noDate = train_test_split_noDate_index

X_noDate = df_noDate.drop(['Weekly_Sales','Date','Store'], axis=1)
y_noDate = df_noDate['Weekly_Sales']
adaboost_noDate = AdaBoostRegressor(random_state=42).fit(X_train_noDate,
	                                                     y_train_noDate)
adaboost_acc_noDate = adaboost_noDate.score(X_test_noDate, y_test_noDate)
adaboost_rmse_noDate = rmse(y_test_noDate,
                            adaboost_noDate.predict(X_test_noDate))
print(adaboost_acc_noDate)
print(adaboost_rmse_noDate)
