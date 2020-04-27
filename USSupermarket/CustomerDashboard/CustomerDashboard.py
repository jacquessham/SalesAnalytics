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
	html.H1(children=headline, style={'text-align':'center'}),
	# Position 0, headline
	dcc.Tabs(id='dashboard-tab', value='bar', children=[
		dcc.Tab(label='Bar Chart', value='bar', children=tab1_layout), 
		# 1st tab
		dcc.Tab(label='Scatter Plot', value='scatter', children=tab2_layout), 
		# 2nd tab
		dcc.Tab(label='Box Plot', value='box', children=tab3_layout) 
		# 3rd tab
	]) # Close Tabs, Position 1, Tabs
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
	temp = {}
	if metric != 'mode':
		df = customers.groupby(x_col).agg(metric).reset_index()
	else:
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
	# If it is gender, shrink the width of bar
	if x_col == 'Gender':
		temp['width'] = [0.2, 0.2]
	data.append(temp)

	layout = dict(title=plot_title, 
	          xaxis={'title':axis_title[x_col]},
	          yaxis={'title':axis_title[y_col], 'range': [0, y_max*1.1]},
	          transition={'duration': 500}, hoverlabel={'bgcolor':'white'})

	return {'data': data, 'layout': layout}

# Callback for scatterplot
@app.callback(Output('vis-scatter','figure'),
	          [Input('scatter-radio-xaxis','value'),
	           Input('scatter-radio-yaxis','value')])
def update_scatterplot(x_col, y_col):
	y_max = customers[y_col].max()
	data = go.Scatter(x=customers[x_col], y=customers[y_col],
					  hovertemplate=axis_title[x_col] + ': ' + \
		                            customers[x_col].astype(str) + '\t' + \
		                            axis_title[y_col] + ': ' + \
		                            customers[y_col].round(2).astype(str) + \
		                            '<extra></extra>',
		              mode='markers')
	plot_title = ''
	layout = dict(title=plot_title, 
	              xaxis={'title':axis_title[x_col]},
	              yaxis={'title':axis_title[y_col], 'range': [0, y_max*1.1]},
	              showlegend=False, transition={'duration': 500},
	              hoverlabel={'bgcolor':'white'})
	return dict(data=[data], layout=layout)

# Callback for boxplot
@app.callback(Output('vis-box','figure'),
	          [Input('box-radio-xaxis','value'),
	           Input('box-radio-yaxis','value')])
def update_boxplot(x_col, y_col):
	x_uniques = customers[x_col].unique()
	y_max = customers[y_col].max()
	data = []
	for x_elem in x_uniques:
		y = customers[customers[x_col]==x_elem][y_col].tolist()
		data.append(go.Box(y=y, name=str(x_elem),
			               fillcolor='royalblue',line={'color':'royalblue'}))

	plot_title = ''
	layout = dict(title=plot_title, 
	              xaxis={'title':axis_title[x_col]},
	              yaxis={'title':axis_title[y_col], 'range': [0, y_max*1.1]},
	              showlegend=False, transition={'duration': 500},
	              hoverlabel={'bgcolor':'white'})
	return dict(data=data, layout=layout)

if __name__ == '__main__':
    app.run_server(debug=True, port=1300)
