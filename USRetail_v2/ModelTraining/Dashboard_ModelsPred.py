import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# Read files
df_lr = pd.read_csv('Results/lr_prediction.csv')
df_dt = pd.read_csv('Results/dt_prediction.csv')
df_rf = pd.read_csv('Results/rf_prediction.csv')
df_adaboost = pd.read_csv('Results/adaboost_prediction.csv')
df_xgboost = pd.read_csv('Results/xgboost_prediction.csv')

stores = df_lr['Store'].unique()
store_opts = [{'label': 'Store '+str(store), 'value':store}
               for store in stores]
algo_opts = [{'label': 'Linear Regression', 'value': 'lr'},
             {'label': 'Decision Tree Regressor', 'value': 'dt'}, 
             {'label': 'Random Forest', 'value': 'rf'},
             {'label': 'Adaboost', 'value': 'adaboost'},
             {'label': 'XGboost', 'value': 'xgboost'}]

# Dash Set up
app = dash.Dash()

# Plot graph for overall sales
def generate_linechart(df_store):
	df_store = df_store[['Date', 'Weekly_Sales', 'Weekly_Sales_pred']] \
	                   .groupby('Date').sum().reset_index()
	df_store['Date'] = pd.to_datetime(df_store['Date'])
	df_store = df_store.sort_values(by=['Date'])
	print('In the graphing function')
	print(df_store)
	ymax = df_store['Weekly_Sales'].max()*1.1
	data = [go.Scatter(x=df_store['Date'], y=df_store['Weekly_Sales'],
		               mode='lines', name='Training Data'),
	        go.Scatter(x=df_store['Date'], y=df_store['Weekly_Sales_pred'],
		               mode='lines', name='Prediction')]

	layout = {'xaxis':{'title':'Date'},
	          'yaxis':{'title':'Sales ($)', 'range': [0, ymax]},
	          'showlegend':False}
	return {'data':data, 'layout':layout}

# Obtain the right data frame
def get_df(algo):
	if algo == 'dt':
		return df_dt.copy()
	elif algo == 'rf':
		return df_rf.copy()
	elif algo == 'adaboost':
		return df_adaboost.copy()
	elif algo == 'xgboost':
		return df_xgboost.copy()
	return df_lr.copy()



# Dashboard layout
app.layout = html.Div([
	html.H1(children='Sales Prediction from Model Training Phase',
	        style={'text-align':'center'}),
	# Position 0, headline
	dcc.Dropdown(
		id='algo-choice',
		options=algo_opts,
		value=algo_opts[0]['value']
		),
	# Position 1, dropdown lists
	dcc.Tabs(id='dashboard-tab', value='overall', children=[
		dcc.Tab(label='Overall Sales', value='overall', 
			    children=html.Div([
							 html.Br(),
							 html.H2('Overall Sales'),
							 dcc.Graph(id='vis-tab1')
						 ])), 
		# 1st tab
		dcc.Tab(label='Store-wide Sales', value='store',
			    children=html.Div([
							  html.Br(),
							  html.H2('Store-wide Sales'),
							  dcc.Dropdown(
							  	id='tab2-dropdown',
							  	options=store_opts,
							  	value=store_opts[0]['value']
							  	),
							  dcc.Graph(id='vis-tab2')
				  ])) 
		# 3rd tab
	]) # Close Tabs, Position 2, Tabs
]) # Close Div

## Call back function for tab 1
@app.callback(Output('vis-tab1','figure'), [Input('algo-choice','value')])
def tab2_linechart(algo):
	df_temp = get_df(algo)
	df_temp = df_temp[['Date','Weekly_Sales','Weekly_Sales_pred']].groupby('Date') \
	                 .sum().reset_index()
	return generate_linechart(df_temp)

## Call back function for tab 2
@app.callback(Output('vis-tab2','figure'),
	          [Input('algo-choice','value'), Input('tab2-dropdown','value')])
def tab2_linechart(algo, store):
	df_temp = get_df(algo)
	df_temp = df_temp[df_temp['Store']==store]
	return generate_linechart(df_temp)


if __name__ == '__main__':
    app.run_server(debug=True, port=2100)