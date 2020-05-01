import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.api as sm


# Read file
carsales = pd.read_csv('../Data/Car_sales.csv')

# Data Engineering
# Turn all period to NA
carsales = carsales.replace('.',np.nan)
# Fill NA to 0 for Resale value
carsales['Resale_value_4yrs'] = carsales['Resale_value_4yrs'].fillna(0)
col_str = ['Manufacturer','Model','VehicleType','LatestLaunch']
col_num = ['Sales_k','Resale_value_4yrs','Price','EngineSize','Horsepower',
           'Wheelbase','Width','Length','CurbWeight','FuelCapacity',
           'FuelEfficiency']
# Turn the columns to float type
carsales[col_num] = carsales[col_num].apply(pd.to_numeric)
# Define Resales Ratio
carsales['ResalesRatio'] = carsales['Resale_value_4yrs']/carsales['Price']

# Assign features for lr model
xMake = carsales['Manufacturer']
xWheelbase = carsales['Wheelbase']
xWidth = carsales['Width']
xLength = carsales['Length']
xResales = carsales['ResalesRatio']
xPrice = carsales['Price']
xHp = carsales['Horsepower']
y = carsales['Sales_k']

# Fit linear regression model
lr_model = smf.ols(''' y ~ xMake + xWheelbase + xWidth + xLength + xResales
						    + xPrice + xHp''', data=carsales).fit()
# Save result
with open('Results/lr_summary.txt','w') as f:
	f.write(lr_model.summary().as_text())

