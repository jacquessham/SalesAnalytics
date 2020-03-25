import pandas as pd


def dataEngineering(df):

	# Drop Branch, Tax 5%, GrossMarginPercentage, GrossIncome
	df = df.drop(columns=['Branch','Tax5%','GrossMarginPercentage','GrossIncome'])
	df = df.rename(columns = {'Cogs':'GrandTotal'})

	# Alternative way for labelling
	#labeldict = {}
	# Convert City column to label
	"""
	cityArray, cityLabelArray = pd.factorize(df.City)
	df.City = pd.Categorical(cityArray)
	labeldict['num2City'] = {k:v for k,v in enumerate(cityLabelArray.tolist())}
	"""
	# Convert City to one-hot encoding
	df = pd.concat([df,pd.get_dummies(df['City'],prefix='City',
		                              dtype=bool)], axis=1)
	

	# Convert Customer type to dummy variable, 1=Member, 0=Non-member(Normal)
	df['CustomerType'] = df.CustomerType.eq('Member').mul(1).astype('bool')
	df = df.rename(columns = {'CustomerType':'isMember'})

	# Convert Gender type to dummy variable, 1=Male, 0=Female
	df['Gender'] = df.Gender.eq('Male').mul(1).astype('bool')
	df = df.rename(columns = {'Gender':'isMale'})

	# Convert Product Line to one-hot encoding
	df = pd.concat([df,pd.get_dummies(df['ProductLine'],prefix='ProductLine',
		                              dtype=bool)],axis=1)

	# Convert Payment to one-hot encoding
	df = pd.concat([df,pd.get_dummies(df['Payment'],prefix='Payment',
		                              dtype=bool)],axis=1)

	# Drop the duplicated columns
	df = df.drop(columns=['City','ProductLine','Payment'])


	# Convert Date column to datetime type
	# Create columns for all datetime elements
	
	df['Datetime'] = pd.to_datetime(df['Date']+' '+df['Time'])
	# df['Year'] = df['Datetime'].dt.year
	df['Month'] = df['Datetime'].dt.month
	df = pd.concat([df,pd.get_dummies(df['Month'],prefix='Month',
		                              dtype=bool)],axis=1)
	df['Day'] = df['Datetime'].dt.day
	df = pd.concat([df,pd.get_dummies(df['Day'],prefix='Day',
		                              dtype=bool)],axis=1)
	df['Hour'] = df['Datetime'].dt.hour
	df = pd.concat([df,pd.get_dummies(df['Hour'],prefix='Hour',
		                              dtype=bool)],axis=1)
	# df['Minute'] = df['Datetime'].dt.minute

	df = df.drop(columns=['Month','Day','Hour'])
	df = df.drop(columns=['Date','Time'])

	return df


