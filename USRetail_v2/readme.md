# Part 3 - US Retail Analytics Version 2.0
After building a sales prediction model in Part 2 for a US Retail chain, the result of the sales prediction model is not useful enough of forecasting future sales of each store. To be specific, the prediction made from that model only produced 2-3 values for 36 months periods. It is not helpful for the management to understand the sales insight nor forecasting the sales. Our goal in this part is to rebuild the sales prediction model to improve the quality of the forecasting ability.

## Background
The sales prediction model in Part 2 for a US Retail chain is not useful enough of forecasting future sales of each store. After visualizating the prediction, I have realized the prediction model was not able to capture the trend nor seasonality of the sales. Although the predictive model achieved a very high R-square accuracy, I believe the model was overfitted to the training data set. Take Store 1 for example, the sales prediction made for Store 4 looks like this:
<br>
<img src="Background/store.png">
<br>
<br>
Although the prediction model achieved 86.51% R-Square after tuning, the prediction plot is flat and the model seems to have very high bias. In the effort of make high-quality sales forecast, we shall rebuild the sales prediction model which is able to capture trend and seasonality of the sales pattern. You may go to the [Background folder](Background) to learn more about the background of this part of the project and the dashboard to visualize the prediction made in Part 2.

## Model Training
We have explore the data set in Part 2 already so we have so idea of how is the data set looks like, you may find the detail in the [EDA folder](../USRetail/EDA) in Part 2. Similar to the Model Training phase in Part 2, we will explore which algorithm to be used in the prediction model with different standards to prevent high bias of the prediction model. You may find the detail in the [Model Training folder](ModelTraining). A dashboard to visualize the findings may also be found in this folder.
<br><br>
As the result, random forest regressor, and gradient boosting have achieved the highest accuracy. Since a model trained with gradient boosting model is able to capture seasonality better, the final prediction model will be trained with gradient boosting.

## Final Prediction Model
The final refined prediction model is built to replace the old prediction model. The structure is similar to the old prediction model to prepare feature data but the feature data will be trained with gradient boosting. The prediction looks more useful than the old prediction model. You may more detail about the refined prediction model and the visualization of the prediction in the [Final Prediction Model](RefinedModel).

## Next Part
In the next part, we will look at a US supermarket to help the management to make analysis and develop dashboards to make data-driven decisions. You may click <a href="https://github.com/jacquessham/SalesAnalytics/tree/master/USSupermarket">here</a> to find more about next part.

