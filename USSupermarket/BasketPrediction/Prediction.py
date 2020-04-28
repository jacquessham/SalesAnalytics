import pandas as pd


def getProb(df, item1, products_num):
	df_item1 = df[df[item1]==1]
	item1_counts = df_item1.shape[0]
	result = {}
	for col in df_item1.columns:
		if col != 'Items_Count' and col != item1:
			item_counts = df_item1[col].value_counts().to_dict()
			if 1 in item_counts:
				result[col] = (item_counts[1]*1.0)/item1_counts
	return result

div_vis = None
