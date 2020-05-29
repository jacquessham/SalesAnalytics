# Final Refinded Prediction Model
This folder is for the final refined prediction model to predict the department-wide weekly sales between 2013-2014, or beyond.

## How this Model Works
This model has the same structure with the previous [Prediction model](../../USRetail/PredictionModel) in Part 2 but the sales predictive part is trained with gradient boosting algorithm and extra features, ie, Markdowns 1-5. The model creates 45 prediction models (Or the number of stores in the retail chain) which predicts the weekly sales of each store. The department weekly sales will be calculated by the store weekly sales average share of that department. In order to predict the weekly sales of each department of each store, simply gather the feature data for each store and the model will return the weekly sales of each department of each store. The feature data is prepared in the same way as the previous [Prediction model](../../USRetail/PredictionModel) in Part 2. You may go to that folder to find the detail on how the feature is prepared.

## Files
There are 4 Python files in this folder:
<ul>
	<li>USRetailSalesPrediction_v2.py - The driver program that run the model</li>
	<li>Store.py - The code define the store object which train the prediction model and save the results</li>
	<li>MacroPrediction.py - The prediction model that predict the Macro data which is not available (Macro data is time-series data)</li>
	<li>Dashboard_RefinedModel.py - Dashboard to visualize the result</li>
</ul>
<br><br>
<i>Store.py</i> and <i>MacroPrediction.py</i> are the same with the Prediction model](../../USRetail/PredictionModel) in Part 2, except the predictive model in the <i>Store.py</i> code is trained with gradient boosting algorithm. <i>USRetailSalesPrediction_v2.py</i> has the same structure as <i>USRetailSalesPrediction.py</i> but it has added Markdown1-5 as part of the features.
<br><br>
<i>Dashboard_RefinedModel.py</i> is the dashboard to visualize the result from <i>USRetailSalesPrediction_v2.py</i>.

## Packages Needed
This is the list of packages used in the application:
1. Pandas
2. Numpy
3. Datetime
4. Math
5. Dateutil
6. Sklearn - Decision Tree Regressor
7. Facebook Prophet

## The Driver Program
Same as the previous model, the driver program read all training data and train one model of each store. It reads the following files:
<ul>
	<li>Refined Features Data in Data/Refined</li>
	<li>Sales Data in Data/Original</li>
	<li>List of holiday weeks Data/Refined</li>
</ul>
The program identifies the data for each store, then it creates a Store object which trains the prediction model. After that, it calls MacroPrediction.py to prepared feature data and call predict() in Store object to make the prediction in store-wide and department-wide level. Once all those steps are done, the Store object is stored in the model_dict dictionary, where the key is the store number, the value is the Store object.
<br><br>
When the program is done creating all Store objects and the prediction, the driver program will obtain the prediction from all Store objects and save the prediction in csv files, same as feature data file and sales data file. The dashboard will read those csv files to visualize the result afterward.

## Dashboard
<i>Visualization_PredictedPrice.py</i> powers the dashboard and visualize the result findings. The program only visualize the prediction for 1 stock, the ticker must be changed in the code. The dashboard is for developer's use, so I did not build the dynamic selection on stocks. 
<br><br>
Prediction on General Eletrics (GE):
<img src="ge.png">
<br><br>
Prediction on Microsoft (MSFT):
<img src="msft.png">
