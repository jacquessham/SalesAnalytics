import pandas as pd
from abtestingkit import *


supermarket = pd.read_csv('../Burmasupermarket_sales.csv')
abtest_result = abtesting(supermarket,'CustomerType','Cogs',0,'greater than')

f = open('Results/Burmasupermarket_abtesting_member.txt','w')
f.write('-----Result-----\n')
f.write('P-value: ')
f.write(str(round(abtest_result['pval'], 4)))
f.write('\n')
f.write('Power: ')
f.write(str(round(abtest_result['power'], 4)))
if abtest_result['power'] < 0.80:
	f.write('\n')
	f.write('Sample Size needed to achieve 80%: ')
	f.write(str(abtest_result['size_needed'][0]))
	f.write(' ')
	f.write(str(abtest_result['size_needed'][1]))
f.close()