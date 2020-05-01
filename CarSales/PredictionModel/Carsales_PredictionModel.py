import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression as Lr


# Function to assign make for prediction feature
def assign_make(row):
	make_col = 'Manufacturer_'+row['Manufacturer']
	row[make_col] = 1
	return row


# Read file
carsales = pd.read_csv('../Data/Car_sales.csv')
# Obtain the feature for cars model for prediction
carsales_pred_raw = pd.read_csv('../Data/Car_sales_pred.csv')
carsales_pred = carsales_pred_raw

# Data Engineering
# Turn all period to NA
carsales = carsales.replace('.',np.nan)
carsales_pred = carsales_pred.replace('.',np.nan)
# Fill NA to 0 for Resale value
carsales['Resale_value_4yrs'] = carsales['Resale_value_4yrs'].fillna(0)
carsales_pred['Resale_value_4yrs'] = carsales_pred['Resale_value_4yrs'] \
                                                  .fillna(0)
# Take natural log of sales_k
carsales['Sales_k'] = np.log(carsales['Sales_k'].tolist())
# Drop the NA observation in training data set
carsales = carsales.dropna()
# Turn the columns to float type
col_num = ['Sales_k','Resale_value_4yrs','Price','EngineSize','Horsepower',
           'Wheelbase','Width','Length','CurbWeight','FuelCapacity',
           'FuelEfficiency']
carsales[col_num] = carsales[col_num].apply(pd.to_numeric)
# Define Resales Ratio
carsales['ResalesRatio'] = carsales['Resale_value_4yrs']/carsales['Price']
carsales_pred['ResalesRatio'] = carsales_pred['Resale_value_4yrs'] \
                                /carsales_pred['Price']
# Turn Manufacturer to categorial variables
# For training data set
carsales = pd.concat([carsales,pd.get_dummies(carsales['Manufacturer'],
	                  prefix='Manufacturer',dtype=bool)], axis=1)
makes = ['Manufacturer_'+make for make in carsales['Manufacturer'].unique()] 
# For prediction features
carsales_pred = pd.concat([carsales_pred,pd \
	                       .get_dummies(carsales_pred['Manufacturer'],
	                       prefix='Manufacturer',dtype=bool)], axis=1)
# Pandas apply and fillna(0) does not work, so go with this route
for col in makes:
	if col not in carsales_pred.columns:
		carsales_pred[col] = False

# Select features and response variable for models
features = ['Wheelbase', 'Width', 'Length', 'ResalesRatio',
            'Price', 'Horsepower']
features = features + makes            
X = carsales[features]
y = carsales['Sales_k']
lr = Lr().fit(X, y)

# To predict
X_pred = carsales_pred[features]
# Take e of the result to take out the log scale
y_pred = np.exp(lr.predict(X_pred))
carsales_pred_raw['Sales_k'] = y_pred
# Save result with the original data frame
carsales_pred_raw.to_csv('Result/Carsales_pred.csv', index=False)
