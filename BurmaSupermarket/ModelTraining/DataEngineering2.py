import pandas as pd

def dataEngineering(df):
	# Drop Branch, Tax 5%, GrossMarginPercentage, GrossIncome
	df = df.drop(columns=['Branch','Tax5%','GrossMarginPercentage','GrossIncome'])
	df = df.rename(columns = {'Cogs':'GrandTotal'})

	df['Datetime'] = pd.to_datetime(df['Date']+' '+df['Time'])
	df['Month'] = df['Datetime'].dt.month
	df = pd.concat([df,pd.get_dummies(df['Month'],prefix='Month',
		                              dtype=bool)],axis=1)
	df['Day'] = df['Datetime'].dt.day
	df = pd.concat([df,pd.get_dummies(df['Day'],prefix='Day',
		                              dtype=bool)],axis=1)
	df['Hour'] = df['Datetime'].dt.hour
	df = pd.concat([df,pd.get_dummies(df['Hour'],prefix='Hour',
		                              dtype=bool)],axis=1)

	# Convert Customer type to dummy variable, 1=Member, 0=Non-member(Normal)
	df['CustomerType'] = df.CustomerType.eq('Member').mul(1).astype('bool')
	df = df.rename(columns = {'CustomerType':'isMember'})

	# Convert Gender type to dummy variable, 1=Male, 0=Female
	df['Gender'] = df.Gender.eq('Male').mul(1).astype('bool')
	df = df.rename(columns = {'Gender':'isMale'})

	df = df[['City','ProductLine','Month','Day','Hour',
	         'Quantity','isMember','isMale','GrandTotal']] \
	       .groupby(['City','ProductLine','Month','Day','Hour']).sum() \
	       .reset_index()

	# Convert City to one-hot encoding
	df = pd.concat([df,pd.get_dummies(df['City'],prefix='City',
		                              dtype=bool)], axis=1)


	# Convert Product Line to one-hot encoding
	df = pd.concat([df,pd.get_dummies(df['ProductLine'],prefix='ProductLine',
		                              dtype=bool)],axis=1)

	df = df.drop(columns=['City','ProductLine'])

	return df
