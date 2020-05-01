# Prediction Model
The goal of this phase is to build a prediction model to predict the lifetime car sales of the car models not available in the car dealership.

## Strategy
In the previous phases, we have decided the features and algorithm to build the prototype prediction model. Therefore, we will use the selected features and build the prediction model with linear regression. Once we have trained the prediction model with original data set, we will make a prediction on new car models.

## Files and Data Used
There are 1 python file and 1 result in text file:
<ul>
	<li>Carsales_PredicitonModel.py - Program to make prediction</li>
	<li>Carsales_pred.csv - Result in csv format</li>
</ul>
<br><br>
The program uses 2 data set:
<ul>
	<li>Car_sales.csv - Original data set to train prediction model</li>
	<li>Car_sales_pred.csv - Prediction Feature data, the data set contains the car model featuers of car models not available in the original data set to make prediction</li>
</ul>

## Package Needed
This is the list of packages needed in this application:
<ol>
	<li>Pandas</li>
	<li>Numpy</li>
	<li>Sklearn - Linear Regression</li>
</ol>


## Carsales_PredicitonModel.py
Similar to the model training phase, there are some data engineering work be done first after we have read the original data set. Since the original data use period for NA data, the program first convert all period to NA data in order to be recognized by Pandas first. Then, the program fills 0 for resales value. It makes sense to have 0 resales value because car models can be potential having no resell market or worth nothing after certain years. Pandas automatically set all columns be string because the numeric features columns contain non-numeric data, ie, period. The next step is to convert the numeric features to numeric types. After that, define a column for resales ratio by calculate the resales value divide by unit price. Lastly, we have decided car makes are important features of car sales, so we have to convert the car make column to be boolean categorical columns.
<br><br>
After the prediction feature data is read, the same engineering work is done to ensure the data frame shape be identical to the training data set.
<br><br>
The model is trained with linear regression, the following features are selected:
<ul>
	<li>Wheelbase</li>
	<li>Width</li>
	<li>Length</li>
	<li>Resales Ratio</li>
	<li>Price</li>
	<li>Horsepower</li>
	<li>Car makes</li>
</ul>
<br>
Sales_k is selected for the response variable. In order to prevent negative predictions be produced, we need to take natural log in Sales_K first. Once a prediction is produced, the program takes exponential to return to unscaled number.

## Result
In the prediction feature data set, we have features of BMW Z4 and Toyota Prius. The model predicts the lifetime car sales of these models be:
<ul>
	<li>BMW Z4: 3,467 units</li>
	<li>Toyota Prius: 28.24 units</li>
</ul>
Note that, if we did not take a natural log of Sales_k in the training data set, the prediction of BMW Z4 is a negative number which does not make sense. Therefore, the result shows that it is necessary to take natural log for Sales_k in order for the model produces positive number prediction.

## Next Step
This is the last step of this part of the project. You may find the conclusion in the <a href="https://github.com/jacquessham/SalesAnalytics/tree/master/CarSales">front page</a>.
