import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from flask import Flask
from gevent.pywsgi import WSGIServer
import pandas as pd
from math import floor, ceil, exp
from initialise_parameters import params, parameter_csv, example_population_frame, preparePopulationFrame, control_data
import numpy as np
import plotly.graph_objects as go
import copy
from functions import simulator
import flask
import datetime
import json
from plotter import categories, figure_generator, age_structure_plot, stacked_bar_plot
########################################################################################################################


# for now, have stopped updating since likely to use another front end














# print(example_population_frame)
# external_stylesheets = 'https://codepen.io/chriddyp/pen/bWLwgP.css'
tab_label_color = 'black' # "#00AEF9"
external_stylesheets = dbc.themes.SPACELAB

app = dash.Dash(__name__, external_stylesheets=[external_stylesheets])

server = app.server

app.config.suppress_callback_exceptions = True
########################################################################################################################
# setup

df = copy.deepcopy(example_population_frame)
df = df.loc[:,'Age':'Population']
df2 = df.loc[:,['Hosp_given_symptomatic','Critical_given_hospitalised']].astype(str) + '%'
df = pd.concat([df.loc[:,'Age'],df2],axis=1)
df = df.rename(columns={"Hosp_given_symptomatic": "Hospitalised", "p_critical": "Requiring Critical Care"})

def generate_table(dataframe, max_rows=10):
    return dbc.Table.from_dataframe(df, striped=True, bordered = True, hover=True)


# dummy_figure = {'data': [], 'layout': {'template': 'simple_white'}}

bar_height = '100'
bar_width  =  '100'

bar_non_crit_style = {'height': bar_height, 'width': bar_width, 'display': 'block' }




camps = {'Camp_1': 'Name of Camp 1',
        'Camp_2': 'Name of Camp 2'
        }














########################################################################################################################




























layout_inter = html.Div([
    dbc.Row([
        # column_1,
        



                        html.Div([
                        dbc.Row([
                        dbc.Col([
                        html.Div([


                                    # store results
                                    dcc.Store(id='sol-calculated'),
                                    dcc.Store(id='conf-calculated'),
                                    dcc.Store(id='sol-calculated-do-nothing'),
            
                                    # dbc.Col([

                                    # dbc.Jumbotron([
                                    # tabs
                                    dbc.Tabs(id="interactive-tabs", active_tab='tab_0', 
                                        children=[

                                        # tab 0
                                        dbc.Tab(label='Model Output',
                                         label_style={"color": tab_label_color, 'fontSize':'120%'},
                                         tab_id='tab_0',
                                         tab_style = {'minWidth':'50%','textAlign': 'center', 'cursor': 'pointer'},
                                         children = [
                                                    # html.Div([



                                                    # Instructions_layout,

                                                    # html.Hr(),

                                                    html.H3('Strategy Outcome',id='line_page_title',className="display-4",style={'fontSize': '250%','textAlign': 'center', 'marginTop': '3vh', 'marginBottom': '1vh'}),

                                                    # html.Hr(),

                                                    dcc.Markdown('''
                                                    *In this Section we explore possible outcomes of different choices of **COVID-19 control**.*
                                                    
                                                    *Pick a **strategy** below.*

                                                    '''
                                                    ,style = {'marginTop': '3vh', 'marginBottom': '3vh', 'textAlign': 'center'}
                                                    ),
                                                    # 1. **Pick your strategy** (bar below)
                                                    
                                                    # 2. Choose which **results** to display (button below).
                                             
                                             
                                                    html.Hr(),

                                                    # html.Hr(),

                                                # dbc.Row([
            
                                                        # dbc.Col([
                                                            # dbc.Jumbotron([
                                                                



############################################################################################################################################################################################################################
                                                                                            # html.Div([

                                                                                                        ##################################

                                                                                                                        # form group 1
                                                                                                                        dbc.FormGroup([

                                                                                ########################################################################################################################

                                                                                                                                                    dbc.Col([
                                                                                                                                                            


                                                                                                                                                            


                                                                                ########################################################################################################################


                                                                                                                                                            
                                                                                                                                                dbc.Row([
                                                                                                                                                        dbc.Col([
                                                                                                                                                            
                                                                                                                                                            html.H3(['Pick Your Strategy ',
                                                                                                                                                            dbc.Button('🛈',
                                                                                                                                                            color='primary',
                                                                                                                                                            # className='mb-3',
                                                                                                                                                            id="popover-pick-strat-target",
                                                                                                                                                            size='md',
                                                                                                                                                            style = {'cursor': 'pointer', 'marginBottom': '0.5vh'}),
                                                                                                                                                            ],
                                                                                                                                                            className = 'display-4',
                                                                                                                                                            style={'fontSize': '230%', 'marginTop': "3vh", 'marginBottom': "3vh", 'textAlign': 'center'}),

                                                                                                                                                            


                                                                                                                                                            dbc.Popover(
                                                                                                                                                                [
                                                                                                                                                                dbc.PopoverHeader('Pick Your Strategy'),
                                                                                                                                                                dbc.PopoverBody(dcc.Markdown(
                                                                                                                                                                '''

                                                                                                                                                                1. Pick the camp.

                                                                                                                                                                2. Pick the **type of control**.

                                                                                                                                                                3. Pick the **control timings** (how long control is applied for and when it starts).


                                                                                                                                                                *The other options below are optional custom choices that you may choose to investigate further or ignore altogether*.

                                                                                                                                                                *Click the button to dismiss*.

                                                                                                                                                                '''
                                                                                                                                                                ),),
                                                                                                                                                                ],
                                                                                                                                                                id = "popover-pick-strat",
                                                                                                                                                                target="popover-pick-strat-target",
                                                                                                                                                                is_open=False,
                                                                                                                                                                placement='right',
                                                                                                                                                                ),

                                                                                                                                                  


                                                                                                                                                        dcc.Markdown('''*Choose the type of control and when to implement it.*''', style = {'fontSize': '85%' ,'textAlign': 'center', 'marginBottom': '3vh'}), # 'textAlign': 'left', fs 80%

                                                                                                                                                        
                                                                                                                                                    dbc.Row([


                                                                                                                                                           



                                                                                                                                                            dbc.Col([ 
                                                                                                                                                                
                                                                                                                                                                
                                                                                                                                                            html.H6([
                                                                                                                                                            '1. Choice of Camp ',
                                                                                                                                                            
                                                                                                                                                            ],
                                                                                                                                                            style={'fontSize': '100%', 'marginTop': '1vh', 'marginBottom': '1vh','textAlign': 'center'}),

                                                                                                                                                                


                                                                                                                                                                              
                                                                                                                                                            html.Div([
                                                                                                                                                            dcc.Dropdown(
                                                                                                                                                                id = 'camps',
                                                                                                                                                                options=[{'label': camps[key],
                                                                                                                                                                'value': key} for key in camps],
                                                                                                                                                                value= 'Camp_2',
                                                                                                                                                                clearable = False,
                                                                                                                                                                # disabled=True
                                                                                                                                                            ),],
                                                                                                                                                            style={'cursor': 'pointer', 'textAlign': 'center'}),

                                                                                                                                                            html.H6([
                                                                                                                                                                '2. Control Type ',
                                                                                                                                                                dbc.Button('🛈',
                                                                                                                                                                    color='primary',
                                                                                                                                                                    # className='mb-3',
                                                                                                                                                                    size='sm',
                                                                                                                                                                    id='popover-control-target',
                                                                                                                                                                    style={'cursor': 'pointer','marginBottom': '0.5vh', 'textAlign': 'center'}
                                                                                                                                                                    ),
                                                                                                                                                                ],
                                                                                                                                                                style={'fontSize': '100%', 'marginTop': '1vh', 'marginBottom': '1vh','textAlign': 'center'}),


                                                                                                                                                            dbc.Popover(
                                                                                                                                                                [
                                                                                                                                                                dbc.PopoverHeader('Control'),
                                                                                                                                                                dbc.PopoverBody(dcc.Markdown(
                                                                                                                                                                '''

                                                                                                                                                                The type of **control** determines how much we can reduce the **infection rate** of the disease (how quickly the disease is transmitted between people).
                                                                                                                                                                
                                                                                                                                                                '''
                                                                                                                                                                ),),
                                                                                                                                                                ],
                                                                                                                                                                id = "popover-control",
                                                                                                                                                                is_open=False,
                                                                                                                                                                target="popover-control-target",
                                                                                                                                                                placement='right',
                                                                                                                                                                ),

                                                                                                                                                                              
                                                                                                                                                            html.Div([
                                                                                                                                                            dcc.Dropdown(
                                                                                                                                                                id = 'preset',
                                                                                                                                                                options=[{'label': control_data.Name[i],
                                                                                                                                                                'value': i} for i in range(len(control_data.Name))],
                                                                                                                                                                value= 0,
                                                                                                                                                                clearable = False,
                                                                                                                                                                # disabled=True
                                                                                                                                                            ),],
                                                                                                                                                            style={'cursor': 'pointer', 'textAlign': 'center'}),




                                                                                                                                                                html.H6([
                                                                                                                                                                '3. Control Timings ',
                                                                                                                                                                dbc.Button('🛈',
                                                                                                                                                                color='primary',
                                                                                                                                                                size='sm',
                                                                                                                                                                id='popover-months-control-target',
                                                                                                                                                                style= {'cursor': 'pointer','marginBottom': '0.5vh'}),
                                                                                                                                                                ],
                                                                                                                                                                style={'fontSize': '100%','marginTop': '1vh', 'marginBottom': '1vh','textAlign': 'center'}),


                                                                                                                                                            
                                                                                                                                                                html.Div([
                                                                                                                                                                dcc.RangeSlider(
                                                                                                                                                                            id='day-slider',
                                                                                                                                                                            min=0,
                                                                                                                                                                            max=200,
                                                                                                                                                                            step=1,
                                                                                                                                                                            # disabled=True,
                                                                                                                                                                            # pushable=0,
                                                                                                                                                                            marks={i: 'Day '+ str(i) if i ==0 else str(i) for i in range(0,201,10)},
                                                                                                                                                                            value=[10,100],
                                                                                                                                                                ),
                                                                                                                                                                ],
                                                                                                                                                                # style={'fontSize': '180%'},
                                                                                                                                                                ),


                                                                                                                                                            dbc.Popover(
                                                                                                                                                                [
                                                                                                                                                                dbc.PopoverHeader('Control Timing'),
                                                                                                                                                                dbc.PopoverBody(dcc.Markdown(
                                                                                                                                                                '''

                                                                                                                                                                Use this slider to determine when control **starts** and **finishes**.

                                                                                                                                                                When control is in place the infection rate is reduced by an amount depending on the strategy choice.

                                                                                                                                                                When control is not in place the infection rate returns to the baseline level.
                                                                                                                                                                
                                                                                                                                                                '''
                                                                                                                                                                ),),
                                                                                                                                                                ],
                                                                                                                                                                id = "popover-months-control",
                                                                                                                                                                is_open=False,
                                                                                                                                                                target="popover-months-control-target",
                                                                                                                                                                placement='right',
                                                                                                                                                            ),

                                                                                                                                                            html.Hr(),

                                                                                                                                                            dbc.Row(
                                                                                                                                                                dbc.Button('Calculate',
                                                                                                                                                                color='primary',
                                                                                                                                                                size='lg',
                                                                                                                                                                id='calc-button',
                                                                                                                                                                style= {'cursor': 'pointer','marginBottom': '0.5vh'}),
                                                                                                                                                            justify =  'center'
                                                                                                                                                            ),







                                                                                                                                                            
                                                                                                                                                        #     ],
                                                                                                                                                        #     width=6,
                                                                                                                                                        #     ),



                                                                                                                                                        # dbc.Col([






                                                                                                                                                            






                                                                                                                                                        ],width=12),

                                                                                                                                                    ]),




                                                                                                                                                    # ]),





                                                                                                                                                        ],width=True),
                                                                                                                                                        #end of PYS row
                                                                                                                                                    ]),

                                                                                                                                                                    
                                                                                                                                                        # html.Hr(),
                                                                                        ###################################

                                                                                                
                                                                                                
                                                                                                
                                                                                                


                                                                                #########################################################################################################################################################


                                                                                                                                                    ],
                                                                                                                                                    width = True
                                                                                                                                                    ),

                                                                                                                                                    
                                                                                ########################################################################################################################

                                                                                                                        # end of form group 1
                                                                                                                        ],
                                                                                                                        row=True
                                                                                                                        ),
                                                                                ########################################################################################################################









############################################################################################################################################################################################################################    

                                                    html.Hr(),
                                    ##############################################################################################################################################################################################################################
                                            # start of results col
                                                    # html.Div('hello?'),

                                                    html.Div([
                                             


                                                        dbc.Row([


                                                                html.H3('Results',
                                                                className='display-4',
                                                                style={'fontSize': '250%', 'textAlign': 'center' ,'marginTop': "1vh",'marginBottom': "1vh"}),
                                                                
                                                                dbc.Spinner(html.Div(id="loading-sol-1"),color='primary'), # not working??

                                                                ],
                                                                justify='center',
                                                                style = {'marginTop': '3vh', 'marginBottom': '3vh'}
                                                        ),
                                                        
                                             
                                                      

                                             

                                                                                        

                                                                
                                                                
                                                    html.Div(id='DPC-content',children=[
                                                                
                                                                
                                                                dbc.Row(
                                                                    html.H4("All Outputs",
                                                                    style={'marginBottom': '1vh', 'textAlign': 'center' ,'marginTop': '4vh','fontSize': '180%'}),
                                                                justify =  'center'
                                                                ),

                                                                
                                                                dcc.Graph(id='line-plot-1',style={'height': '70vh', 'width': '100%'}),


                                                                        dbc.Row([
                                                                            dbc.Col([


                                                                                dbc.Row(
                                                                                    html.H4("Plot Settings ",
                                                                                    style={'marginBottom': '1vh', 'textAlign': 'center' ,'marginTop': '4vh','fontSize': '180%'}),
                                                                                    
                                                                                justify =  'center'
                                                                                ),

                                                                                dbc.Col([
                                                                                dcc.Markdown('''*Plot different disease progress categories, different risk groups, compare the outcome of your strategy with the outcome of 'Do Nothing', or plot the ICU capacity.*''', 
                                                                                style = {'textAlign': 'center', 'fontSize': '85%','marginBottom': '1vh' , 'marginTop': '1vh'}),
                                                                                ],width={'size':8, 'offset': 2}),

                            
                                                                                                            dbc.Row([
                                                                                                                                        dbc.Col([


                                                                                                                                                html.H6('Categories To Plot',style={'fontSize': '100%','textAlign': 'center'}),
                                                                                                                                                dbc.Col([


                                                                                                                                                    dbc.Checklist(id='categories-to-plot-checklist-1',
                                                                                                                                                                    options=[
                                                                                                                                                                        {'label': categories[key]['longname'], 'value': key} for key in categories
                                                                                                                                                                    ],
                                                                                                                                                                    value= ['S','E','I','R','H','C','D'],
                                                                                                                                                                    labelStyle = {'display': 'inline-block','fontSize': '80%'},
                                                                                                                                                                ),
                                                                                                                                                    
                                                                                                                                                    dcc.Markdown('''
                                                                                                                                                        *Category choice is for the plot above. Hospital categories are shown in the plot below.*
                                                                                                                                                        ''',style={'fontSize': '75%', 'textAlign': 'justify', 'marginTop': '0vh'}),
                                                                                                                                                        

                                                                                                                                                ],width={'size':6 , 'offset': 3}),

                                                                                                                                        ],width=6),







                                                                                                                                        dbc.Col([


                                                                                                                                                        html.H6("Compare with 'Do Nothing'",style={'fontSize': '100%','textAlign': 'center'}),

                                                                                                                                                        dbc.Col([


                                                                                                                                                            dbc.Checklist(
                                                                                                                                                                id = 'plot-with-do-nothing',
                                                                                                                                                                options=[
                                                                                                                                                                    {'label': 'Compare', 'value': 1, 'disabled': True},
                                                                                                                                                                ],
                                                                                                                                                                value= 0,
                                                                                                                                                                labelStyle = {'display': 'inline-block','fontSize': '80%'},
                                                                                                                                                            ),

                                                                                                                                                        ],width={'size':6 , 'offset': 3}),

                                                                                                                                                        html.H6("Plot Intensive Care Capacity",style={'fontSize': '100%','textAlign': 'center', 'marginTop': '2vh'}),


                                                                                                                                                        dbc.Col([
                                                                                                                                                            dbc.Checklist(
                                                                                                                                                                id = 'plot-ICU-cap',
                                                                                                                                                                options=[
                                                                                                                                                                    {'label': 'Plot', 'value': 1, 'disabled': True},
                                                                                                                                                                ],
                                                                                                                                                                value= 0,
                                                                                                                                                                labelStyle = {'display': 'inline-block','fontSize': '80%'},
                                                                                                                                                            ),

                                                                                                                                                        ],width={'size':6 , 'offset': 3}
                                                                                                                                                        ,style={'marginBottom': '0vh'}
                                                                                                                                                        ),
                                                                                                                                                        dcc.Markdown('''
                                                                                                                                                        *ICU capacity will only be clear on small y-scales (hospital categories only), or logarithmic scales. For the classic 'flatten the curve' picture, check this box and then select 'Critical' and no others in the '**Categories To Plot**' checklist.*
                                                                                                                                                        ''',style={'fontSize': '75%', 'textAlign': 'justify', 'marginTop': '0vh'}),


                                                                                                                                        ],width=6),


                                                                                                                                                                        

                                                                                                                        ],
                                                                                                                        id='outputs-div',
                                                                                                                        no_gutters=True,
                                                                                                                        # justify='center'
                                                                                                                        ),
                                                                                                                        
                                                                                                                        # html.Hr(),
                                                                                        # ],
                                                                                        # id="collapse-plots",
                                                                                        # is_open=False,
                                                                                        # ),

                                                                                ],
                                                                                width=12,
                                                                                ),


                                                                                # end of plot settings row
                                                                                ],
                                                                                justify='center',
                                                                                no_gutters=True
                                                                                # style={'textAlign': 'center'}
                                                                                ),

                                                                # html.Hr(style={'marginTop': '3vh'}),

                                                                dcc.Markdown('''
                                                                            Each line displays the number of people in that category at each time point. Two of the categories are cumulative, since once you recover, or you die, you remain in that category. The time for which control is in place is shown in light blue. This may be adjusted using the '**Pick Your Strategy** sliders above. The time for which the intensive care capacity is exceeded is shown in pink. The extent to which healthcare capacity is increased is a strategy choice under '**Custom Options**'.

                                                                            You may choose to adjust the graph axes. Choosing a logarithmic scale for the *y* axis makes it easier to compare the different quantities and their rates of growth or decay. However a linear scale makes it easiest to draw comparisons between the relative sizes of the categories.

                                                                            An interesting way to compare the strategies is their effectiveness relative to 'do nothing'; that is, relative to no control measure at all. To see this, select the '*Compare with Do Nothing*' checkbox in '**Plot Settings**'.

                                                                            ''',style={'fontSize': '100%', 'textAlign': 'justify', 'marginTop': '6vh', 'marginBottom': '3vh'}),

 
 
                                                                html.Hr(),

 
                                                                 dbc.Row([
                                                                 dbc.Col([

                                                                        html.H6('Categories To Plot (Next 3 plots)',style={'fontSize': '100%','textAlign': 'center'}),
                                                                        dbc.Col([


                                                                            dbc.RadioItems(id='categories-to-plot-checklist-2',
                                                                                            options=[
                                                                                                {'label': categories[key]['longname'], 'value': key} for key in categories
                                                                                            ],
                                                                                            value= 'H',
                                                                                            inline=True,
                                                                                            labelStyle = {'display': 'inline-block','fontSize': '80%'},
                                                                                        ),
                                                                            
                                                                            dcc.Markdown('''
                                                                                *Category choice is for the plot above. Hospital categories are shown in the plot below.*
                                                                                ''',style={'fontSize': '75%', 'textAlign': 'justify', 'marginTop': '0vh'}),
                                                                                

                                                                        ],width={'size':8 , 'offset': 2}),

                                                                ],width=True),
                                                                ],justify=True),

                                                                dbc.Row(
                                                                    html.H4("Uncertainty in R0",
                                                                    style={'marginBottom': '1vh', 'textAlign': 'center' ,'marginTop': '4vh','fontSize': '180%'}),
                                                                justify =  'center'
                                                                ),
 
                                                                dcc.Graph(id='line-plot-uncertainty',style={'height': '70vh', 'width': '100%'}),
 
                                                                html.Hr(),

                                                                dbc.Row(
                                                                    html.H4("Age Structure",
                                                                    style={'marginBottom': '1vh', 'textAlign': 'center' ,'marginTop': '4vh','fontSize': '180%'}),
                                                                justify =  'center'
                                                                ),


                                                                dcc.Graph(id='line-plot-2',style={'height': '70vh', 'width': '100%'}),




                                                                html.Hr(),

                                                                dbc.Row(
                                                                    html.H4("Age Structure",
                                                                    style={'marginBottom': '1vh', 'textAlign': 'center' ,'marginTop': '4vh','fontSize': '180%'}),
                                                                justify =  'center'
                                                                ),

                                                                dcc.Graph(id='line-plot-3',style={'height': '70vh', 'width': '100%'}),


                                                                #  dbc.Row([
                                                                #  dbc.Col([

                                                                #         html.H6('Categories To Plot',style={'fontSize': '100%','textAlign': 'center'}),
                                                                #         dbc.Col([


                                                                #             dbc.RadioItems(id='categories-to-plot-checklist-3',
                                                                #                             options=[
                                                                #                                 {'label': categories[key]['longname'], 'value': key} for key in categories
                                                                #                             ],
                                                                #                             value= 'H',
                                                                #                             inline=True,
                                                                #                             labelStyle = {'display': 'inline-block','fontSize': '80%'},
                                                                #                         ),
                                                                            
                                                                #             dcc.Markdown('''
                                                                #                 *Category choice is for the plot above. Hospital categories are shown in the plot below.*
                                                                #                 ''',style={'fontSize': '75%', 'textAlign': 'justify', 'marginTop': '0vh'}),
                                                                                

                                                                #         ],width={'size':8 , 'offset': 2}),

                                                                # ],width=True),
                                                                # ],justify=True),


                                                                html.Hr(),


                                                                html.H6([
                                                                    'Results Type ',
                                                                    dbc.Button('🛈',
                                                                        color='primary',
                                                                        # className='mb-3',
                                                                        size='sm',
                                                                        id='popover-res-type-target',
                                                                        style={'cursor': 'pointer','marginBottom': '0.5vh'}
                                                                        ),
                                                                    ],
                                                                    style={'fontSize': '100%', 'marginTop': '1vh', 'marginBottom': '1vh','textAlign': 'center'}),

                                                                    
                                                                html.Div([
                                                                dcc.Dropdown(
                                                                    id = 'dropdown',
                                                                    options=[{'label': 'Disease Progress Curves','value': 'DPC_dd'},
                                                                    {'label': 'Bar Charts','value': 'BC_dd'},
                                                                    {'label': 'Strategy Overview','value': 'SO_dd'},
                                                                    ],
                                                                    value= 'DPC_dd',
                                                                    clearable = False,
                                                                    disabled=True
                                                                ),],
                                                                style={'cursor': 'pointer'}),


                                                                dbc.Popover(
                                                                        [
                                                                        dbc.PopoverHeader('Results'),
                                                                        dbc.PopoverBody(dcc.Markdown(
                                                                        '''

                                                                        Choose between disease progress curves, bar charts and strategy overviews to explore the outcome of your strategy choice.

                                                                        '''
                                                                        ),),
                                                                        ],
                                                                        id = "popover-res-type",
                                                                        is_open=False,
                                                                        target="popover-res-type-target",
                                                                        placement='left',
                                                                    ),











                                                    ]
                                                    ),
                                             
                                                    
                                                    
                                                ]),


# end of results col
#########################################################################################################################################################











                                                    
                                             


                                         ],
                                         
                                         ),
#########################################################################################################################################################
                                                                                                                dbc.Tab(label='Model Explanation', label_style={"color": tab_label_color, 'fontSize':'120%'}, tab_id='model_s',
                                                                                                                tab_style = {'minWidth':'50%','textAlign': 'center', 'cursor': 'pointer'},
                                                                                                                children=[
                                                                                                        
                                                                                                                                                html.Div([
                                                                                                                                                                # dbc.Col([

                                                                                                                                                                    html.H3('Model Explanation',
                                                                                                                                                                    className = 'display-4',
                                                                                                                                                                    style = {'marginTop': '1vh', 'marginBottom': '1vh', 'textAlign': 'center', 'fontSize': '250%'}),

                                                                                                                                                                    html.Hr(),
                                                                                                                                                                    dcc.Markdown(
                                                                                                                                                                    '''
                                                                                                                                                                    *Underlying all of the predictions is a mathematical model. In this Section we explain how the mathematical model works.*

                                                                                                                                                                    We present a compartmental model for COVID-19, split by risk categories. That is to say that everyone in the population is **categorised** based on **disease status** (susceptible/ infected/ recovered/ hospitalised/ critical care/ dead) and based on **COVID risk**.
                                                                                                                                                                    
                                                                                                                                                                    The model is very simplistic but still captures the basic spread mechanism. It is far simpler than the [**Imperial College model**](https://spiral.imperial.ac.uk/handle/10044/1/77482), but it uses similar parameter values and can capture much of the relevant information in terms of how effective control will be.

                                                                                                                                                                    It is intended solely as an illustrative, rather than predictive, tool. We plan to increase the sophistication of the model and to update parameters as more (and better) data become available to us.
                                                                                                                                                                    
                                                                                                                                                                    We have **two risk categories**: high and low. **Susceptible** people get **infected** after contact with an infected person (from either risk category). A fraction of infected people (*h*) are **hospitalised** and the rest **recover**. Of these hospitalised cases, a fraction (*c*) require **critical care** and the rest recover. Of those in critical care, a fraction (*d*) **die** and the rest recover.

                                                                                                                                                                    The recovery fractions depend on which risk category the individual is in.
                                                                                                                                                                

                                                                                                                                                                    ''',
                                                                                                                                                                    style = {'textAlign': 'justify'}

                                                                                                                                                                    ),



                                                                                                                                                                    dbc.Row([
                                                                                                                                                                    html.Img(src='https://res.cloudinary.com/hefjzc2gb/image/upload/v1585831217/Capture_lomery.png',
                                                                                                                                                                    style={'maxWidth':'90%','height': 'auto', 'display': 'block','marginTop': '1vh','marginBottom': '1vh'}
                                                                                                                                                                    ),
                                                                                                                                                                    ],
                                                                                                                                                                    justify='center'
                                                                                                                                                                    ),

                                                                                                                                                                    dcc.Markdown('''

                                                                                                                                                                    The selection of risk categories is done in the crudest way possible - an age split at 60 years (based on the age structure data below). A more nuanced split would give a more effective control result, since there are older people who are at low risk and younger people who are at high risk. In many cases, these people will have a good idea of which risk category they belong to.

                                                                                                                                                                    *For the more mathematically inclined reader, a translation of the above into a mathematical system is described below.*

                                                                                                                                                                    ''',style={'textAlign': 'justify','marginTop' : '2vh','marginBottom' : '2vh'}),
                                                                                                                                                                    
                                                                                                                                                                    

                                                                                                                                                                    dbc.Row([
                                                                                                                                                                    html.Img(src='https://res.cloudinary.com/hefjzc2gb/image/upload/v1585831217/eqs_f3esyu.png',
                                                                                                                                                                    style={'maxWidth':'90%','height': 'auto','display': 'block','marginTop': '1vh','marginBottom': '1vh'})
                                                                                                                                                                    ],
                                                                                                                                                                    justify='center'
                                                                                                                                                                    ),


                                                                                                                                                                    dbc.Row([
                                                                                                                                                                    html.Img(src='https://res.cloudinary.com/hefjzc2gb/image/upload/v1585831217/text_toshav.png',
                                                                                                                                                                    style={'maxWidth':'90%','height': 'auto','display': 'block','marginTop': '1vh','marginBottom': '1vh'}
                                                                                                                                                                    ),
                                                                                                                                                                    ],
                                                                                                                                                                    justify='center'
                                                                                                                                                                    ),

                                                                                                                                                                    
                                                                                                                                                                    dcc.Markdown('''
                                                                                                                                                                    Of those requiring critical care, we assume that if they get treatment, a fraction *1-d* recover. If they do not receive it they die, taking 2 days. The number able to get treatment must be lower than the number of ICU beds available.
                                                                                                                                                                    ''',
                                                                                                                                                                    style={'textAlign': 'justify'}),



                                                                                                                                                                    html.Hr(),

                                                                                                                                                                    html.H4('Parameter Values',style={'fontSize': '180%', 'textAlign': 'center'}),

                                                                                                                                                                    dcc.Markdown('''
                                                                                                                                                                    The model uses a weighted average across the age classes below and above 60 to calculate the probability of a member of each class getting hospitalised or needing critical care. Our initial conditions are updated to match new data every day (meaning the model output is updated every day, although in '**Custom Options**' there is the choice to start from any given day).

                                                                                                                                                                    We assume a 10 day delay on hospitalisations, so we use the number infected 10 days ago to inform the number hospitalised (0.044 of infected) and in critical care (0.3 of hospitalised). We calculate the approximate number recovered based on the number dead, assuming that 0.009 infections cause death. All these estimates are as per the Imperial College paper ([**Ferguson et al**](https://spiral.imperial.ac.uk/handle/10044/1/77482)).

                                                                                                                                                                    The number of people infected, hospitalised and in critical care are calculated from the recorded data. We assume that only half the infections are reported ([**Fraser et al.**](https://science.sciencemag.org/content/early/2020/03/30/science.abb6936)), so we double the recorded number of current infections. The estimates for the initial conditions are then distributed amongst the risk groups. These proportions are calculated using conditional probability, according to risk (so that the initial number of infections is split proportionally by size of the risk categories, whereas the initially proportion of high risk deaths is much higher than low risk deaths).

                                                                                                                                                                    ''',
                                                                                                                                                                    style={'textAlign': 'justify'}),



                                                                                                                                                                    

                                                                                                                                                                    dbc.Row([
                                                                                                                                                                    html.Img(src='https://res.cloudinary.com/hefjzc2gb/image/upload/v1586345773/table_fhy8sf.png',
                                                                                                                                                                    style={'maxWidth':'90%','height': 'auto','display': 'block','marginTop': '1vh','marginBottom': '1vh'}
                                                                                                                                                                    ),
                                                                                                                                                                    ],
                                                                                                                                                                    justify='center'
                                                                                                                                                                    ),



                                                                                                                                                                    html.P('** the Imperial paper uses 8 days in hospital if critical care is not required (as do we). It uses 16 days (with 10 in ICU) if critical care is required. Instead, if critical care is required we use 8 days in hospital (non-ICU) and then either recovery or a further 8 in intensive care (leading to either recovery or death).',
                                                                                                                                                                    style={'fontSize':'85%'}),

                                                                                                                                                                    dcc.Markdown('''
                                                                                                                                                                    Please use the following links: [**Ferguson et al**](https://spiral.imperial.ac.uk/handle/10044/1/77482), [**Anderson et al**](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(20)30567-5/fulltext) and [**Zhao et al**](https://journals.plos.org/plosntds/article/file?rev=2&id=10.1371/journal.pntd.0006158&type=printable)
                                                                                                                                                                    ''',
                                                                                                                                                                    style={'textAlign': 'justify'}),


                                                                                                                                                                    html.H4('Age Structure',style={'fontSize': '180%', 'textAlign': 'center'}),
                                                                                                                                                                    
                                                                                                                                                                    dcc.Markdown('''
                                                                                                                                                                    The age data is taken from [**GOV.UK**](https://www.ethnicity-facts-figures.service.gov.uk/uk-population-by-ethnicity/demographics/age-groups/latest) and the hospitalisation and critical care data is from the [**Imperial College Paper**](https://spiral.imperial.ac.uk/handle/10044/1/77482) (Ferguson et al.). This means that the age structure will not be accurate when modelling other countries.

                                                                                                                                                                    To find the probability of a low risk case getting hospitalised (or subsequently put in critical care), we take a weighted average by proportion of population. Note that the figures below are proportion of *symptomatic* cases that are hospitalised, which we estimate to be 55% of cases ([**Ferguson et al.**](https://spiral.imperial.ac.uk/handle/10044/1/77482)). The number requiring critical care is a proportion of this hospitalised number.

                                                                                                                                                                    *The table below shows the age structure data that was used to calculate these weighted averages across the low risk category (under 60) and high risk (over 60) category.*
                                                                                                                                                                    
                                                                                                                                                                    ''',
                                                                                                                                                                    style={'textAlign': 'justify','marginTop': '2vh','marginBottom': '2vh'}
                                                                                                                                                                    
                                                                                                                                                                    ),

                                                                                                                                                                    generate_table(df),








                                                                                                                                            ],style={'fontSize': '100%'})
                                                                                                                        ]),

                                                                                                ]),


                                        

                        ],
                        style= {'width': '90%', 'marginLeft': '5vw', 'marginRight': '5vw', 'marginTop': '10vh', 'marginBottom': '5vh'}
                        ),

                    
                        ],
                        width=12,
                        xl=10),
                        
                        ],
                        justify='center'
                        )





                        ],
                        style= {'width': '90%', 'backgroundColor': '#f4f6f7', 'marginLeft': '5vw', 'marginRight': '5vw', 'marginBottom': '5vh'}
                        ),



########################################################################################################################
        # end of row 1
########################################################################################################################


    ],
    # no_gutters=True,
    justify='center'
    )],
    style={'fontSize' : '1.9vh'},
    id='main-page-id'
    )


















        
page_layout = html.Div([
    
            
            dbc.Row([
                dbc.Col([
                    html.H3(children='Controlling COVID-19 in a refugee setting',
                    className="display-4",
                    style={'marginTop': '1vh', 'textAlign': 'center','fontSize': '340%'}
                    ),



                    html.P([
                    html.Span('Disclaimer: ',style={'color': '#C37C10'}), # orange
                    'This work is for educational purposes only and not for accurate prediction of the pandemic.'],
                    style = {'marginTop': '0vh','marginBottom': '0vh', 'fontSize': '110%', 'color': '#446E9B', 'fontWeight': 'bold'}
                    ),
                    html.P(
                    'There are many uncertainties in the COVID debate. The model is intended solely as an illustrative rather than predictive tool.',
                    style = {'marginTop': '0vh','marginBottom': '2.5vh', 'fontSize': '110%', 'color': '#446E9B', 'fontWeight': 'bold'}
                    ), # 

                ],width=True,
                style={'textAlign': 'center'}
                ),
            ],
            align="center",
            style={'backgroundColor': '#e9ecef'}
            ),

        layout_inter,

        # # page content
        # dcc.Location(id='url', refresh=False),

        html.Footer('This page is intended for illustrative/educational purposes only, and not for accurate prediction of the pandemic.',
                    style={'textAlign': 'center', 'fontSize': '100%', 'marginBottom': '1.5vh' , 'color': '#446E9B', 'fontWeight': 'bold'}),
        html.Footer([
                    "Authors: ",
                     html.A('Nick P. Taylor', href='https://twitter.com/TaylorNickP'),", ",
                     ],
        style={'textAlign': 'center', 'fontSize': '90%'}),
        html.Footer([
                     html.A('Source code', href='https://github.com/nt409/covid-19'), ". ",
                     "Data is taken from ",
                     html.A("Worldometer", href='https://www.worldometers.info/coronavirus/'), " if available or otherwise ",
                     html.A("Johns Hopkins University (JHU) CSSE", href="https://github.com/ExpDev07/coronavirus-tracker-api"), "."
                    ],
                    style={'textAlign': 'center', 'fontSize': '90%'}),

        

        ],
        # 
        )
##
########################################################################################################################





app.layout = page_layout

app.title = 'Control of COVID-19 in refugee camps'





########################################################################################################################
# callbacks




########################################################################################################################
# collapse
def toggle(n, is_open):
    if n:
        return not is_open
    return is_open


for p in ["custom"]:
    app.callback(
        Output(f"collapse-{p}", "is_open"),
        [Input(f"collapse-button-{p}", "n_clicks")
        ],
        [State(f"collapse-{p}", "is_open")],
    )(toggle)


########################################################################################################################
# popovers


for p in [ "pick-strat","control", "months-control", "res-type" , "cc-care" ,"custom-options", "inf-rate", "inf-tab", "cont-tab", "example","red-deaths","ICU","herd", 'cycles-off', 'cycles-on', 'groups-allowed']:
    app.callback(
        Output(f"popover-{p}", "is_open"),
        [Input(f"popover-{p}-target", "n_clicks")
        ],
        [State(f"popover-{p}", "is_open")],
    )(toggle)




##############################################################################################################################


@app.callback(
    [Output('sol-calculated', 'data'),
    Output('conf-calculated', 'data'),
    Output('loading-sol-1','children'),
    ],
    [
    Input('calc-button','n_clicks'),
    ],
    [
    State('preset', 'value'),
    State('day-slider', 'value'),
    State('camps', 'value'),
    ])
def find_sol(n_clicks,preset,timings,camp):
    if n_clicks is None:
        raise PreventUpdate
    
    t_stop = 200

    beta_factor = control_data.Value[preset]

    population_frame, population = preparePopulationFrame(camp)
    
    infection_matrix = np.ones((population_frame.shape[0],population_frame.shape[0]))
    beta_list = np.linspace(params.beta_list[0],params.beta_list[2],20)
    sols = []
    for beta in beta_list:
        sols.append(simulator().run_model(T_stop=t_stop,infection_matrix=infection_matrix,population=population,population_frame=population_frame,control_time=timings,beta=beta,beta_factor=beta_factor))

    n_time_points = len(sols[0]['t'])

    y_plot = np.zeros((len(categories.keys()), len(sols) , n_time_points ))

    for k, sol in enumerate(sols):
        for name in categories.keys():
            sol['y'] = np.asarray(sol['y'])

            y_plot[categories[name]['index'],k,:] = sol['y'][categories[name]['index'],:]
            for i in range(1, population_frame.shape[0]): # age_categories
                y_plot[categories[name]['index'],k,:] = y_plot[categories[name]['index'],k,:] + sol['y'][categories[name]['index'] + i*params.number_compartments,:]


    y_min = np.zeros((params.number_compartments,n_time_points))
    y_max = np.zeros((params.number_compartments,n_time_points))

    for name in categories.keys():
        y_min[categories[name]['index'],:] = [min(y_plot[categories[name]['index'],:,i]) for i in range(n_time_points)]
        y_max[categories[name]['index'],:] = [max(y_plot[categories[name]['index'],:,i]) for i in range(n_time_points)]

    # print(params.beta_list)
    
    sols_out = []
    sols_out.append(simulator().run_model(T_stop=t_stop,infection_matrix=infection_matrix,population=population,population_frame=population_frame,control_time=timings,beta=params.beta_list[1],beta_factor=beta_factor))
    
    return [sols_out, [y_min,y_max], None]



@app.callback(
    [
    Output('line-plot-1', 'figure'),
    Output('line-plot-uncertainty', 'figure'),
    Output('line-plot-2', 'figure'),
    Output('line-plot-3', 'figure'),
    ],
    [
    Input('sol-calculated', 'data'),
    Input('conf-calculated', 'data'),
    Input('categories-to-plot-checklist-1','value'),
    Input('categories-to-plot-checklist-2','value')],
    [
    State('preset', 'value'),
    State('day-slider', 'value'),
    State('camps', 'value'),
    ])
def plot_graphs(sols,conf,cats,cats2,preset,timings,camp):
    if sols is None:
        raise PreventUpdate

    population_frame, population = preparePopulationFrame(camp)

    preset = control_data.Name[preset]

    no_control = False
    if preset=='No control':
        no_control = True

    fig  = figure_generator(sols,cats,population,population_frame,timings,no_control) # ,sols[1:])
    fig_U  = figure_generator(sols,cats2,population,population_frame,timings,no_control,conf) # ,sols[1:])
    fig2 = age_structure_plot(sols,cats2,population,population_frame,timings,no_control)
    fig3 = stacked_bar_plot(sols,cats2,population,population_frame)

    return [fig, fig_U, fig2, fig3]







########################################################################################################################

if __name__ == '__main__':
    app.run_server(debug=True)










