# Part 5 - US Car Dealership Analytics
In this part, we are going to explore the data given from a US car dealership and make prediction on car sales. This is the fourth part of the Sales Analytics project.

## Data
There are 2 files in this part of the project. The original data set originated from <a href="https://www.kaggle.com/hsinha53/car-sales">Kaggle</a> contains the lifetime sales of each car model available in the dealership. The other data set is the car model which is not available in the dealership for sales prediction in the same format with the original data. You may find more detail in the [Data folder](Data).
<br><br>
The data set available in this part:
* Car_sales.csv - The original data
* Car_sales_pred.csv - The prediction feature data, data of car models features for car sales prediction

## Goal
1. Build a dashboard for management to explore the relationship between car sales and car features of cars available in the dealership
2. Build a prediction model to predict car sales for new car models

## EDA
We have use Plotly to build visualization to explore the data insight and embedded in Dash in a markdown format. The data insight may be found in the [EDA folder](EDA)

## Dashboard
We have built a dashboard for management to look at the relationship between car sales and car features of car models available in the car dealership with Dash. You may find more detail and the dashboard screenshot in the [Dashboard folder](Dashboard)

## Prediction Model
There is 2 phases for making a prediction model: Modeling Training and Making Prototype Prediction Model. In the modeling training phase, we are going to find out the best algorithm for the prediction model. Once we have figured out and built the prototype prediction model, we will obtain 2 car models not available in the data set to make prediction. You may find the Model Training phase in the [Model Training folder](ModelTraining), or find the prototype predition model in the [Prediction Model folder](PredictionModel).

## Conclusion
We have successfully built a dashboard for car sales analysis and a prediction model to predict lifetime car sales of new car models. However, there are some concerns for the prediction model. First, the accuracy of the prediction model is not high. In the model training phase, the model achieves only about 35% R-square. The low accuracy rate may be contributed by the small data set because the original data set only has about 150 observations. Secondly, the observations are lifetime sales instead of monthly or annual sales. This prediction model may be useful to make decision to sell new car models, but not daily operations of the car dealership. Lastly, the training data set only consists gas only car, so the prediction may not be useful for make sales prediction on other types of cars. 