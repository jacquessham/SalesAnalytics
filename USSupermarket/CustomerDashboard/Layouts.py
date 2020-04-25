import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html


# Headline, description, layout of the dashboard
headline = 'Customer Dashboard'
description = 'Coming Soon...'
axis_title = {'Age': 'Age', 'Gender': 'Gender',
              'AnnualIncome': 'Annual Income ($k)',
              'SpendingScore': 'Spending Score (1-100)'}

# Tab 1 (Bar Chart) Layout
tab1_layout = html.Div([
	html.Br(),
	html.Div([html.P('Select X-axis:',style={'text-align': 'left'}),
			  dcc.RadioItems(
				  id='bar-radio-xaxis',
				  options=[{'label':'Age', 'value':'Age'},
					        {'label':'Gender', 'value':'Gender'}],
				  value='Age',
				  labelStyle={'display':'block', 'text-align': 'left'})
			    ], style={'width':'30%','display': 'inline-block',
				      'vertical-align': 'middle'}), # 1st Option
	html.Div([html.P('Select Y-axis:',style={'text-align': 'left'}),
			  dcc.RadioItems(
				  id='bar-radio-yaxis',
				  options=[{'label':'Annual Income', 'value':'AnnualIncome'},
					        {'label':'Spending Score', 'value':'SpendingScore'}],
				  value='AnnualIncome',
				  labelStyle={'display':'block', 'text-align': 'left'})
			    ], style={'width':'30%','display': 'inline-block',
				      'vertical-align': 'middle'}), # 2nd Option
	html.Div([html.P('Select Metrics:', style={'text-align': 'left'}),
			  dcc.Dropdown(
				  id='bar-metircs-dropdown',
				  options=[{'label':'Average', 'value':'mean'},
				           {'label':'Median', 'value':'median'},
				           {'label':'Minimum', 'value':'min'},
				           {'label':'Maximum', 'value':'max'},
				           {'label':'Mode', 'value':'mode'}],
				  value='mean',
				  style={'text-align': 'left'}
				  )
		      ], style={'width':'30%','display': 'inline-block',
			            'vertical-align': 'middle'}),
	dcc.Graph(id='vis-bar')
	], style={'text-align': 'center'}) # Close Div

# Tab 2 (Scatter Plot) Layout
tab2_layout = html.Div([
	html.Br(),
	html.Div([html.P('Select X-axis:',style={'text-align': 'left'}),
			  dcc.RadioItems(
				  id='scatter-radio-xaxis',
				  options=[{'label':'Age', 'value':'Age'},
				  		   {'label':'Annual Income', 'value':'AnnualIncome'},
					       {'label':'Spending Score', 'value':'SpendingScore'}],
				  value='Age',
				  labelStyle={'display':'block', 'text-align': 'left'})
			    ], style={'width':'20%','display': 'inline-block',
				      'vertical-align': 'middle'}), # 1st Option
	html.Div([html.P('Select Y-axis:',style={'text-align': 'left'}),
			  dcc.RadioItems(
				  id='scatter-radio-yaxis',
				  options=[{'label':'Age', 'value':'Age'},
				  		   {'label':'Annual Income', 'value':'AnnualIncome'},
					       {'label':'Spending Score', 'value':'SpendingScore'}],
				  value='AnnualIncome',
				  labelStyle={'display':'block', 'text-align': 'left'})
			    ], style={'width':'20%','display': 'inline-block',
				      'vertical-align': 'middle'}), # 2nd Option
	dcc.Graph(id='vis-scatter')
	], style={'text-align': 'center'}) # Close Div

# Tab 3 (Box Plot Layout)
tab3_layout = html.Div([
	html.Br(),
	html.Div([html.P('Select X-axis:',style={'text-align': 'left'}),
			  dcc.RadioItems(
				  id='box-radio-xaxis',
				  options=[{'label':'Age', 'value':'Age'},
				  		   {'label':'Annual Income', 'value':'AnnualIncome'},
					       {'label':'Gender', 'value':'Gender'},
					       {'label':'Spending Score', 'value':'score'}],
				  value='Age',
				  labelStyle={'display':'block', 'text-align': 'left'})
			    ], style={'width':'20%','display': 'inline-block',
				      'vertical-align': 'middle'}), # 1st Option
	html.Div([html.P('Select Y-axis:',style={'text-align': 'left'}),
			  dcc.RadioItems(
				  id='box-radio-yaxis',
				  options=[{'label':'Age', 'value':'Age'},
				  		   {'label':'Annual Income', 'value':'AnnualIncome'},
					       {'label':'Gender', 'value':'Gender'},
					       {'label':'Spending Score', 'value':'SpendingScore'}],
				  value='AnnualIncome',
				  labelStyle={'display':'block', 'text-align': 'left'})
			    ], style={'width':'20%','display': 'inline-block',
				      'vertical-align': 'middle'}), # 2nd Option
	dcc.Graph(id='vis-box')
	], style={'text-align': 'center'}) # Close Div
