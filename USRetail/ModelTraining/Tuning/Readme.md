# Tuning
The goal is to tune the hyperparameters for the Adaptive Boosting Model to improve the accuacry.

## Strategy
Two hyperparameters to tune: max_depth in Decision Tree Regressor and n_estimators in Adaptive Boosting.
<br><br>
The default setting: max_depth = 3, n_estimators = 50
<br><br>
Use grid search to train the adaptive boosting models to find which hyperparameter setting achieve the lowest RMSE.
<br><br>
The range of max_depth is 3-10,15,20,25,30,35,40,45,50.
<br>
The range of n_estimators is 10,20,30,...140,150.

## Results
Once we have R-square and RMSE for each model, we save the data in a csv file. As the result, the model with max_depth = 3, n_estimators = 10 achieve the lowest RMSE. We will use these hyperparameters for the final prediction model.