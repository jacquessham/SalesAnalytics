import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor as Dtr
from sklearn.ensemble import RandomForestRegressor as Rfr
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

# Declare Kfold object and list to store r-square and rmse for each model
kf = KFold(n_splits=10, shuffle=True, random_state=42)
lr_acc = []
lr_rmse = []
svr_acc = []
svr_rmse = []
dt_acc = []
dt_rmse = []
rf_acc = []
rf_rmse = []

# Train and test the model
for train_index, test_index in kf.split(df):
	X_train, X_test = X.iloc[train_index,:], X.iloc[test_index,:]
	y_train, y_test = y.iloc[train_index], y.iloc[test_index]

	lr = LinearRegression().fit(X_train, y_train)
	lr_acc.append(lr.score(X_test, y_test))
	lr_rmse.append(rmse(y_test, lr.predict(X_test)))
	svr = SVR().fit(X_train, y_train)
	svr_acc.append(svr.score(X_test, y_test))
	svr_rmse.append(rmse(y_test, svr.predict(X_test)))
	dt = Dtr(random_state=42).fit(X_train, y_train)
	dt_acc.append(dt.score(X_test, y_test))
	dt_rmse.append(rmse(y_test, dt.predict(X_test)))
	rf = Rfr(random_state=42).fit(X_train, y_train)
	rf_acc.append(rf.score(X_test, y_test))
	rf_rmse.append(rmse(y_test, rf.predict(X_test)))	

# Print results
print('****************Linear Regression****************')
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
print('*************************************************')


print('***********************SVR***********************')
print('The R-square of each fold:')
for rsqu in svr_acc:
  print(rsqu)
print('The average of the accuracy is', np.mean(svr_acc))
print('-------------------------------------------------')
# Print result in RMSE if needed
print('The RMSE of each fold:')
for acc in svr_rmse:
  print(acc)
print('The average of the accuracy is', np.mean(svr_rmse))
print('*************************************************')

print('************Decision Tree Regressor**************')
print('The R-square of each fold:')
for rsqu in dt_acc:
  print(rsqu)
print('The average of the accuracy is', np.mean(dt_acc))
print('-------------------------------------------------')
# Print result in RMSE if needed
print('The RMSE of each fold:')
for acc in dt_rmse:
  print(acc)
print('The average of the accuracy is', np.mean(dt_rmse))
print('*************************************************')

print('************Random Forest Regressor**************')
print('The R-square of each fold:')
for rsqu in rf_acc:
  print(rsqu)
print('The average of the accuracy is', np.mean(rf_acc))
print('-------------------------------------------------')
# Print result in RMSE if needed
print('The RMSE of each fold:')
for acc in rf_rmse:
  print(acc)
print('The average of the accuracy is', np.mean(rf_rmse))
print('*************************************************')

# Save the result in text file
f = open('Results/AlgoCompareResult.txt','w')

# Linear Regression
f.write('****************Linear Regression****************')
f.write('\n')
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
f.write('\n')
f.write('*************************************************')
f.write('\n\n')
# SVR
f.write('***********************SVR***********************')
f.write('\n')
# Write R-square
f.write('The R-square of each fold:\n')
for fold in range(len(svr_acc)):
    line = str(fold+1)
    line += '. '
    line += str(svr_acc[fold])
    line += '\n'
    f.write(line)
f.write('The average of the accuracy is: ')
f.write(str(round(np.mean(svr_acc),4)))
f.write('\n\n')
# Write Rmse
f.write('The RMSE of each fold:\n')
for fold in range(len(svr_rmse)):
    line = str(fold+1)
    line += '. '
    line += str(svr_rmse[fold])
    line += '\n'
    f.write(line)
f.write('The average of the RMSE is: ')
f.write(str(round(np.mean(svr_rmse))))
f.write('\n')
f.write('*************************************************')
f.write('\n\n')
# Decision Tree Regressor
f.write('************Decision Tree Regressor**************')
f.write('\n')
# Write R-square
f.write('The R-square of each fold:\n')
for fold in range(len(dt_acc)):
    line = str(fold+1)
    line += '. '
    line += str(dt_acc[fold])
    line += '\n'
    f.write(line)
f.write('The average of the accuracy is: ')
f.write(str(round(np.mean(dt_acc),4)))
f.write('\n\n')
# Write Rmse
f.write('The RMSE of each fold:\n')
for fold in range(len(dt_rmse)):
    line = str(fold+1)
    line += '. '
    line += str(dt_rmse[fold])
    line += '\n'
    f.write(line)
f.write('The average of the RMSE is: ')
f.write(str(round(np.mean(dt_rmse))))
f.write('\n')
f.write('*************************************************')
f.write('\n\n')
# Random Forest Regressor
f.write('************Random Forest Regressor**************')
f.write('\n')
# Write R-square
f.write('The R-square of each fold:\n')
for fold in range(len(rf_acc)):
    line = str(fold+1)
    line += '. '
    line += str(rf_acc[fold])
    line += '\n'
    f.write(line)
f.write('The average of the accuracy is: ')
f.write(str(round(np.mean(rf_acc),4)))
f.write('\n\n')
# Write Rmse
f.write('The RMSE of each fold:\n')
for fold in range(len(rf_rmse)):
    line = str(fold+1)
    line += '. '
    line += str(rf_rmse[fold])
    line += '\n'
    f.write(line)
f.write('The average of the RMSE is: ')
f.write(str(round(np.mean(rf_rmse))))
f.write('\n')
f.write('*************************************************')
f.close()
