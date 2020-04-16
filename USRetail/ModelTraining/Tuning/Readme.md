# Tuning
The goal is to tune the hyperparameters for the Decision Tree Regressor Model by performing grid search to improve the accuacry. We use R-square and RMSE for evaluation. If we have the same R-square, we may use RMSE to for further evaluation. The best model has the highest R-square or lowest RMSE.

## Strategy
The hyperparameters to tune: max_depth in Decision Tree Regressor.
<br><br>
The default setting: max_depth = 3
<br><br>
Use grid search to train the adaptive boosting models to find which hyperparameter setting achieve the lowest RMSE.
<br><br>
The range of max_depth is 3-10,15,20,25,30,35,40,45,50.
<br><br>
The file [DtTuning.py](DtTuning.py) will obtain the R-square and RMSE of each model and save to [TuningResult.csv](TuningResult.csv).

## Results
Once we have R-square and RMSE for each model, we save the data to [TuningResult.csv](TuningResult.csv). As the result, the model with max_depth = 3 achieve the lowest RMSE. We will use this hyperparameters for the final prediction model. 

## Next Step
We will build the final prediction model, you may find the model [here](../../PredictionModel)