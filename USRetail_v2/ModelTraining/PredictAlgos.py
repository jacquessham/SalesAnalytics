import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor as Dtr
from sklearn.ensemble import RandomForestRegressor as Rfr
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor as Xgboost


# Read all data and join the data 
data_features = pd.read_csv('../../USRetail/Data/Refined/features_dataset_refined.csv')
data_sales = pd.read_csv('../../USRetail/Data/Original/sales_dataset.csv')
data_sales = data_sales[['Store','Dept','Date','Weekly_Sales']] \
                       .groupby(['Store','Date']).sum().reset_index()
df = data_features.merge(data_sales[['Store','Date','Weekly_Sales']] \
	                               .groupby(['Store','Date']).sum() \
	                               .reset_index(),on=['Store','Date'],
	                               how='left').fillna(0)
# Try all stores
stores = df['Store'].unique()

pred_lr = {'Date':[], 'Weekly_Sales':[], 'Weekly_Sales_pred':[], 'Store':[]}
pred_dt = {'Date':[], 'Weekly_Sales':[], 'Weekly_Sales_pred':[], 'Store':[]}
pred_rf = {'Date':[], 'Weekly_Sales':[], 'Weekly_Sales_pred':[], 'Store':[]}
pred_adaboost = {'Date':[], 'Weekly_Sales':[],
                 'Weekly_Sales_pred':[], 'Store':[]}

pred_xgboost = {'Date':[], 'Weekly_Sales':[],
                 'Weekly_Sales_pred':[], 'Store':[]}


for store in stores:
    df_currstore = df[df['Store']==store]
    # Split data to features and label                      
    X = df_currstore.drop(['Weekly_Sales','Date','Store'], axis=1)
    y = df_currstore['Weekly_Sales']

    # Save results from LR model
    lr = LinearRegression().fit(X, y)
    pred_temp = lr.predict(X)
    pred_lr['Date'] = pred_lr['Date'] + df_currstore['Date'].tolist()
    pred_lr['Store'] = pred_lr['Store'] + [store for _ in range(X.shape[0])]
    pred_lr['Weekly_Sales'] = pred_lr['Weekly_Sales'] + y.tolist()
    pred_lr['Weekly_Sales_pred'] = pred_lr['Weekly_Sales_pred'] \
                                   + pred_temp.tolist()

    # Save results from DT model
    dt = Dtr(random_state=42).fit(X, y)
    pred_temp = dt.predict(X)
    pred_dt['Date'] = pred_dt['Date'] + df_currstore['Date'].tolist()
    pred_dt['Store'] = pred_dt['Store'] + [store for _ in range(X.shape[0])]
    pred_dt['Weekly_Sales'] = pred_dt['Weekly_Sales'] + y.tolist()
    pred_dt['Weekly_Sales_pred'] = pred_dt['Weekly_Sales_pred'] \
                                   + pred_temp.tolist()
    # Save results from RF model
    rf = Rfr(random_state=42).fit(X, y)
    pred_temp = rf.predict(X)
    pred_rf['Date'] = pred_rf['Date'] + df_currstore['Date'].tolist()
    pred_rf['Store'] = pred_rf['Store'] + [store for _ in range(X.shape[0])]
    pred_rf['Weekly_Sales'] = pred_rf['Weekly_Sales'] + y.tolist()
    pred_rf['Weekly_Sales_pred'] = pred_rf['Weekly_Sales_pred'] \
                                   + pred_temp.tolist()

    # Save results from adaboost
    adaboost = AdaBoostRegressor(random_state=42).fit(X, y)
    pred_temp = adaboost.predict(X)
    pred_adaboost['Date'] = pred_adaboost['Date'] + df_currstore['Date'].tolist()
    pred_adaboost['Store'] = pred_adaboost['Store'] + [store for _ in range(X.shape[0])]
    pred_adaboost['Weekly_Sales'] = pred_adaboost['Weekly_Sales'] + y.tolist()
    pred_adaboost['Weekly_Sales_pred'] = pred_adaboost['Weekly_Sales_pred'] \
                                   + pred_temp.tolist()

    # Save results from adaboost
    xgboost = Xgboost(random_state=42).fit(X, y)
    pred_temp = xgboost.predict(X)
    pred_xgboost['Date'] = pred_xgboost['Date'] + df_currstore['Date'].tolist()
    pred_xgboost['Store'] = pred_xgboost['Store'] + [store for _ in range(X.shape[0])]
    pred_xgboost['Weekly_Sales'] = pred_xgboost['Weekly_Sales'] + y.tolist()
    pred_xgboost['Weekly_Sales_pred'] = pred_xgboost['Weekly_Sales_pred'] \
                                   + pred_temp.tolist()


df_lr = pd.DataFrame(pred_lr)
df_lr.to_csv('Results/lr_prediction.csv', index=False)

df_dt = pd.DataFrame(pred_dt)
df_dt.to_csv('Results/dt_prediction.csv', index=False)

df_rf = pd.DataFrame(pred_rf)
df_rf.to_csv('Results/rf_prediction.csv', index=False)

df_adaboost = pd.DataFrame(pred_adaboost)
df_adaboost.to_csv('Results/adaboost_prediction.csv', index=False)

df_xgboost = pd.DataFrame(pred_xgboost)
df_xgboost.to_csv('Results/xgboost_prediction.csv', index=False)