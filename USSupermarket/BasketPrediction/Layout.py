import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html


def get_div_dropdown(options):
	return dcc.Dropdown(
						id='item-dropdown',
						options=[{'label': prod.title(), 'value': prod} \
						         for prod in options],
						multi=True
					)

def get_div_vis():
	return [html.Div(dcc.Graph(id='left-vis'),
		             style={'width':'48%', 'display':'inline-block'}),
	        html.Div(dcc.Graph(id='right-vis'),
	        	     style={'width':'48%', 'display':'inline-block'})]

def getBarChart(results, pos='left'):
	x = [k for k, v in results]
	y = [v for k, v in results]
	data = [{'x':x, 'y':y, 'type':'bar','textposition':'outside',
	         'texttemplate': '%{y:.2f}'}]
	if len(results) < 4:
		data[0]['width'] = 0.2


	if pos=='right':
		chart_title = 'Probability of What Customer would Buy'
		xaxis_title = 'Items'
	else:
		chart_title = 'Probability of Items in the Shopping Cart'
		xaxis_title = 'Number of Items in Shopping Cart'

	layout = {'title': chart_title,
	          'xaxis':{'title': xaxis_title, 'tickmode':'linear'},
	          'yaxis':{'title':'Probability','range':[0,1]},
	          'hoverlabel':{'bgcolor':'white'}}
	return {'data':data, 'layout':layout}

headline = 'Basket Prediction'
direction = '''
	This dashboard is to predict what customers would buy given what
	they have put in the basket. You may select the items and obtain
	the probability of what items the customers would put next in the
	basket and the probability of how many items they would have in
	the basket. You may select the available items in the following
	dropdown list. You may select more than 1 item. 
'''
