# Building the Models based on each Store or each Department in each Store
Finding the model accuracy. Use R-square to determine.

## Model based on the Whole Retail Chain (Model 1)
* Sum up the Weekly_sales from all stores based on each week
* Sum up MarkDown 1-5 from all stores based on each week, if none, convert to 0
* Take mean of Temperature and Fuel_price
* Train model with Linear Regression with K-fold
* Shuffle=True in K-fold
* Take all MarkDowns, average temperature and fuel price as features
* Negative R-square

## Model based on each Store (Model 2)
* Only Train Store 1
* Merge features and sales data and filter only the observations in Store 1
* Aggregate all department sales within Store 1 based on each week
* Convert to 0 if MarkDown 1-5 is null
* Train model with Linear Regression with K-fold
* Shuffle=True in K-fold
* Take all MarkDowns, temperature, fuel price, CPI, Unemployment in the city where Store 1 located in, and IsHoliday  as features
* ~60% R-square



## Model based on each Department in each Store (Model 3)
* Only Train Department 1 in Store 1
* Filter feature data to only Store 1
* Merge the filtered data with sales data with only Department 1 in Store 1
* Convert to 0 if MarkDown 1-5 is null
* Train model with Linear Regression with K-fold
* Shuffle=True in K-fold
* Take all MarkDowns, temperature, fuel price, CPI, Unemployment in the city where Store 1 located in, and IsHoliday  as features
* ~60% R-square

## Verdict
Since Model 2 based on each store is ~58% and the other models received negative r-square, choose the Model 2 - model based on each Store.
<br><br>
But how to obtain the department-wide sales for each store for the following year?
<br>
Once we have a model to predict the weekly sales in each store, then we will esimate the sales portion of each department in the store and use the estimated sales portion of each department to predict the weekly sales at the given department in the store.