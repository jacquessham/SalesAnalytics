# Part 2 - US Retail Analytics
This part we are going to explore the data in a given US Retail chain. It is the second part of the Sales Analytics project.
<br><br>
You may find the result in the [Report folder](Report) related to this project.
<br><br>
To explore the other parts of the Sales Analytics project, please go back to the <a href="https://github.com/jacquessham/SalesAnalytics">front page</a> for other parts.

## Data
There are 3 files in the data set which came from Kaggle. Those files consists the data of the given US Retail chain between 2010 and 2013.
<br><br>
The data may be found in the [Data folder](Data)
<br><br>
The data set consists of the following data:
1. Features - Environment and Features Records of each store on a given date
2. Sales - Sales of a given department in a given store on a given date
3. Stores - Meta data of each store (Size)

## Goals
1. Predict department-wide sales for each store in 2013 and 2014.
2. Model the effects of markdowns on holiday weeks.

## EDA
We have used Tableau to find data insight. The data insight maybe found in the [EDA folder](EDA)

## Goal 1: Predict department-wide sales for each store in 2013 and 2014
Once we have understood the data insight in EDA, the next step is to use the data set to train the prediction model to achieve this goal. In the Model Training phase, we will explore which algorithm and features to be used in the prediction model. Once we have figured out, we will build a prediction according to the Model Training phase and save the result in csv files in the same format of data from Kaggle.
<br><br>
There are 4 phases within the model training phases. Please more information or files in the [Model Training folder](ModelTraining)
<ol>
	<li>Find out the perspective of the model, meaning whether we shall build the model based on each Store or each Department in each store.</li>
	<li>Find out which algorithm to use to build the prediction model.</li>
	<li>Explore which features to include or exclude</li>
	<li>Tune the prediction Model</li>
</ol>
Once we have confirmed which algorithm and features to use for the final prediction model, we can build the prediction model. Because most of the features are time-series data, the prediction model also takes account on obtaining the data of such features. You may find more information about it in the <a href="https://github.com/jacquessham/SalesAnalytics/tree/master/USRetail/PredictionModel">Prediction Model folder</a>

## Goal 2: Model the effects of markdowns on holiday weeks.
Another task is to find the effects of markdowns on holiday weeks. In this step, we are going to filter the data set to holiday data and fit this data set to a linear regression model to interpret the effects of markdown promotions. You may find the findings and comments in the [MarkdownModel folder](MarkdownModel)

## Report
The report folder contains a formal summary of this project, including the steps conducted and the findings. You may learn more about it in the [Report folder](Report).

## Next Part
In the effort to improve the usefulness prediction model, the next part will be focused to refine the prediction model and visualize the prediction on a dashboard for the management. You may find more detail about next part in the [US Retail Analytics Version 2 folder](../USRetail_v2)

