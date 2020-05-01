# Dashboard on Relationship between Car Sales and Car Features
The goal is to build a dashboard to display the relationship between car model lifetime car sales and the numeric features of the car models on a scatter plot.

## Background and Strategy
The best way for managerment to understand the general relationship between car sales and car model features is to look at an interactive dashboard. As we have found out the data is distributed sparsely, the best way to display this type of data is to visualize on a scatter plot. Since car sales is the only KPI, car sales is the only feature on y-axis on the dashboard, while the dashboard allows users to select any numeric features on x-axis. We have learnt that car make is one of the important indicator for car sales, the dashboard also offers user to look at car makes on the colour of the scatter point. Another dashboard feature is to allow users to include or exclude car makes for users to look at the trend with condition.

## Files
There are 2 python files in this folder:
<ul>
	<li>CarsalesDashboard.py - Driver program to run the dashboard</li>
	<li>Layout.py - Helper code to define the layout of the dashboard</li>
</ul>

## CarsalesDashboard.py
This is the driver program to run the dashboard. The program contains 3 parts:
<ol>
	<li>Data Preparation</li>
	<li>Dashboard Layout</li>
	<li>Dashboard Callbacks</li>
</ol>
<br>
In Data Preparation, the program use Pandas to read csv files, which the program use the <a href="">original data</a>. You may find more detail in the <a href="">data folder</a>. The program first handles NA's and turn the numeric features to float type in the data frame. After that, the program calculates the resales value ratio by dividing the 4 years resales value by original price. 
<br><br>
The dashboard contains 4 components: Title, direction, box of options, and the visualization. There are three options available for users. First, there is a dropdown list for user to select a feature on x-axis. Second, a multi-selection dropdown list for user to include or exclude car makes. And at last, a radio button list for user to select include or exclude car makes for the second dropdown list. In default, the dashboard include all car makes. In the exclude option, there is no option for user to exclude all options. The default setting if exclude is selected is no make excluded. The code contains a base layout of the dashboard, each component relies on the detail layout from the <i>Layout.py</i> code. The default setting of x-axis is Price.
<br><br>
There are two call backfunctions:
<ol>
	<li>update_dropdown()</li>
	<li>update_graph()</li>
</ol>

### update_dropdown()
This callback function is to change the placeholder of the multi-selection dropdown list to notify users to include or exclude make if they wanted to. Only two cases accounted: Included or Excluded selected on the radio button. 

### update_graph()
This callback function is to update the scatter plot based on what the users selected. There are three parameters which pass the values from all options available. First, the function would filter the make and car sales columns, and the columns based on what x-axis selected. If car makes are to included or excluded, the condition function would filter the car makes ordered by the user. If nothing is included or exclude, the list of makes selection is empty, the function has to obtain all makes in the data set in order to have Plotly to colour the data point. Once the data is manipulated, it will call get_scatterplot() in <i>Layouts.py</i> to create a scatter plot.

## Layout.py
The <i>Layout.py</i> program is a helper code for <i><CarsalesDashboard.py</i>. The code contains 2 static variables and 2 functions. The static variables are tilte and direction of the dashboard. The 2 functions are get_div_options() and get_scatterplot().
<br><br>
get_div_options() could be a static variable itself. The reason it is a function because it sort the options of dropdown lists content first before building the layout. It requires two inputs, both are the list of options available in either dropdown list. get_scatterplot() returns a scatter plot. The function only plot the scatter plot, any data manipulation is done before calling this function.

## Result
The dashboard looks like this in default:
<br>
<image src="Images/Default.png">
<br><br>
If the user change the x-axis, it looks like this:
<br>
<image src="Images/Resalesratio.png">
<br><br>
When the user include some car makes, the scatter plot becomes:
<br>
<images src="Images/Include.png">
<br><br>
Or if two car makes are excluded from the plot, the scatter plot becomes:
<br>
<images src="Images/Exclude.png">


## Next Step
The next goal is to build a prediction model to predict the lifetime car sales of car models. The next phase is Model Training. You may find more detail in the [Model training folder](../ModelTraining)