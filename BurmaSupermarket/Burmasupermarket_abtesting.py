import pandas as pd
from abtestingkit import *


supermarket = pd.read_csv('Burmasupermarket_sales.csv')
abtest_result = abtesting(supermarket,'CustomerType','Cogs',0,'greater than')
print(abtest_result)