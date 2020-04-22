import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm


stores = pd.read_csv('../Data/50_SupermarketBranches.csv')
xAd = stores['AdvertisementSpend']
xProm = stores['PromotionSpend']
xState = stores['State']
y = stores['Profit']

model = smf.ols('y ~ xAd + xProm + xState', data=stores).fit()
sm.stats.anova_lm(model, type=2)

with open('summary.txt','w') as f:
	f.write(model.summary().as_text())
