import pandas as pd
import math
from datetime import datetime
from dateutil.relativedelta import relativedelta
from fbprophet import Prophet


# Use Facebook Prophet to make prediction
def predict(df, future_ds):
	m = Prophet()
	columns_name = df.columns
	df.columns = ['ds','y']
	m.fit(df)
	prediction = m.predict(future_ds)
	prediction = prediction[['ds','yhat']]
	prediction.columns = columns_name

	return prediction

# Call predict() to Make prediction on multiple columns
def predictColumns(df, columns, target_year, df_holiday):
	last_day = df['Date'].max()
	future_weeks = math.ceil(((datetime(target_year+1,1,1) - last_day).days)/7)
	future_ds = pd.DataFrame({'ds': [relativedelta(weeks=num)+last_day 
		                             for num in range(1,future_weeks)]})
	# If not using copy() will reference the same object
	prediction = future_ds.copy()
	prediction.columns = ['Date']
	for col in columns:
		df_temp = df[['Date',col]]
		prediction_col = predict(df_temp, future_ds)
		prediction = prediction.merge(prediction_col, on=['Date'], how='inner')

	# Converting Date to the week number of the year
	prediction['Year'] = prediction.Date.dt.year
	years = prediction['Year'].tolist()
	prediction['Year_1day'] = [datetime(x,1,1) for x in years]
	prediction['Week'] = (prediction['Date']-prediction['Year_1day']).dt.days/7
	prediction['Week'] = prediction['Week'].apply(lambda x: math.ceil(x))

	# Left join the prediction df with df_holiday to find which weeks are holiday
	prediction = prediction.merge(df_holiday, on='Week', how='left')

	# Drop the datetime columns, except Date
	prediction = prediction.drop(['Year','Year_1day','Week'], axis=1)

	return prediction
