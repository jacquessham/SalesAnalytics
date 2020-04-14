import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error as rmse
from sklearn.model_selection import train_test_split


# Read all data and join the data 
data_features = pd.read_csv('../../Data/Original/features_dataset.csv')
data_features = data_features.drop(['MarkDown1','MarkDown2','MarkDown3',
	                                'MarkDown4','MarkDown5'],axis=1)
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
X = df.drop(['Weekly_Sales','Date','Store'], axis=1)
y = df['Weekly_Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1,
	                                                random_state=42)

# Declare dict to store results
# Key:(max_depth, n_estimators), val: (R-square, rmse)
results = {}

# Train default hyperparameter first
# Key is (3,50) according to sklearn doc
adr = AdaBoostRegressor(random_state=42).fit(X_train, y_train)
adr_acc = adr.score(X_test, y_test)
adr_rmse = rmse(y_test, adr.predict(X_test))
results[(3,50)] = (adr_acc, adr_rmse)

# Set up the grid
max_depth_list = [num for num in range(3,11)] 
max_depth_list += [num for num in range(15,51,5)]
n_estimators_list = [num for num in range(10,151,10)]


# Grid search 
for depth in max_depth_list:
	for estimator in n_estimators_list:
		dt = DecisionTreeRegressor(max_depth=depth,random_state=42)
		adr = AdaBoostRegressor(base_estimator=dt, n_estimators=estimator,
			                    random_state=42).fit(X_train, y_train)
		adr_acc = adr.score(X_test, y_test)
		adr_rmse = rmse(y_test, adr.predict(X_test))
		results[(depth,estimator)] = (adr_acc, adr_rmse)

# Write the result in a text file
f = open('TuningResult.csv','w')
f.write('DT_max_depth,Adr_n_estimator,R-square,RMSE\n')

for pairs in results:
	k1, k2 = pairs
	rsqu, rmse = results[pairs]
	line = ''
	line += str(k1)
	line += ','
	line += str(k2)
	line += ','
	line += str(round(rsqu,4))
	line += ','
	line += str(round(rmse))
	line += '\n'
	f.write(line)

f.close()

