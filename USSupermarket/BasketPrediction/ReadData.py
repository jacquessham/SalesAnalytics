import pandas as pd
import numpy as np


def readfiles(filepath):
	# Read files
	f = open(filepath,'r')
	rawtext = f.read().split('\n')

	# Split each line by comma
	transactions_str = [] # Store items in string per basket
	# To split items by comma for each basket
	for transaction in rawtext:
		transactions_str.append(transaction.split(','))

	# Assign each item to column number and convert transaction to column number
	transactions_num = [] # Store items in number per basket
	pointer = 0 # For assign item number
	product2num = {} # Dict to convert items from string to number
	num2product = {} # Dict to convert items from number to string

	# Convert each basket from string to number labels
	for tran in transactions_str:
		temp_list = []
		for item in tran:
			if item not in product2num:
				product2num[item] = pointer
				num2product[pointer] = item
				pointer += 1
			temp_list.append(product2num[item])
		transactions_num.append(temp_list)

	products_num = len(product2num) # Obtain the length of items list
	transaction_tabluar = [] # For convert to categorical columns
	transaction_len = [] # For obtain the number of items per basket

	# To convert items to categorical columns and number of items per basket
	for tran in transactions_num:
		temp_list = [1 if curr in tran else 0 for curr in range(products_num)]
		transaction_tabluar.append(temp_list)
		transaction_len.append(len(tran))
	cols = [num2product[curr] for curr in range(products_num)]

	transaction_tabluar = pd.DataFrame(np.array(transaction_tabluar), columns=cols)
	transaction_tabluar['Items_Count'] = transaction_len

	return {'transaction_tabluar': transaction_tabluar,
	        'cols': cols,
	        'product2num': product2num, 'num2product': num2product,
	        'products_num': products_num}



