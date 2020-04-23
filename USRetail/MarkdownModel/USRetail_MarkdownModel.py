import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.api as sm


# Read Data
data_features = pd.read_csv('../Data/Refined/features_dataset_refined.csv')
data_sales = pd.read_csv('../Data/Original/sales_dataset.csv')
df_sales = data_sales[['Store','Date','Weekly_Sales']] \
                     .groupby(['Store','Date']).sum().reset_index()
# Merge features with weekly sales
df = data_features.merge(df_sales[['Store','Date','Weekly_Sales']] \
	                             .groupby(['Store','Date']).sum() \
	                             .reset_index(),on=['Store','Date'],
	                             how='left')
# Make a list of Markdown columns and fill NA with 0
markdowns = ['MarkDown'+str(num+1) for num in range(5)]
df[markdowns] = df[markdowns].fillna(0)
# Get holiday weekly and non-holidy weekly data only
df_normal = df[~df['IsHoliday']]
df_holiday = df[df['IsHoliday']]


# Define columns for statsmodels
# For holiday weeks
xTempH = df_holiday['Temperature']
xGasH = df_holiday['Fuel_Price']
xMarkDown1H = df_holiday['MarkDown1']
xMarkDown2H = df_holiday['MarkDown2']
xMarkDown3H = df_holiday['MarkDown3']
xMarkDown4H = df_holiday['MarkDown4']
xMarkDown5H = df_holiday['MarkDown5']
xCPIH = df_holiday['CPI']
xUnemploymentH = df_holiday['Unemployment']
yH = df_holiday['Weekly_Sales']

"""
# May not be useful now
# For normal weeks
xTemp = df_normal['Temperature']
xGas = df_normal['Fuel_Price']
xMarkDown1 = df_normal['MarkDown1']
xMarkDown2 = df_normal['MarkDown2']
xMarkDown3 = df_normal['MarkDown3']
xMarkDown4 = df_normal['MarkDown4']
xMarkDown5 = df_normal['MarkDown5']
xCPI = df_normal['CPI']
xUnemployment = df_normal['Unemployment']
y = df_normal['Weekly_Sales']
"""

# Fit the model with holiday data
model_holiday = smf.ols('''yH ~ xTempH + xGasH + xMarkDown1H + xMarkDown2H + 
	                   xMarkDown3H + xMarkDown4H + xMarkDown5H + xCPIH + 
	                   xUnemploymentH''', data=df_holiday).fit()
# Print and save the result
print(model_holiday.summary())
with open('MarkdownModelHolidaySummary.txt','w') as f:
	f.write(model_holiday.summary().as_text())

"""
# Fit the model with weekday data
model_normal = smf.ols('''y ~ xTemp + xGas + xMarkDown1 + xMarkDown2 + 
	                   xMarkDown3 + xMarkDown4 + xMarkDown5 + xCPI + 
	                   xUnemployment''', data=df_normal).fit()
# Print and save the result
print(model_normal.summary())
with open('MarkdownModelNormalWeeksSummary.txt','w') as f:
	f.write(model_normal.summary().as_text())
"""