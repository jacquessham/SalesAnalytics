import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from Layout import *



# Read file
carsales = pd.read_csv('../Data/Car_sales.csv')
# The dataset replace NA's with ., convert back to NA's
carsales = carsales.replace('.',np.nan)
# Engineer the data
# Fill the NA for Resales value
carsales['Resale_value_4yrs'] = carsales['Resale_value_4yrs'].fillna(0)
col_str = ['Manufacturer','Model','VehicleType','LatestLaunch']
col_num = ['Sales_k','Resale_value_4yrs','Price','EngineSize','Horsepower',
           'Wheelbase','Width','Length','CurbWeight','FuelCapacity',
           'FuelEfficiency']
carsales[col_num] = carsales[col_num].apply(pd.to_numeric)
# Other features does not make sense to have no data nor 0
carsales = carsales.dropna()
# Add features
carsales['ResalesRatio'] = carsales['Resale_value_4yrs']/carsales['Price']
carsales['Revenue'] = carsales['Sales_k']*carsales['Price']/1000

# Manipulate a data frame for car make and sales
make_sales = carsales[['Manufacturer','Sales_k']] \
                     .groupby('Manufacturer').sum().reset_index()
make_revenue = carsales[['Manufacturer','Revenue']] \
                       .groupby('Manufacturer').sum().reset_index()

# Manipulate a data frame to display feature correlation
carcorr = carsales.corr().reset_index()[['index','Sales_k']]
carcorr.columns = ['Features','Correlation']
carcorr['PosNeg'] = carcorr['Correlation'].apply(lambda x: 'Positive' if x > 0
                                                            else 'Negative')


# Dash Set up
app = dash.Dash()
# Dashboard Layout
app.layout = html.Div([
    html.H1(children=headline, style={'text-align':'center'}),
    # Position 0, headline
    dcc.Markdown(children=background),
    # Position 1, background
    html.Div([dcc.Markdown(text_sales_make0),
              dcc.Graph(figure = generate_barchart(make_sales, None,
                                'Manufacturer','Sales_k',
                                'Car Sales by Make','Make',
                                'Car Unit Sales (Thousand)', False)
                  ),
              dcc.Markdown(text_sales_make1)]),
    # Position 2, Bar chart of Sales by Make
    html.Div([dcc.Markdown(text_sales_model0),
              dcc.Graph(figure = generate_barchart(make_revenue, None,
                                'Manufacturer','Revenue',
                                'Revenue by Make','Make',
                                'Car Sales ($ Million)', False)
                  ),
              dcc.Markdown(text_sales_model1)]),
    # Position 3, Bar chart of Sales by Model
    html.Div([dcc.Markdown(text_histo_price0),
              dcc.Graph(figure=generate_histogram(carsales, 'Price',
                            'Histogram of Car Unit Price', 
                            'Car Unit Price ($k)', 'Count')),
              dcc.Markdown(text_histo_price1)],
              style={'width':'70%','margin':'auto'}),
    # Position 5, Histogram of Car Price
    html.Div([dcc.Markdown(text_histo_resales0),
              dcc.Graph(figure=generate_histogram(carsales, 'ResalesRatio',
                            'Histogram of Car Resales Ratio', 
                            'Resales Ratio', 'Count')),
              dcc.Markdown(text_histo_resales1)],
              style={'width':'70%','margin':'auto'}),
    # Position 6, Histogram of Resale Ratio
    html.Div([dcc.Markdown(text_scatter_price0),
    	      dcc.Graph(figure=generate_scatterplot(carsales, 
                              'Manufacturer','Price','Sales_k',
                              'Car Sales by Price','Price ($k)',
                              'Car Unit Sales (Thousand)', 
                              'linear','log')),
    	      dcc.Markdown(text_scatter_price1)]),
    # Position 7, Scatter Plot of Sales and Price
    html.Div([dcc.Markdown(text_scatter_resales0),
    	      dcc.Graph(figure=generate_scatterplot(carsales, 
                              'Manufacturer','ResalesRatio','Sales_k',
                              'Car Sales by Resales Ratio','ResalesRatio',
                              'Car Unit Sales (Thousand)')),
    	      dcc.Markdown(text_scatter_resales1)]),
    # Position 8, Scatter Plot of Sales and Resales Ratio
    html.Div([dcc.Markdown(text_scatter_hp0),
    	      dcc.Graph(figure=generate_scatterplot(carsales, 
                              'Manufacturer','Horsepower','Sales_k',
                              'Car Sales by Horsepower','Horsepower',
                              'Car Unit Sales (Thousand)')),
    	      dcc.Markdown(text_scatter_hp1)]),
    # Position 9, Scatter Plot of Sales and Horsepower
    html.Div([dcc.Markdown(text_scatter_mpg0),
    	      dcc.Graph(figure=generate_scatterplot(carsales, 
                              'Manufacturer','FuelEfficiency','Sales_k',
                              'Car Sales by Fuel Efficiency',
                              'Fuel Efficiency (MPG)',
                              'Car Unit Sales (Thousand)')),
    	      dcc.Markdown(text_scatter_mpg1)]),
    # Position 10, Scatter Plot of Sales and Fuel Efficiency
    html.Div([dcc.Markdown(text_histo_width0),
    	      dcc.Graph(figure=generate_histogram(carsales, 'Width',
                            'Histogram of Car Width', 
                            'Width (Inches)', 'Count')),
    	      dcc.Markdown(text_histo_width1)],
              style={'width':'70%','margin':'auto'}),
    # Position 11, Histogram of Width
    html.Div([dcc.Markdown(text_scatter_length0),
    	      dcc.Graph(figure=generate_scatterplot(carsales, 
                              'Manufacturer','Length','Sales_k',
                              'Car Sales by Car Length',
                              'Length (Inches)',
                              'Car Unit Sales (Thousand)')),
    	      dcc.Markdown(text_scatter_length1)]),
    # Position 12, Scatter Plot of Sales and Length
    html.Div([dcc.Markdown(text_bar_corr0),
              dcc.Graph(figure = generate_barchart(
              	                carcorr[(carcorr['Features']!='Revenue')], 
                                'PosNeg','Features','Correlation',
                                'Features Correlation with Car Sales',
                                'Features','Correlation', False)),
              dcc.Markdown(text_bar_corr1)]),
    # Position 13, Bar Chart for feature correlation
    html.Pre()
    # Position 14, Conclusion
    ])

if __name__ == '__main__':
    app.run_server(debug=True, port=1400)