import dash_core_components as dcc
import dash_html_components as html


def get_div_dropdown(options):
	return dcc.Dropdown(
						options=[{'label': prod, 'value': prod} \
						         for prod in options],
						multi=True
					)

headline = 'Basket Prediction'
direction = 'Coming soon...'

def get_div_vis():
	return [html.Div(dcc.Graph(id='left-vis'),
		             style={'width':'48%', 'display':'inline-block'}),
	        html.Div(dcc.Graph(id='right-vis'),
	        	     style={'width':'48%', 'display':'inline-block'})]
