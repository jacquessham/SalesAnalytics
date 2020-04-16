# Model Selection
The goal of this phase is to the find which prediction model built by different algorithm has the highest accuracy. Each model we will obtain the R-square as the metrics of accuracy. Whichever model has the highest accuracy will be chosen for the final prediction model.

## Files
We have the following files:
<ul>
	<li>FeaturesExplain.py - Intepret the features used in the Linear Regression model</li>
	<li>AlgoCompare.py - Train models with SVR, decision tree regressor, and random forest regressor along with K-Fold and return R-square of each model</li>
	<li>AdaboostTraining.py - Train model with adaptive boosting regressor without K-Fold and return the R-square of this model</li>
	<li>XgboostTraining.py - Train model with Gradient Boosting Regressor without K-Fold and return the R-square of this model</li>
</ul>

## Package Used
* Pandas
* Numpy
* Sklearn
** KFold
** train_test_split
** LinearRegression
** SVR
** DecisionTreeRegressor
** RandomForestRegressor
** AdaBoostRegressor
** GradientBoostingRegressor

## Hyperparameters used
* Use K=10 for KFold
* Use 42 for random state, in order to eliminate the randomness

## Understand how the Features Affect on Weekly Sales in Linear Regression
The file [FeaturesExplain.py](/FeaturesExplain.py) generates the intepretation of the features used in the linear regression model.
<br><br>
Intepret the features. Coming Soon.

## Algorithms Comparsion
The file [AlgoCompare.py](/AlgoCompare.py) compare accuracy on Linear Regression, SVR, Decision Tree Regressor, and Random Forest Regressor models. R-square will be used for evaluation.
<br><br>
* Linear Regression: 58%
* SVR: Negative R-square
* Decision Tree Regressor: 92%
* Random Forest Regressor: 91%

## Adaptive Boosting Regressor and Gradient Boosting Regressor
The files [AdaboostTraining.py](/AdaboostTraining.py) and [XgboostTraining.py](/XgboostTraining.py) compare accuracy on Adaptive Boosting Regressor, and Gradient Boosting Regressor.
<br><br>
* Adaboost: 83%
* XGboost: 86%

## Verdict
Since the model built with decision tree regressor achieve the highest R-square, 92%, we will train the final model with decision tree regressor. You may find the next phase [here](../ExploringFeatures)