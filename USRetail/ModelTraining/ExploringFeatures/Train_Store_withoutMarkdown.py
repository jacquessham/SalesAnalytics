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
df_noMarkdown = df.drop(['MarkDown1','MarkDown2','MarkDown3',
	                                'MarkDown4','MarkDown5'],axis=1)

# Train model with markdowns as features
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
dt_noMarkdown = Dtr(random_state=42).fit(X_train_noMarkdown,
	                                                     y_train_noMarkdown)
dt_acc_noMarkdown = dt_noMarkdown.score(X_test_noMarkdown,
	                                                y_test_noMarkdown)
dt_rmse_noMarkdown = rmse(y_test_noMarkdown,
                            dt_noMarkdown.predict(X_test_noMarkdown))
print(dt_acc_noMarkdown)
print(dt_rmse_noMarkdown)
