import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression as Lr
from sklearn.tree import DecisionTreeRegressor as Dtr
from sklearn.ensemble import RandomForestRegressor as Rfr
from sklearn.ensemble import AdaBoostRegressor as Adaboost
from sklearn.ensemble import GradientBoostingRegressor as Xgboost


# Read file
carsales = pd.read_csv('../Data/Car_sales.csv')

# Data Engineering
# Turn all period to NA
carsales = carsales.replace('.',np.nan)
# Take natural log of sales_k
carsales['Sales_k'] = np.log(carsales['Sales_k'].tolist())
# Fill NA to 0 for Resale value
carsales['Resale_value_4yrs'] = carsales['Resale_value_4yrs'].fillna(0)
carsales = carsales.dropna()
# Turn the columns to float type
col_num = ['Sales_k','Resale_value_4yrs','Price','EngineSize','Horsepower',
           'Wheelbase','Width','Length','CurbWeight','FuelCapacity',
           'FuelEfficiency']
carsales[col_num] = carsales[col_num].apply(pd.to_numeric)
# Define Resales Ratio
carsales['ResalesRatio'] = carsales['Resale_value_4yrs']/carsales['Price']
# Turn Manufacturer to categorial variables
carsales = pd.concat([carsales,pd.get_dummies(carsales['Manufacturer'],
	                  prefix='Manufacturer',dtype=bool)], axis=1)

# Select features and response variable for models
makes = ['Manufacturer_'+make for make in carsales['Manufacturer'].unique()] 
features = ['Wheelbase', 'Width', 'Length', 'ResalesRatio',
            'Price', 'Horsepower']
features = features + makes            
X = carsales[features]
y = carsales['Sales_k']

# Define Kfold and results dictionary to store result
kf = KFold(n_splits=5, shuffle=True, random_state=42)
results = {'lr':[], 'dt':[], 'rf':[], 'adaboost':[], 'xgboost':[]}

# Train and test the model
for train_index, test_index in kf.split(carsales):
	X_train, X_test = X.iloc[train_index,:], X.iloc[test_index,:]
	y_train, y_test = y.iloc[train_index], y.iloc[test_index]

	lr = Lr().fit(X_train, y_train)
	lr_score = lr.score(X_test, y_test)
	results['lr'].append(lr_score)

	dt = Dtr().fit(X_train, y_train)
	dt_score = dt.score(X_test, y_test)
	results['dt'].append(dt_score)

	rf = Rfr().fit(X_train, y_train)
	rf_score = dt.score(X_test, y_test)
	results['rf'].append(rf_score)

	adaboost = Adaboost().fit(X_train, y_train)
	adaboost_score = adaboost.score(X_test, y_test)
	results['adaboost'].append(adaboost_score)

	xgboost = Xgboost().fit(X_train, y_train)
	xgboost_score = xgboost.score(X_test, y_test)
	results['xgboost'].append(xgboost_score)

f = open('Results/ModeltrainingResult.txt','w')
# Linear Regression
f.write('****************Linear Regression****************')
f.write('\n')
# Write R-square
f.write('The average of the accuracy is: ')
f.write(str(round(np.mean(results['lr']),4)))
f.write('\n')
f.write('*************************************************')
f.write('\n\n')

# Decision Tree Regressor
f.write('************Decision Tree Regressor**************')
f.write('\n')
# Write R-square
f.write('The the accuracy is: ')
f.write(str(round(np.mean(results['dt']),4)))
f.write('\n')
f.write('*************************************************')
f.write('\n\n')

# Random Forest Regressor
f.write('************Random Forest Regressor**************')
f.write('\n')
# Write R-square
f.write('The the accuracy is: ')
f.write(str(round(np.mean(results['rf']),4)))
f.write('\n')
f.write('*************************************************')
f.write('\n\n')

# Adaboost Regressor
f.write('*********Adaptive Boosting Regressor*************')
f.write('\n')
# Write R-square
f.write('The the accuracy is: ')
f.write(str(round(np.mean(results['adaboost']),4)))
f.write('\n')
f.write('*************************************************')
f.write('\n\n')

# Xgboost Regressor
f.write('*********Gradient Boosting Regressor*************')
f.write('\n')
# Write R-square
f.write('The the accuracy is: ')
f.write(str(round(np.mean(results['xgboost']),4)))
f.write('\n')
f.write('*************************************************')

f.close()