#!/usr/bin/env python3

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import os

csv_url = 'https://raw.githubusercontent.com/youraunt/public/master/INWK2300/covid_19_Colorado_Daily.csv'
df = pd.read_csv(csv_url, parse_dates=['Date'])

app = dash.Dash()
server = app.server

tested_bar_graph = go.Bar(x=df['Date'], y=df['Tested'], marker_color='CornflowerBlue')
tested_scatter_graph = go.Scatter(x=df['Date'], y=df['Tested'], marker_color='darkSalmon')
new_cases_scatter_graph = go.Scatter(x=df['Date'], y=df['New Cases'], mode='lines+markers', marker_color='darkSalmon',
                                     line_color='CornflowerBlue')
new_deaths_graph = go.Scatter(x=df['Date'], y=df['New Deaths'], mode='lines+markers', marker_color='darkSalmon',
                              line_color='CornflowerBlue')
confirmed_bar_graph = go.Bar(x=df['Date'], y=df['Confirmed'], marker_color='CornflowerBlue')
confirmed_scatter_graph = go.Scatter(x=df['Date'], y=df['Confirmed'], marker_color='darkSalmon')
hospital_bar_graph = go.Bar(x=df['Date'], y=df['Hospitalized'], marker_color='CornflowerBlue')
hospital_scatter_graph = go.Scatter(x=df['Date'], y=df['Hospitalized'], marker_color='darkSalmon')
death_bar_graph = go.Bar(x=df['Date'], y=df['Death'], marker_color='CornflowerBlue')
death_scatter_graph = go.Scatter(x=df['Date'], y=df['Death'], marker_color='darkSalmon')

app.layout = html.Div(
    style={'backgroundColor': 'white'},
    children=[
        html.H1(
            children=
            'Graphing the the effects of COVID-19 in Colorado.',
            style={
                'textAlign': 'center',
                'color': 'black'
            }
        ),
        dcc.Graph(
            id='New_Deaths',
            figure={
                'data': [new_deaths_graph],
                'layout': {
                    'xaxis': {
                        'title': 'Date',
                        'showgrid': False
                    },
                    'yaxis': {
                        'title': 'Number of Individuals',
                        'showgrid': False
                    },
                    'title': 'New Deaths',
                    'font': {
                        'color': 'grey'
                    }
                }
            }
        ),
        dcc.Graph(
            id='New_Cases',
            figure={
                'data': [new_cases_scatter_graph],
                'layout': {
                    'xaxis': {
                        'title': 'Date',
                        'showgrid': False,
                        'rotation': 45
                    },
                    'yaxis': {
                        'title': 'Number of Individuals',
                        'showgrid': False
                    },
                    'title': 'New Cases',
                    'font': {
                        'color': 'grey'
                    }
                }
            }
        ),

        dcc.Graph(
            id='Tested_',
            figure={
                'data': [tested_scatter_graph],
                'layout': {
                    'xaxis': {
                        'title': 'Date',
                        'showgrid': False
                    },
                    'yaxis': {
                        'title': 'Number of Individuals',
                        'showgrid': False
                    },
                    'title': 'Tested',
                    'font': {
                        'color': 'grey'
                    }
                }
            }
        ),
        dcc.Graph(
            id='Tested',
            figure={
                'data': [tested_bar_graph],
                'layout': {
                    'xaxis': {
                        'title': 'Date',
                        'showgrid': False
                    },
                    'yaxis': {
                        'title': 'Number of Individuals',
                        'showgrid': False
                    },
                    'title': 'Tested',
                    'font': {
                        'color': 'grey'
                    }
                }
            }
        ),

        dcc.Graph(
            id='Graph_confirmed',
            figure={
                'data': [confirmed_scatter_graph],
                'layout': {
                    'xaxis': {
                        'title': 'Date',
                        'showgrid': False
                    },
                    'yaxis': {
                        'title': 'Number of Individuals',
                        'showgrid': False
                    },
                    'title': 'Confirmed',
                    'font': {
                        'color': 'grey'
                    }
                }
            }
        ),

        dcc.Graph(
            id='Graph_Test_confirmed',
            figure={
                'data': [confirmed_bar_graph],
                'layout': {
                    'xaxis': {
                        'title': 'Date',
                        'showgrid': False
                    },
                    'yaxis': {
                        'title': 'Number of Individuals',
                        'showgrid': False
                    },
                    'title': 'Confirmed',
                    'font': {
                        'color': 'grey'
                    }
                }
            }
        ),

        dcc.Graph(
            id='Graph_hospitalized',
            figure={
                'data': [hospital_scatter_graph],
                'layout': {
                    'xaxis': {
                        'title': 'Date',
                        'showgrid': False
                    },
                    'yaxis': {
                        'title': 'Number of Individuals',
                        'showgrid': False
                    },
                    'title': 'Hospitalized',
                    'font': {
                        'color': 'grey'
                    }
                }
            }
        ),
        dcc.Graph(
            id='Graph_hospital',
            figure={
                'data': [hospital_bar_graph],
                'layout': {
                    'xaxis': {
                        'title': 'Date',
                        'showgrid': False
                    },
                    'yaxis': {
                        'title': 'Number of Individuals',
                        'showgrid': False
                    },
                    'font': {
                        'color': 'grey'
                    }
                }
            }
        ),
        dcc.Graph(
            id='Graph_death',
            figure={
                'data': [death_scatter_graph],
                'layout': {
                    'xaxis': {
                        'title': 'Date',
                        'showgrid': False
                    },
                    'yaxis': {
                        'title': 'Number of Individuals',
                        'showgrid': False
                    },
                    'title': 'Deaths',
                    'font': {
                        'color': 'grey'
                    }
                }
            }

        ),
        dcc.Graph(
            id='Graph_Test_deaths',
            figure={
                'data': [death_bar_graph],
                'layout': {
                    'xaxis': {
                        'title': 'Date',
                        'showgrid': False
                    },
                    'yaxis': {
                        'title': 'Number of Individuals',
                        'showgrid': False
                    },
                    'title': 'Deaths',
                    'font': {
                        'color': 'grey'
                    }
                }
            }
        ),
        html.Div(
            children='Retrieved From: https://raw.githubusercontent.com/youraunt/public/master/INWK2300'
                     '/covid_19_Colorado_Daily.csv',
            style={'textAlign': 'left', 'color': 'grey'
                   }),
        html.Div(
            children='Source: https://covid19.colorado.gov/case-data',
            style={'textAlign': 'left', 'color': 'grey'
                   })
    ])
if __name__ == '__main__':
    app.run_server(debug=True)
