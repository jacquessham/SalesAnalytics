import pandas as pd


def getProb(df, items):
	df_item = df
	# If nothing is select, or no prior
	if items is not None:
		# To filter out transaction without the prior selection
		for item in items:
			df_item = df_item[df_item[item]==1]
	else:
		# To declare a list for items to prevent error in later for loop
		items = []
	df_rows = df_item.shape[0]
	result_items = {}

	# Calculate probabilities for products
	for col in df_item.columns:
		if col != 'Items_Count' and col not in items:
			item_counts = df_item[col].value_counts().to_dict()
			if 1 in item_counts:
				result_items[col] = (item_counts[1]*1.0)/df_rows

	# Calculate probability of no next item
	basket_num = df_item['Items_Count'].tolist()
	if df_rows != 0:
		basket_full = [1 if int(num)==len(items) else 0 for num in basket_num]
		result_items['No Further Item'] = (sum(basket_full)*1.0)/df_rows
	else:
		result_items['No Further Item'] = 1

	# Calculate probability of number of items in basket
	df_basketnum = df_item
	df_basketnum = df_basketnum[df_basketnum['Items_Count']>=len(items)]
	df_basketnum_rows = df_basketnum.shape[0]
	basketnum = df_basketnum['Items_Count'].value_counts().to_dict()
	result_basketnum = {}
	for num in basketnum:
		result_basketnum[num] = (basketnum[num]*1.0)/df_basketnum_rows
	if len(result_basketnum)==0:
		result_basketnum[len(items)] = 1


	return result_items, result_basketnum
