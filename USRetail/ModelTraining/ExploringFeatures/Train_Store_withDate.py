import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor as Dtr
from sklearn.metrics import mean_squared_error as rmse
from sklearn.model_selection import train_test_split


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
dt = Dtr(random_state=42).fit(X_train, y_train)
dt_acc = dt.score(X_test, y_test)
dt_rmse = rmse(y_test, dt.predict(X_test))
print(dt_acc)
print(dt_rmse)

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
dt_noDate = Dtr(random_state=42).fit(X_train_noDate,y_train_noDate)
dt_acc_noDate = dt_noDate.score(X_test_noDate, y_test_noDate)
dt_rmse_noDate = rmse(y_test_noDate,dt_noDate.predict(X_test_noDate))
print(dt_acc_noDate)
print(dt_rmse_noDate)
