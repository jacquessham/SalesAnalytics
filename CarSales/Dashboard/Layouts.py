import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html


headline = 'Dashboard of Car Sales and Features'
direction = '''
				The goal of this dashboard is to display the relationship between
				car sales and car features. You may select a car feature on the
				x-axis. The dashboard in default display all makes available in 
				the dealership. You may select include or exclude the make(s) you
				wish or not wish to include in the scatter plot.
			'''

def get_div_options(opts_x, opts_make):
	opts_make = sorted(opts_make)
	opts_x = sorted(opts_x)

	div_options = [
		html.Div([
			html.P('X-axis'),
			dcc.Dropdown(
				id='xaxis-dropdown',
				options=[{'label': opt, 'value': opt} for opt in opts_x],
				value='Price',
				style={'width':'80%', 'text-align': 'left'}
				)
			],style={'width':'30%','display': 'inline-block',
						      'vertical-align': 'middle'}),
		# Position 0, dropdown list for x-axis


		html.Div([
			html.P('Make'),
			dcc.Dropdown(
				id='make-dropdown',
				options=[{'label': opt, 'value': opt} for opt in opts_make],
				value='all',
				multi=True,
				style={'text-align': 'left'}
				)
			], style={'width':'30%','display': 'inline-block',
						      'vertical-align': 'middle'}),
		# Position 1, dropdown list for makes
		html.Div(style={'width':'5%','display': 'inline-block',
					    'vertical-align': 'middle'}),
		html.Div([
			html.Br(),
			html.Br(),
			dcc.RadioItems(
				id='include-radio',
				options=[{'label': 'Include', 'value': 'Include'},
				         {'label': 'Exclude', 'value': 'Exclude'}],
				value='Include',
				labelStyle={'display':'block','text-align': 'left'}
				)
		], style={'width':'20%','display': 'inline-block',
					      'vertical-align': 'middle'})
		# Position 2, radio button for include/exclude
	]
	return div_options

def get_scatterplot(df, makes, x):
	y_max = df['Sales_k'].max()
	data = []

	for make in makes:
		df_temp = df[df['Manufacturer']==make]
		# print(df_temp)
		data.append(go.Scatter(
			x=df_temp[x], y=df_temp['Sales_k'], name=make,
			hovertemplate='Make'+': '+make+'\t'+ \
						  x+': '+df_temp[x].astype(str)+'\t\t'+ \
			              'Sales (In thosand): '+'\t'+\
			              df_temp['Sales_k'].astype(str)+\
			              '<extra></extra>',
		    mode='markers'
			))
	layout = dict(xaxis={'title': x},
                  yaxis={'title':'Sales (In thousand)',
                         'range': [0, y_max*1.1]},
                  showlegend=True, transition={'duration': 500},
                  hoverlabel={'bgcolor':'white'})

	return {'data': data, 'layout': layout}