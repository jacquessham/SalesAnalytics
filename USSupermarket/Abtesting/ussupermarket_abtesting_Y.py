import pandas as pd
from abtestingkit import *


# Function to identify whether the customer is low or high level income
def classifyY(y, y_med):
	if y < y_med: return 'High'
	return 'Low'


# Read file for data
customers = pd.read_csv('../Data/Original/Supermarket_CustomerMembers.csv')
# Find the 50 percentile to split customers into low and high income
y_med = customers['AnnualIncome'].median()
customers['IncomeClassifier'] = customers['AnnualIncome'] \
                                         .apply(lambda x: classifyY(x,y_med))

# Get result for Case 1
result1 = abtesting(customers,'IncomeClassifier','SpendingScore',
	                0,'greater than')
savefile(result1, 'case1result.txt')
# Get result for Case 2
result2 = abtesting(customers,'Gender','SpendingScore')
savefile(result2, 'case2result.txt')
