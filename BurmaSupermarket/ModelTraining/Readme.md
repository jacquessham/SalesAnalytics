# Model Training
This folder consists of codes and result of the model training phase. The goal is to use the existing training data to build a prediction model to predict future sales of the Burma supermarket chain.

## Strategy
The plan is to pick the features and train the model in different algorithms and evaluate each model by accuracy, or R-square. We will pick the best model based on the model achieved the highest R-square. We will partition into 3 cases, where each case has its picks of features. Each case, we will train 4 models using Linear Regression, SVR, Decision Tree Regressor, Random Forest Regressor. 
<br><br>

## Case 1: Base Line Model
We will use the following features:
* City, One-hot-encoding
* ProductionLine, One-hot-encoding
* Month (Obtain from Date), One-hot-encoding
* Day (Obtain from Date), One-hot-encoding
* Hour (Obtain from Hour, One-hot-encoding
* isMember, boolean
* isMale, One-hot-encoding
<br><br>
There are 2 files to train the prediction model for this case:
* ModelTraining.py - Driver program
* DataEngineer.py - Helper program to do data engineer
<br>
First, ModelTraining.py read the data in pandas dataframe and call dataEngineering() from DataEngineer.py to engineer the features to the above requirement. We will pick "GrandTotal" as response variable. Once the features are prepared, ModelTraining.py fits the data using the mentioned algorithms and K-Fold to produce 4 models. Because the data set contains time-series data, K-fold's shuffle is set to be True to eliminate autocorrelation among observations.
<br><br>
The result of this model looks like this:<br>
Linear Regression: Negative R-square<br>
SVR: Negative R-Square<br>
Decision Tree Regressor: Negative R-square<br>
Random Forest Regressor: Negative R-square

## Case 2: Effects on Quantity as Feature
In this case, we will explore the effect on quantity as feature by adding quantity as feature. We will use the following features:
* City, One-hot-encoding
* ProductionLine, One-hot-encoding
* Month (Obtain from Date), One-hot-encoding
* Day (Obtain from Date), One-hot-encoding
* Hour (Obtain from Hour, One-hot-encoding
* isMember, boolean
* isMale, One-hot-encoding
* Quantity, integer
<br>
There are 2 files to train the prediction model for this case:
* ModelTraining2.py - Driver program
* DataEngineer2.py - Helper program to do data engineer
<br><br>
The process of training this model is the same as ModelTraining.py, expect DataEngineer2.py would include "Quantity" as one of the features.
<br><br>
The result of this model looks like this:<br>
Linear Regression: 49%<br>
SVR: Negative R-Square<br>
Decision Tree Regressor: Negative R-square<br>
Random Forest Regressor: 39%
<br><br>
It looks like including quantity as feature is useful on making prediction because the base line models are all receive negative R-square.

## Result
As the result, we find that the model trained with the features used in Case 2 and linear regression achieved the highest R-square. We will use those features and that algorithm to build the final prediction model. You may find that model in the [PredictionModel folder](../PredictionModel)
<br><br>
You may also find the result of accuracy rate of all models trained in this phase in the [Results folder](Results)

## Notes
* The data set is small, there are only 1000 observations
* Use one-hot-encoding to handle labeled data in features
* Quantity is the only non-boolean data
* K-fold set Shuffle=True to eliminate autocorrelation among observation
