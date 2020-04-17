# Sales Analytics of Burma Supermarkets
This is one part of the Sales Analytics Project. The data set is a selective data set on supermarket transactions in 3 different supermarkets in Burma. The goal of this part is to find interesting data insight and make prediction models for this Burma supermarket chain.

## Goal and Strategy
* Goal 1: Find interesting data insight
* Goal 2: Make prediction model to predict future sales 
<br><br>
The first step to explore the data insight first by making a lot of visualization on the exploratory data analysis (EDA) phase. Then, we will discuss some of the interesting finding in the visualization first and raise some question(s) for business purpose. We will answer those question(s) by conducting A/B Testing in order to achieve Goal 1.
<br><br>
The next step is to use existing data set to train prediction model by picking the best features and algorithm in the Model Training phase. Once the feature and algorithm is selected, we will use this result to build the prediction model to predict future sales.

## Data
The data is obtained from <a href="https://www.kaggle.com/aungpyaeap/supermarket-sales">Kaggle</a>. The data is the selective transactions in the given Burma supermarket chain, there are about 1000 transactions. It is a balance data set, meaning the data distribution on all columns are almost the same.
<br>
Please find more detail in the [Data Folder](Data)

## Data Exploration
I used Tableau to visualize some data insight before training prediction models to explore and understand more about the data set itself. Please find the findings and insight in the [EDA folder](EDA). The folder includes the Tableau files that creates the visualization and the images of visualizations.


## A/B Testing
After performed the exploratory data analysis, I am interested about whether the sales of member is higher than the sales of non-member. Please find the findings and result in the [ABtesting folder](ABtesting). The folder includes the findings, result, and codes which run the analysis.


## ModelTraining
Another goal of this part is to make a prediction model. In this [ModelTraining folder](ModelTraining), I will go over how to build the prediction model. This folder includes the codes and result of the model training phase. 


## Prediction Model
This [PredictionModel folder](PredictionModel) consists the code and description of the prediction model on predicting sales. (Coming Soon)


## Thought
We have achieved the goals of this part of the project. We have confirmed that the sales fo members is greater than the sales of non-members and health & beauty sales from male consumers is greater. The marketing department may use these finding to focus the efforts on marking promotion on these area. Also we have built a prediction model to predict future sales if the features data set is available. This is useful for the management of this Burma supermarket chain to make sales and budget planning.
<br><br>
However, we know that the data set is a selective data set from the full data set. In this prediction model, the observation size in the training model is too small that the prediction model that the accuracy of the prediction model may not be trustworthy. The model may be improved if the prediction model is trained with larger training data set or the full data set. Also, the features available in the training set is not informative enough because there are not a lot of unique features to the observation. I suggest the model would be more useful if more KPI associated with each observation is available.

## Next Part
In the next part, we will look at a US Retail Chain that we are also looking at the data insights and making prediction model similar to this part. You may click [here](../USRetail) to find more about next part.
