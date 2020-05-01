# Model Training
The first step to make the prediction model is to find the best algorithm for building the prediction model. 

## Strategy
The first step is to build a prediction model in linear regression as a baseline model to learn more about the prediction model in a statistical perspective first. Then we will compare the model built by 5 algorithms:
<ul>
	<li>Linear Regression</li>
	<li>Decision Tree Regressor</li>
	<li>Random Forest Regressor</li>
	<li>Adaptive Boosting Regressor</li>
	<li>Gradient Boosting Regressor</li>
</ul>
Each model we will obtain the R-square as the metric of accuracy with 5-folds. Whichever model has the highest average accuracy will be chosen for the final prediciton model.

## Files
We have 2 python files and 2 result in text files:
<ol>
	<li>Carsales_lr.py - Use statistic package to train model with linear regression to learn the prediction model in a statistical perspective</li>
	<li>Carsales_modeltraining.py - Use Sklearn to train models with 5-folds and 5 algorithms for comparsion</li>
	<li>lr_summary.txt (In Results folder) - Result for Carsales_lr.py</li>
	<li>ModeltrainingResult.txt (In Results folder) - Result for Carsales_modeltraining.py</li>
</ol>

## Package Used
Note that we have use 42 for random state, in order to eliminate the randomness.

### Carsales_lr.py
<ul>
	<li>Pandas</li>
	<li>Numpy</li>
	<li>Statsmodels</li>
</ul>

### Carsales_modeltraining.py
<ul>
	<li>Pandas</li>
	<li>Numpy</li>
	<li>Sklearn - KFold</li>
	<li>Sklearn - LinearRegression</li>
	<li>Sklearn - DecisionTreeRegressor</li>
	<li>Sklearn - RandomForestRegressor</li>
	<li>Sklearn - AdaBoostRegressor</li>
	<li>Sklearn - GradientBoostingRegressor</li>
</ul>

## Intepretation of Linear Regression
The summary of the linear regression model from the Carsales_lr.py is here:
<br>
<img src="Intepretation_lr.png">
<br><br>
We have chosen 7 features for the model from EDA: Car make, car wheelbase, car width, car length, car resales ratio, car unit price, and car horsepower. Since car make is a categorical feature, such column expands to the number of the columns of car makes in the data set. From those new created columns, we can interpret the coefficient to understand which car make are great sellers in the dealership. For example, the coefficient for Ford is 137.39 that we can expect the dealership sell more Ford than any other car brands. In contrast, we have -14.97 for Jaguar, we expect the dealership sell less Jaguar cars than other brands. The model has a positive coefficient for wheelbase and length, we expect larger cars sell better than smaller cars. Price has a negative coefficient as expected because cheaper cars tend to sell more. Interestingly, we have a negative coefficient on resales value that means popular cars tend to have weaker sales in this dealership.

## Algorithms Comparsion
The file Carsales_modeltraining.py compare accuracy on the model built by 5 algorithms. Before training the model, there are some data engineering work be done first. Since the original data use period for NA data, the program first convert all period to NA data in order to be recognized by Pandas first. Then, the program fills 0 for resales value. It makes sense to have 0 resales value because car models can be potential having no resell market or worth nothing after certain years. Pandas automatically set all columns be string because the numeric features columns contain non-numeric data, ie, period. The next step is to convert the numeric features to numeric types. After that, define a column for resales ratio by calculate the resales value divide by unit price. Lastly, we have decided car makes are important features of car sales, so we have to convert the car make column to be boolean categorical columns.
<br><br>
To prevent the model predict a negative number, we have to take the natural log of the car sales column. Using natural log, it ensures the prediction to be positive and increase the accuracy of all model performance.
<br><br>
Once the data is engineered, we use 5-fold to randomly split training and test data set (Shuffle is set to be True to eliminate the correlation among observations since the data is sort by car makes). For each fold, we train 5 models with 5 algorithms and return the R-square. After 5 times, we take the average of R-squares and obtain the following result:
<ul>
	<li>Linear Regression: 35%</li>
	<li>Decision Tree Regressor: 0%</li>
	<li>Random Forest Regressor: 0%</li>
	<li>Adaptive Boosting Regressor: 30%</li>
	<li>Gradient Boosting Regressor: 32%</li>
</ul>

## Verdict
Since the model built with Linear Regression achieve the highest R-square, we will build the prediction model with linear regression. 

## Next Step
The next step is to build the prototype prediction model. You may find the next phase in the [Prediction Model folder](../PredictionModel)
