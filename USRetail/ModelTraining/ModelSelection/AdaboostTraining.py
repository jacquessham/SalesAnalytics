import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error as rmse
from sklearn.model_selection import train_test_split


# Read all data and join the data 
data_features = pd.read_csv('../../Data/Refined/features_dataset_refined.csv')
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

# Using default hyperparameter
adaboost = AdaBoostRegressor(random_state=42).fit(X_train, y_train)
adaboost_acc = adaboost.score(X_test, y_test)
adaboost_rmse = rmse(y_test, adaboost.predict(X_test))

# Print result in R-squ
print('The R-square is:', adaboost_acc)
# Print result in RMSE if needed
print('The RMSE is:', adaboost_rmse)

# Save the result in text file
f = open('Results/AdaboostResult.txt','w')
# Write R-square
f.write('Adaptive Boosting Regressor\n')
f.write('The R-square is: ')
f.write(str(round(adaboost_acc,4)))
f.write('\n')
# Write Rmse
f.write('The RMSE is: ')
f.write(str(round(adaboost_rmse,4)))
f.close()
