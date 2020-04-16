# Building the Models based on each Store or each Department in each Store
In this phase, we will use linear regression model because this is the baseline algorithm. We will use R-square to determine the accuracy. We will choose the perspective whichever perspective has the highest R-square.
<br><br>
Note that it is not useful to use RMSE in this case because the number of Department Perspective and Store Perspective is significantly smaller.

## Perspectives
Store Perspective means building one prediction model by using aggregated weekly sales in all department in the same store. Such perspective predict the future weekly sales of this store. However, it does not directly predict the department weekly sales directly. If we want to predict department weekly sales, we may estimate the sales proportion of the given department in the store first, and use this percentage to mutliple the store weekly sales to obtain. If this perspective is used, we need to aggregate the weekly sales from each store on each week first before training the model. Also, there will be 45 prediction models to make prediction for each store.
<br><br>
Department Perspective means building one prediction model by using weekly sales in each department in the given store. The prediction model directly predict the weekly sales of such department that will achieve the goal right away. If this perspective is used, the number of prediction models to be built will be the number of stores times the number of departments. It means each department of each store has its own prediction model.

## Files
The folder consists 3 files.
<ul>
	<li> TrainOverall.py (Overall Perspective) is the file obtain the model accuracy using one prediciton model in one retail chain</li>
	<li> TrainByStore.py (Store Perspective) is the file obtain the model accuracy by building one prediction model in a given store </li>
	<li> TrainByDept.py (Department Perspective) is the file obtain the model accuracy by buildiing one prediction model in a given department in a given store</li>
</ul>

## Data Used
All models used [refined feature data](../../Data/Refined/features_dataset_refined.csv) and [original sales data](../../Data/Oringinal/features_dataset.csv). You may find the detail in the [Data folder](../../Data)

## Package Used
* Pandas
* Numpy
* Sklearn
** KFold
** LinearRegression

## Hyperparameters used
* Use K=10 for KFold
* Use 42 for random state, in order to eliminate the randomness

## Model based on the Whole Retail Chain (Model 1: Overall Perspective)
* Sum up the Weekly_sales from all stores based on each week
* Sum up MarkDown 1-5 from all stores based on each week
* Take mean of Temperature and Fuel_price
* Train model with Linear Regression with K-fold
* Shuffle=True in K-fold
* Take all MarkDowns, average temperature and fuel price as features
* Negative R-square

## Model based on each Store (Model 2: Store Perspective)
* Only Train Store 1
* Merge features and sales data and filter only the observations in Store 1
* Aggregate all department sales within Store 1 based on each week
* Convert to 0 if MarkDown 1-5 is null
* Train model with Linear Regression with K-fold
* Shuffle=True in K-fold
* Take all MarkDowns, temperature, fuel price, CPI, Unemployment in the city where Store 1 located in, and IsHoliday  as features
* ~60% R-square


## Model based on each Department in each Store (Model 3: Department Perspective)
* Only Train Department 1 in Store 1
* Filter feature data to only Store 1
* Merge the filtered data with sales data with only Department 1 in Store 1
* Convert to 0 if MarkDown 1-5 is null
* Train model with Linear Regression with K-fold
* Shuffle=True in K-fold
* Take all MarkDowns, temperature, fuel price, CPI, Unemployment in the city where Store 1 located in, and IsHoliday  as features
* Negative R-square

## Result
You may find the result written in text file in the [Results folder](Results)
* Model 1 (Overal Perspective) has negative R-square
* Model 2 (Store Perspective) has ~58% R-square
* Model 3 (Department Perspective) has negative R-square

## Verdict
Since Model 2 based on each store is ~60% and the other models received negative r-square, choose the Model 2 - model based on each Store.
<br><br>
Once we have a model to predict the weekly sales in each store, then we will esimate the sales portion of each department in the store and use the estimated sales portion of each department to predict the weekly sales at the given department in the store.

## Next Step
The next step is to find which algorithm to used for the prediction model to achieve better accuracy. You may find more [here](../ModelSelection)