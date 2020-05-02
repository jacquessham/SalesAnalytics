import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from ReadData import *
from Layout import *
from Prediction import *


filepath = '../Data/Market_Basket_Optimisation.csv'
data_dict = readfiles(filepath)


# Dashboard options set up
products_avail = sorted(list(data_dict['product2num'].keys()))

# Dash Set up
app = dash.Dash()

# Dropdown list options set up
app.layout = html.Div([
	html.H1(children=headline, style={'text-align':'center'}),
	# Position 0, headline
	html.P(children=direction, style={'width':'80%','margin':'auto'}),
	# Position 1, direction,
	html.Br(),
	# Position 2, next line
	html.Div(children=get_div_dropdown(products_avail)),
	# Position 3, div for dropdown
	html.Div(children=get_div_vis())
	# Position 4, div for visualization
	])

@app.callback([Output('left-vis','figure'), Output('right-vis','figure')],
	          [Input('item-dropdown','value')])
def display_graph(items):
	result_items, result_basketnum = getProb(data_dict['transaction_tabluar'],
		                                     items)
	# Sort the items by highest probability
	result_items = [(k, result_items[k]) for k in result_items]
	result_items = sorted(result_items, key=lambda elem: elem[1], 
		                  reverse=True)
	# Sort the basketnum by number of items
	result_basketnum = [(k, result_basketnum[k]) for k in result_basketnum]

	return getBarChart(result_basketnum[:10]), \
	       getBarChart(result_items[:10],'right')


if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
