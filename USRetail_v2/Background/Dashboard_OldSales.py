import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# Read files
filepath = '../../USRetail/PredictionModel/Results/'
df_store = pd.read_csv(filepath + 'sales_store_prediction.csv')
df_depts = pd.read_csv(filepath + 'sales_prediction.csv')

stores = df_store['Store'].unique()
store_opts = [{'label': 'Store '+str(store), 'value':store}
               for store in stores]

depts = df_depts['Dept'].unique()
dept_opts = [{'label': 'Department '+str(dept), 'value':dept}
              for dept in depts]

# Dash Set up
app = dash.Dash()

# Plot graph for overall sales
def generate_linechart(df_store):
	df_store = df_store[['Date', 'Weekly_Sales']].groupby('Date') \
	                   .sum().reset_index()
	ymax = df_store['Weekly_Sales'].max()*1.1
	data = [go.Scatter(x=df_store['Date'], y=df_store['Weekly_Sales'],
		               mode='lines')]

	layout = {'xaxis':{'title':'Date'},
	          'yaxis':{'title':'Sales ($)', 'range': [0, ymax]},
	          'showlegend':False}
	return {'data':data, 'layout':layout}



# Dashboard layout
app.layout = html.Div([
	html.H1(children='Sales Prediction from Version 1 Predictive Model',
	        style={'text-align':'center'}),
	# Position 0, headline
	dcc.Tabs(id='dashboard-tab', value='overall', children=[
		dcc.Tab(label='Overall Sales', value='overall', 
			    children=html.Div([
							 html.Br(),
							 html.H2('Overall Sales'),
							 dcc.Graph(
							 	       figure=generate_linechart(df_store))
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
				  ])), 
		# 2nd tab
		dcc.Tab(label='Department-wide Sales', value='department',
			    children=html.Div([
							  html.Br(),
							  html.H2('Department-wide Sales'),
							  html.Div([html.Div([
							  	            dcc.Dropdown(
										    id='tab3-dropdown-store',
										    options=store_opts,
										    value=store_opts[0]['value']
										 )], style={'display':'inline-block',
							  	                    'width':'20%'}),
							  			html.Div([
										dcc.Dropdown(
										    id='tab3-dropdown-department',
										    options=dept_opts,
										    value=dept_opts[0]['value'])],
										style={'display':'inline-block',
										       'width':'20%'}
							  	)]),
							  dcc.Graph(id='vis-tab3')
				  ])) 
		# 3rd tab
	]) # Close Tabs, Position 1, Tabs
]) # Close Div

## Call back function for tab 2
@app.callback(Output('vis-tab2','figure'), [Input('tab2-dropdown','value')])
def tab2_linechart(store):
	df_temp = df_store.copy()
	df_temp = df_temp[df_temp['Store']==store]
	return generate_linechart(df_temp)

## Call back function for tab 3
@app.callback(Output('vis-tab3','figure'), 
	          [Input('tab3-dropdown-store','value'),
	           Input('tab3-dropdown-department','value')])
def tab3_linechart(store, dept):
	df_temp = df_depts.copy()
	df_temp = df_temp[(df_temp['Store']==store) & (df_temp['Dept']==dept)]
	return generate_linechart(df_temp)


if __name__ == '__main__':
    app.run_server(debug=True, port=2000)