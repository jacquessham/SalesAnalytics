# Prediction Model
This is the final prediction model to predict sales for the Burma supermarket chain. From the result in Model Training Phase, the final prediction model is built with Linear Regression with the following features:
* City
* Product Line
* Quantity
* isMember
* isMale
* Month
* Day
* Hour

## Application
The application consists 3 parts: Data Engineering, Model Training, and Prediction. 
<br><br>
The data engineering part consist a function, dataEngineering(). The function aggregates Quantity, number of members, number of male consumer by month, day, hour city and product line. dataEngineering() is able to manipulate training features data and prediction features data. However, the function only handles feature labels available in the training features data set. It means if the feature label found in prediction data set but not in the training data set would throw an error. Therefore, since there are only 3 cities and 7 production line available in training data set, the prediction data set should not have cities and production line not in the training data set.
<br><br>
The second part is Modeling Training. In this part, the model would recieve the data set and use this data set with all observations to train the prediction model with linear regression.
<br><br>
The third part is Prediction. In this part the model would read the data set for future prediction. It requires the same features as the training data set. Once the features is available, it would call the linear regression object to make the prediction. Since we do not have the future features data set available, this part is commented.

## Final Product
We have achieved the goals of this part of the project. Please refer to the [front page](..) for conclusion and thought.