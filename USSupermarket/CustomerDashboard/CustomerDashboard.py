import pandas as pd
from scipy.stats import mode
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from Layouts import *


# Read files
customers = pd.read_csv('../Data/Supermarket_CustomerMembers.csv')

# Dash Set up
app = dash.Dash()

# Dashboard layout
app.layout = html.Div([
	html.H1(children=headline),
	# Position 0, headline
	html.Div(children=description),
	# Position 1, description
	dcc.Tabs(id='dashboard-tab', value='bar', children=[
		dcc.Tab(label='Bar Chart', value='bar', children=tab1_layout), 
		# 1st tab
		dcc.Tab(label='Scatter Plot', value='scatter', children=tab2_layout), 
		# 2nd tab
		dcc.Tab(label='Box Plot', value='box', children=tab3_layout) 
		# 3rd tab
	]) # Close Tabs
]) # Close Div

# Callback for bar chart
@app.callback(Output('vis-bar','figure'),
	          [Input('bar-radio-xaxis','value'),
	           Input('bar-radio-yaxis','value'),
	           Input('bar-metircs-dropdown','value')])
def update_barchart(x_col, y_col, metric):
	# Select the columns
	df = customers[[x_col, y_col]]
	# Layout setting
	y_max = df[y_col].max()

	# Prepare the data for the plot
	data = []
	plot_title = ''
	# Pandas has no mode(), need to custom a lambda function for that
	if metric != 'mode':
		temp = {}
		df = customers.groupby(x_col).agg(metric).reset_index()
		temp['x'] = df[x_col]
		temp['y'] = df[y_col]
		temp['hovertemplate'] = axis_title[x_col] + ': ' + \
		                        df[x_col].astype(str) + '\t' + \
		                        axis_title[y_col] + ': ' + \
		                        df[y_col].round(2).astype(str) + \
		                        '<extra></extra>'
		temp['type'] = 'bar'
		data.append(temp)
	else:
		temp = {}
		df = customers[[x_col,y_col]].groupby(x_col) \
		              .agg({y_col: lambda x:mode(x)[0]}) \
		              .reset_index()
		temp['x'] = df[x_col]
		temp['y'] = df[y_col]
		temp['hovertemplate'] = axis_title[x_col] + ': ' + \
		                        df[x_col].astype(str) + '\t' + \
		                        axis_title[y_col] + ': ' + \
		                        df[y_col].round(2).astype(str) + \
		                        '<extra></extra>'
		temp['type'] = 'bar'
		data.append(temp)

	layout = dict(title=plot_title, 
	          xaxis={'title':axis_title[x_col]},
	          yaxis={'title':axis_title[y_col], 'range': [0, y_max*1.1]},
	          transition={'duration': 500})

	return {'data': data, 'layout': layout}

# Callback for scatterplot
@app.callback(Output('vis-scatter','figure'),
	          [Input('scatter-radio-xaxis','value'),
	           Input('scatter-radio-yaxis','value')])
def update_scatterplot(x_col, y_col):
	data = go.Scatter(x=customers[x_col], y=customers[y_col],
					  hovertemplate=axis_title[x_col] + ': ' + \
		                            customers[x_col].astype(str) + '\t' + \
		                            axis_title[y_col] + ': ' + \
		                            customers[y_col].round(2).astype(str) + \
		                            '<extra></extra>',
		              mode='markers')
	return dict(data=[data])

# Callback for boxplot
@app.callback(Output('vis-box','figure'),
	          [Input('box-radio-xaxis','value'),
	           Input('box-radio-yaxis','value')])
def update_boxplot(x_col, y_col):
	return None


if __name__ == '__main__':
    app.run_server(debug=True, port=1300)