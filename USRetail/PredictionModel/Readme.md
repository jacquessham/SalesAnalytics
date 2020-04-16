# Prediction Model
This is folder for the final prediction model to predict the department-wide weekly sales between 2013-2014, or beyond. 

## How this Model works
The model is trained by Temperature, Fuel price, Consumer Price Index, and Unemployment rate from each store with Decision Tree Regressor. The model creates 45 prediction models (Or the number of stores in the retail chain) which predicts the weekly sales of each store. The department weekly sales will be calculated by the store weekly sales average share of that department. In order to predict the weekly sales of each department of each store, simply gather the feature data for each store and the model will return the weekly sales of each department of each store.
<br><br>
The training data will be using the [refined feature data set](../Data/Refined/features_dataset_refined.csv) in the [Data/Refined folder](../Data/Refined) and [sales data set](../Original/sales_dataset.csv) in the [Data/Original folder](../Data/Original)

## Files
There are 3 files in this folder:
1. USRetailSalesPrediction.py - The driver program that run the model
2. Store.py - The code define the store object which train the prediction model and save the results
3. MacroPrediction.py - The prediction model that predict the Macro data which is not available (Macro data is time-series data)

## Preparing Feature Data
Note that the data of the Macro data is time-series data, that the Macro data is needed to be predicted using time-series statistical learning. The file MacroPrediction.py is able to predict the macro data in order to prepare the feature data for predicting the weekly sales of each store. The training data, besides train the prediction model for weekly sales, is also used for predicting future Macro data. MacroPrediction.py is called in USRetailSalesPrediciton.py when preparing feature data for predicting future weekly sales.
<br><br>
MacroPrediction.py has two functions: 
* predictColumn()
* predict()
<br><br>
predict() predicts the future data from a list of given future dates. This function is called from predictColumns().
<br><br>
When predictColumn() is called in USRetailSalesPrediction.py, this function received the year that needed to be predicted, training data, list of columns needed to be prepared, and the list of holiday weeks. This function prepares the list of weeks along with Macro Data by calling predict(). Once the Macro data is prepared and return to USRetailSalesPrediction.py and ready to predict.

## Store Object
Store.py is designed to create Store object which saved the meta data of a given store, training data, and prediction. There are 10 instances in the object:
* store_num: Label of the store, received from the driver code
* df: Training data of the store less the features without weekly sales (Rows without weekly sales is not able to be trained in the model), received from the driver code. The data should be saved in Pandas dataframe.
* X_train: Feature data from the training data, the list of features received from driver code, X_train is selected from df by partition with the list of features. The data should be saved in Pandas dataframe.
* y_train: Weekly Sales from the training data, it is partition from df
* deptDisb: The dictionary of list of department and its average weekly sales share, it is calculated by calling deptDisb(), deptDisb() has all the necessary parameters when calling this function. The data is saved in dictionary, with department number as key, the value is the weekly sales share.
* dt: The Decision Tree Regressor object trained by the training data, it is set by calling modeltraining(), modeltraining() has all the necessary parameters when calling this function.
* X_pred: The feature data for predicting store weekly sales, when creating Store object, this instance is null. The data should be saved in Pandas dataframe.
* y_pred: The prediction of store weekly sales, when creating Store object, this instance is null.The data should be saved in Pandas dataframe.
* y_pred_dept: The prediction of all department weekly sales in this store, when creating Store object, this instance is null.The data should be saved in Pandas dataframe.
<br>
The depth is set to 3 for the Decision Tree Regressor model.
<br><br>

### Functions
There are 7 functions in this object:
<ul>
	<li>deptDisb() - Helper function when creating this object</li>
	<li>modelTraining() - Helper function when creating this object</li>
	<li>predict() - Function written to be called in USRetailSalesPrediction.py</li>
	<li>predict_dept() - Helper function for predict()</li>
	<li>getYPred() - Getter function</li>
	<li>getXPredYPred() - Getter function</li>
	<li>getDeptPred() - Getter function</li>
</ul>

Notes:
* deptDisb() and modelTraining() is designed to be called in __init__(), when these functions are called in __init__(), all the parameters needed is set in the previous line in __init__() already
* predict_dept() is the helper function in predict(), once the store prediction is ready in predict(), predict_dept() is called to calculate the weekly sales of each department in this store on all dates, and save the result in y_pred_dept
* predict() is the function to make prediction, it receives all needed parameters from USRetailSalesPrediction.py. The predictions are saved in the object and do not return back. To get the results, use the getter functions.
* getYPred() - Getter function of getting store-wide weekly sales
* getXPredYPred() - Getter function of getting store-wide weekly sales along with feature data, in the same format as feature data set in the [Data folder](../Data)
* getDeptPred() - Getter function of getting department-wide weekly sales, in the same format as sales data in the [Data folder](../Data)

## The Driver Program
The driver program read all training data and train one model of each store. It reads the following files:
<ul>
	<li>Refined Features Data in Data/Refined</li>
	<li>Sales Data in Data/Original</li>
	<li>List of holiday weeks Data/Refined</li>
</ul>
The program identifies the data for each store, then it creates a Store object which trains the prediction model. After that, it calls MacroPrediction.py to prepared feature data and call predict() in Store object to make the prediction in store-wide and department-wide level. Once all those steps are done, the Store object is stored in the model_dict dictionary, where the key is the store number, the value is the Store object.
<br><br>
When the program is done creating all Store objects and the prediction, the driver program will obtain the prediction from all Store objects and save the prediction in csv files, same as feature data file and sales data file.

## Result
You may find the result in csv files in the [Results folder](/Results)

## Thought on the Result
The weekly sales does not vary too much that I suspect the model may be overfitted. There may be more work could be done to make the model is more useful. However, I think this model has achieve our goal making prediction on department-wide weekly sales of all department in all stores. 