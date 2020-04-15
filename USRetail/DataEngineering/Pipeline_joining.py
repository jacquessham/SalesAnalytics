import pandas as pd


data_features = pd.read_csv('../Data/Original/features_dataset.csv')
data_sales = pd.read_csv('../Data/Original/sales_dataset.csv')
data_stores = pd.read_csv('../Data/Original/stores_dataset.csv')

data_combined = data_sales.merge(data_features.drop('IsHoliday', axis=1),
                                 on=['Store','Date'], how='left')
data_combined = data_combined.merge(data_stores, on='Store', how='left')
data_combined = data_combined.drop('Type', axis=1)
data_combined.to_csv('../Data/Engineered/sales_combined.csv', index=False)
