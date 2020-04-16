import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error as rmse


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


# Split data to features and label                     
X = df.drop(['Weekly_Sales','Date','Store'], axis=1)
y = df['Weekly_Sales']


kf = KFold(n_splits=10, shuffle=True, random_state=42)
lr_acc = []
lr_rmse =[]

# Train and test the model
for train_index, test_index in kf.split(df):
	X_train, X_test = X.iloc[train_index,:], X.iloc[test_index,:]
	y_train, y_test = y.iloc[train_index], y.iloc[test_index]

	lr = LinearRegression().fit(X_train, y_train)
	lr_acc.append(lr.score(X_test, y_test))
	lr_rmse.append(rmse(y_test, lr.predict(X_test)))


# Print result in R-squ
print('The R-square of each fold:')
for rsqu in lr_acc:
  print(rsqu)
print('The average of the accuracy is', np.mean(lr_acc))
print('-------------------------------------------------')
# Print result in RMSE if needed
print('The RMSE of each fold:')
for acc in lr_rmse:
  print(acc)
print('The average of the accuracy is', np.mean(lr_rmse))

# Save the result in text file
f = open('Results/TrainByStoreResult.txt','w')
# Write R-square
f.write('The R-square of each fold:\n')
for fold in range(len(lr_acc)):
    line = str(fold+1)
    line += '. '
    line += str(lr_acc[fold])
    line += '\n'
    f.write(line)
f.write('The average of the accuracy is: ')
f.write(str(round(np.mean(lr_acc),4)))
f.write('\n\n')
# Write Rmse
f.write('The RMSE of each fold:\n')
for fold in range(len(lr_rmse)):
    line = str(fold+1)
    line += '. '
    line += str(lr_rmse[fold])
    line += '\n'
    f.write(line)
f.write('The average of the RMSE is: ')
f.write(str(round(np.mean(lr_rmse))))
f.close()

