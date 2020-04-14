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
df_noMarkdown = df.drop(['MarkDown1','MarkDown2','MarkDown3',
	                                'MarkDown4','MarkDown5'],axis=1)

# Train model with markdowns as features
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

# Train model without markdowns as features
# Split data to features and label
X_noMarkdown = df_noMarkdown.drop(['Weekly_Sales','Date','Store'], axis=1)
y_noMarkdown = df_noMarkdown['Weekly_Sales']  
train_test_split_noMarkdown_index =  train_test_split(X_noMarkdown, y_noMarkdown,
	                                              test_size=0.1,
	                                              random_state=42)
X_train_noMarkdown, X_test_noMarkdown, \
y_train_noMarkdown, y_test_noMarkdown = train_test_split_noMarkdown_index

X_noMarkdown = df_noMarkdown.drop(['Weekly_Sales','Date','Store'], axis=1)
y_noMarkdown = df_noMarkdown['Weekly_Sales']
adaboost_noMarkdown = AdaBoostRegressor(random_state=42).fit(X_train_noMarkdown,
	                                                     y_train_noMarkdown)
adaboost_acc_noMarkdown = adaboost_noMarkdown.score(X_test_noMarkdown,
	                                                y_test_noMarkdown)
adaboost_rmse_noMarkdown = rmse(y_test_noMarkdown,
                            adaboost_noMarkdown.predict(X_test_noMarkdown))
print(adaboost_acc_noMarkdown)
print(adaboost_rmse_noMarkdown)
