# Part 2 - US Retail Analytics

## Data
There are 3 data sets. The data sets came from Kaggle.
1. Features
2. Sales
3. Stores

## Goals
1. Predict department-wide sales for each store for the following year.
2. Model the effects of markdowns on holiday weeks.
3. Find insights.

## EDA
Used Tableau to find data insight

## Model Training

### Building the Models based on each Store or each Department in each store
Use R-square to determine the accuracy, linear regression model
<br><br>
* TrainOverall.py has negative R-square
* TrainByStore.py has ~60% R-square
* TrainByDept.py has negative R-square
<br><br>
ModelSelection
* Understand feature effect on weekly sales
* Tried Adaboost and XGboost algos
* Adaboost is better
<br><br>
Exploring Features: Markdown1-5 and Date



