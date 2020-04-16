# Model Training
There are 4 phases within the model training phases.
1. Find out the perspective of the model, meaning whether we shall build the model based on each Store or each Department in each store. 
2. Find out which algorithm to use to build the prediction model.
3. Explore which features to include or exclude
4. Tune the prediction Model

## Building the Models based on each Store or each Department in each store
The first step is to find out the perspective of the model. It means whether the model is trained using aggregated department sales in a given store or using just only department sales in a given store. If we train using aggregated department sales in a given store, there is one prediction model in a given store to predict a aggregated weekly sales in a given store (Store Perspective); if we train using just only department sales in a given store, there is multiple prediction models in a given store that each prediction model predict the weekly sales of a given department in a given store (Department Perspective). The task is to find out using which perspective may achieve highest accuracy.
<br><br>
If we choose the route of training one prediction model in a given store, we will also have to estimate the sales proportion of each department of the given store. Once we have predicted the weekly sales in a given store, we will calculate the weekly sales of the individual department by multiplying the weekly sales in a given store times the sales proprotion of the given department.
<br><br>
In this phase, we will use linear regression model because this is the baseline algorithm. We will use R-square to determine the accuracy. We will choose the perspective whichever perspective has the highest R-square.
<br><br>
You may find more detail of the model training phase in this [folder](FindPerspective). As the result, the Store Perspective achieve the highest accuracy. So we will choose Store Perspective.


## Model Selection: Find the best algorithm for Prediction Model
The goal of this phase is to the find which prediction model built by different algorithm has the highest accuracy. You may find more detail [here](ModelSelection).
<br><br>
We have used the following algorithms:
1. Linear Regression
2. SVR
3. Decision Tree Regressor
4. Random Forest Regressor
5. Adaptive Boosting Regressor
6. Gradient Boosting Regressor
<br><br>
As the result, the model built by decision tree regressor achieve the highest accuracy, 92%. The final prediction model will be built by this algorithm.

## Exploring Features: Markdown1-5 and Date
The goal of this phase is to understand feature effect on weekly sales, mainly Markdown1-5 and Date. You may find more detail [here](ExploringFeatures).
<br><br>
As the result, including Markdown1-5 and Date as features did not help improving prediction accuracy.

## Tuning
The goal is tune the hyperparameter of the algorithm to improve prediction accuracy. As the result, using the default setting, ie, max_depth=3 for Decision Tree Regressor achieve the highest accuracy.

## Next Step
We will use all the above result to build the final prediction model. You may find more detail [here](../PredictionModel).
<br><br>
Summary:
* Prediction model will be built for each store
* Use Decision Tree Regressor as the algorithm
* Use Temperature, Fuel Price, CPI, Unemployment rate, Holiday Indicator as features
* The maximium depth for the Decision Tree Regressor is 3
