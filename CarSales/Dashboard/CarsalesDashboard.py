import pandas as pd
import numpy as np
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from Layouts import *


# Read files
carsales = pd.read_csv('../Data/Car_sales.csv')
# Data Engineering
# Turn all period to NA
carsales = carsales.replace('.',np.nan)
carsales['Resale_value_4yrs'] = carsales['Resale_value_4yrs'].fillna(0)
# Drop the NA observation
carsales = carsales.dropna()
col_num = ['Sales_k','Resale_value_4yrs','Price','EngineSize','Horsepower',
           'Wheelbase','Width','Length','CurbWeight','FuelCapacity',
           'FuelEfficiency']
carsales[col_num] = carsales[col_num].apply(pd.to_numeric)
# Define Resales Ratio
carsales['ResalesRatio'] = carsales['Resale_value_4yrs']/carsales['Price']
# Define available feature in the dashboard
col_x = ['ResalesRatio','Price','EngineSize','Horsepower',
         'Wheelbase','Width','Length','CurbWeight','FuelCapacity',
         'FuelEfficiency']

makes = carsales['Manufacturer'].unique()

# Dash Set up
app = dash.Dash()

# Dashboard Layout
app.layout = html.Div([
	html.H1(children=headline, style={'text-align':'center'}),
	# Position 0, headline
	html.Div(children=direction,style={'width':'60%'}),
	# Position 1, direction to use this dashboard
	html.Div(children=get_div_options(col_x, makes)),
	# Position 2, Div for dropdown list and radio buttons
	html.Div(dcc.Graph(id='vis'), style={'text-align':'center',
		                                 'width': '85%',
		                                 'margin':'auto'})
	# Position 3, Div for dcc.Graph()
	])

# The placeholder display on the dropdown list
@app.callback(Output('make-dropdown','placeholder'),
              [Input('include-radio','value')])
def update_dropdown(selection):
	if selection == 'Exclude':
		return 'Select Make(s) to Exclude from the Graph'
	return 'All makes selected'


@app.callback(Output('vis','figure'),[Input('xaxis-dropdown','value'), 
	          Input('make-dropdown','value'), Input('include-radio','value')])
def update_graph(x, makes, include):
	df = carsales[['Manufacturer', 'Sales_k', x]]
	if 'all' in makes or len(makes)==0:
		# If select all, then makes is empty, fill all makes to include all data
		makes = carsales['Manufacturer'].unique()
	elif include == 'Include':
		df = df[df['Manufacturer'].isin(makes)]
	elif include == 'Exclude':
		df = df[~df['Manufacturer'].isin(makes)]
		makes = [make for make in carsales['Manufacturer'].unique() 
		         if make not in makes]

	return get_scatterplot(df, makes, x)

if __name__ == '__main__':
    app.run_server(debug=True, port=1500)