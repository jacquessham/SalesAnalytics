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
target = 'turkey'
# print(data_dict['transaction_tabluar'][target].tolist())
turkey_probs = getProb(data_dict['transaction_tabluar'],target, 
	                   data_dict['products_num'])
turkey_probs = [(key,turkey_probs[key]) for key in turkey_probs]
turkey_probs = sorted(turkey_probs, key=lambda elem: elem[1], reverse=True)
print(turkey_probs[:5])


# Dashboard options set up
products_avail = sorted(list(data_dict['product2num'].keys()))

# Dash Set up
app = dash.Dash()

# Dropdown list options set up
app.layout = html.Div([
	html.H1(children=headline, style={'text-align':'center'}),
	# Position 0, headline
	html.P(children=direction),
	# Position 1, direction,
	html.Div(children=get_div_dropdown(products_avail)),
	# Position 2, div for dropdown
	html.Div(children=get_div_vis())
	# Position 3, div for visualization
	])

if __name__ == '__main__':
    app.run_server(debug=True, port=8000)