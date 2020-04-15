import pandas as pd


"""
The goal of this file is to fill the na's and extract which weeks are
holiday.
"""
# Read the feature data set
df = pd.read_csv('../Data/Original/features_dataset.csv')

# First - Fill the na's and save to csv file
cols_list = ['Temperature','Fuel_Price','CPI','Unemployment']
markdowns_list = ['MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4',
                  'MarkDown5']
df[cols_list] = df[cols_list].fillna(method='ffill')
df[markdowns_list] = df[markdowns_list].fillna(0)

df.to_csv('../Data/Refined/features_dataset_refined.csv',index=False)

# Find which weeks are holiday, based on store 1 second year data
date = df[df['Store']==1]
date = date[['Date','IsHoliday']]
date['Year'] = pd.to_datetime(date['Date'], format='%d/%m/%Y').dt.year
date = date[date['Year']==date['Year'].min()+1]
rows = date['IsHoliday'].count()
date['Week'] = range(1,rows+1)
date = date.drop(['Date','Year'], axis=1)
date = date[['Week','IsHoliday']]

date.to_csv('../Data/Refined/IsHoliday.csv',index=False)
