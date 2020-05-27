# Model Training
Similar to the Model Training phase in Part 2, we will explore which algorithm to be used in the prediction model with different standards to prevent high bias of the prediction model. In this phase, we are also going to build a dashboard to visualizate the prediction made from the models trained with the selected algorithms.

## Goal
Our goal is to build a sales predictive model to replace the prediction model in Part 2. The predictive model should be able to capture trend and seasonality patterns, and be useful for forecasting future sales.

## Packages Used
The packages used in the files in this folder:
<ul>
	<li>pandas</li>
	<li>numpy</li>
	<li>sklearn</li>
	<li>Plotly</li>
	<li>Dash</li>
</ul>

## New Strategy
The strategy of model training in Part 2, we evaluated the models by comparing the accuracy of each model. Similarily, we are going to evaluate the models with the same metrics but we are going to take extra steps in this phase. We are going to train the models with the following algorithms:
<ul>
	<li>Linear Regression</li>
	<li>SVR</li>
	<li>Decision Tree Regressor</li>
	<li>Random Forest Regressor</li>
	<li>Adaptive Boosting</li>
	<li>Gradient Boosting</li>
</ul>
<br>
Here is the extra step we are going to do in this phase.

### Conduct 10-Fold in every Store
In the model training phase in Part 2, we have only trained models with Store 1 data set. However, we have found out the model fits in one store may not perform well in other stores. Therefore, we are going to conduct 10-fold with data set in each store and take an average of R-square across all stores. We will evaluate the models by the accuracy of the average R-square of all stores instead of the average R-square of 1 store.

### Take Visualization as one of the Evaluation
In the model training phase in Part 2, we did not visualize the prediction in that phase and resulted that we did not realize the overfitted model was failed to capture trend and seasonality pattern. Therefore, we will visualize the prediction from each model to observe whether the trend and seasonality patterns are captured this time. We will build a dashboard to visualize the prediction with training data in line chart. 

## Files
There are 5 Python files in this folder:
<ul>
	<li>AlgoCompare.py</li>
	<li>AdaboostTraining.py</li>
	<li>XgboostTraining.py</li>
	<li>PredictAlgos.py</li>
	<li>Dashboard_modelsPred.py</li>
</ul>
<br>
and a folder of <i>Results</i> of prediction saved in csv files and images from the dashboard.

### AlgoCompare.py
This program takes the training data from [Part 2 Data folder](../../USRetail/Data), conduct 10-fold with each store sales by training predictive model with linear regression, SVR, decision tree regressor, and random forest regressor. The program takes the R-square of each fold and take an average of R-square across all store for each algorithm, and display the average R-square on the command line.

### AdaboostTraining.py
This program takes the training data from [Part 2 Data folder](../../USRetail/Data), conduct 10-fold with each store sales by training predictive model only adaptive boosting. The program takes the R-square of each fold and take an average of R-square across all store for each algorithm, and display the average R-square on the command line.

### XgboostTraining.py
This program takes the training data from [Part 2 Data folder](../../USRetail/Data), conduct 10-fold with each store sales by training predictive model with gradient boosting. The program takes the R-square of each fold and take an average of R-square across all store for each algorithm, and display the average R-square on the command line.

### PredictAlgos.py
This program takes the training data from [Part 2 Data folder](../../USRetail/Data) and train the predictive models with all selected algorithms without partitioning the data set. The program would take the same features in the training data to obtain the prediction and save csv files in the <i>Results</i> folder. All the results will be saved in the format of <i>xxxx_prediction.csv</i> where xxxx is the algorithm name.

### Dashboard_modelsPred.py
This program is a dashboard to visualize the prediction from <i>PredictAlgo.py</i> with line chart. This dashboard is a tool to help evaluating the models in this phase.

## Dashboard
The dashboard is ran by <i>Dashboard_modelsPred.py</i> which visualize the sales of all stores and selected store in 2 tab. The 1st tab visualizes the overall sales across all stores; the 2nd tab allows users to select a store and visualize the prediction of the selected store. The dashboard is aimed to help us to identify whether the models were able to capture the sales trend and seasonality pattern.
<br><br>
The dashboard by default goes to Tab 1, which visualize the overall sales across all store. The line chart visualizes both training data and prediction. The user may change the algorithm in the drop down box below the title, the line chart will update the prediction line from the data made from that model. It looks like this:
<br>
<img src="tab1.png">
<br><br>
Tab 2 visualizes the prediction of individual store. There is an extra drop down list to select the store in the US Retail chain, the line chart will visualize both training data and prediction accordingly. Like Tab 1, users may change the algorithm to update the prediction data. It looks like this:
<br>
<img src="tab2.png">


## Results
This time, we are going to evaluate models with 2 criterias: Evaluate with Accuracy (R-square) and Evaluate with visualizations (Whether the trend and seasonality pattern is captured).

### Evaluation with Accuracy
The accuracy of the models are:
<ul>
	<li>Linear Regression: 42.66% R-square</li>
	<li>SVR: Negative R-square</li>
	<li>Decision Tree Regressor: 83.45% R-square</li>
	<li>Random Forest Regressor: 87.65% R-square</li>
	<li>Adaptive Boosting: 87.22%</li>
	<li>Gradient Boosting: 86.54%</li>
</ul>


### Evaluation with Visualization
The overall sales and Store 5 sales predicted by Linear Regression Model:
<br>
<img src="overall_lr.png">
<br>
<img src="store5_lr.png">
<br><br>
The overall sales and Store 5 sales predicted by Random Forest Regressor Model:
<br>
<img src="overall_rf.png">
<br>
<img src="store5_rf.png">
<br><br>
The overall sales and Store 5 sales predicted by Adaptive Boosting Model:
<br>
<img src="overall_adaboost.png">
<br>
<img src="store5_adaboost.png">
<br><br>
The overall sales and Store 5 sales predicted by Gradient Boosting Model:
<br>
<img src="overall_xgboost.png">
<br>
<img src="store5_xgboost.png">

### Evaluation on Linear Regression Model
This model was able to capture the trend and seasonality pattern but the accuracy score is relatively low. Looking at the line chart, we can see the prediction is consistently off from the training data. The R-square is 42.66% which is a good benchmark for baseline model.

### Evaluation on SVR
This model achieved a negative R-square that it suggests this model may not as useful as taking sales average. So, we are not going to consider this model.

### Evaluation on Decision Tree Regressor
The previous prediction model was trained with decision tree regressor but it does not stop us to explore the possibility of using this algorithm. However, after training with more training data from other stores, the accuracy dropped to 83.45%. It reflects that the model used in other stores may not be as useful as the model used only in Store 1. 

### Evaluation on Random Forest Regressor
The accuracy of this model is the highest among 5 algorithms: 87.65%. The model also seems to able to capture the sales trend and seasonality pattern. This model can be selected as one of the considerable model for the final prediction model.

### Evaluation on Adaptive Boosting Model
This model has achieved 87.22% R-square which ranks the 2nd among 5 algorithms. However, it seems like the model is not able to capture the sales trend and seasonality pattern. Therefore, this model may not be useful for us. 

### Evaluation on Gradient Boosting Model
This model has achieved 86.54% R-square which ranks the 3rd among 5 algorithms. The accuracy does not differ a lot from the accuracy of Random Forest Regressor. It seems like the model seems to able to capture the sales trend and seasonality pattern. This model can be selected as one of the considerable model for the final prediction model.


## Verdict
Coming Soon..

## Next Step
After we have selected the algorithm to train the prediction model, we are going to build the refined prototype prediction model. You may find the detail in the [Refined folder](../RefinedModel).
