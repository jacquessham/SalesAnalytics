# Part 2 - US Retail Analytics
This part we are going to explore the data in a given US Retail chain. It is the second part of the Sales Analytics project.
<br><br>
You may find the [result here (Coming soon)](/) or the [Medium post (Coming soon)](/) related this project.
<br><br>
To explore the other parts of the Sales Analytics project, please go back to the [front page](..) for other parts.

## Data
There are 3 files in the data set which came from Kaggle. Those files consists the data of the given US Retail chain between 2010 and 2013.
<br><br>
The data may be found [here](Data)
<br><br>
The data set consists of the following data:
1. Features - Environment and Features Records of each store on a given date
2. Sales - Sales of a given department in a given store on a given date
3. Stores - Meta data of each store (Size)

## Goals
1. Predict department-wide sales for each store in 2013 and 2014.
2. Model the effects of markdowns on holiday weeks.
3. Find insights.

## EDA
Used Tableau to find data insight. The data insight maybe found [here](EDA)

## Goal 1: Predict department-wide sales for each store in 2013 and 2014
Once we have understood the data insight in EDA, the next step is to use the data set to train the prediction model to achieve this goal. In the Model Training phase, we will explore which algorithm and features to be used in the prediction model. Once we have figured out, we will build a prediction according to the Model Training phase and save the result in csv files in the same format of data from Kaggle.
<br><br>
There are 4 phases within the model training phases. Please more information or files [here](ModelTraining)
1. Find out the perspective of the model, meaning whether we shall build the model based on each Store or each Department in each store. 
2. Find out which algorithm to use to build the prediction model.
3. Explore which features to include or exclude
4. Tune the prediction Model
<br><br>
Once we have confirmed which algorithm and features to use for the final prediction model, the final product to make sales prediction of this retail chain [here](PredictionModel)
<br><br>
Because most of the features are time-series data, the prediction model also takes account of obtaining such features. You may find more information about it in the [folder](PredictionModel)

## Goal 2: Model the effects of markdowns on holiday weeks.
Coming Soon

## Report
Coming Soon