#  Dependencies
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import numpy as np
import pdfkit

#  urls used
ny_times_url_state = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
ny_times_url_county = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
my_git_url = 'https://raw.githubusercontent.com/youraunt/public/master/INWK2300/covid_19_Colorado_Daily.csv'
colorado_gov_url = 'https://covid19.colorado.gov/case-data'
welcome_message = '\n\nWelcome to my Data Visualization Project\n' \
                  'Load the url in your preferred browser.\n\n\n\n'
df = pd.read_csv(my_git_url, parse_dates=['Date'])
# -------------------------------------------------------------------------------------------------------------
#  Data
data_frame = pd.DataFrame(pd.read_csv(ny_times_url_state, parse_dates=['date']))
data_frame = pd.pivot_table(data_frame, values='deaths', index=['date'], columns='state', aggfunc=np.sum)
#  Working with go.Figure to handle style
total_deaths_nytimes = go.Figure()
for col in data_frame.columns:
    total_deaths_nytimes.add_trace(
        go.Scatter(x=data_frame.index, y=data_frame[col].values, name=col, mode='markers+lines',
                   line=dict(shape='linear'), connectgaps=True))
total_deaths_nytimes.update_layout(
    title="Total Deaths",
    xaxis_title='Date',
    yaxis_title="# Deceased",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color='grey'
    )
)
data_frame = pd.DataFrame(pd.read_csv(ny_times_url_state, parse_dates=['date']))
data_frame = pd.pivot_table(data_frame, values='cases', index='date', columns='state', aggfunc=np.sum)
total_cases_nytimes = go.Figure()

for col in data_frame.columns:
    total_cases_nytimes.add_trace(
        go.Scatter(x=data_frame.index, y=data_frame[col].values, name=col, mode='markers+lines',
                   line=dict(shape='linear'), connectgaps=True)
    )
total_cases_nytimes.update_layout(
    title="Total Infections",
    xaxis_title='Date',
    yaxis_title="# Infected",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color='grey'
    )
)
data_frame = pd.DataFrame(pd.read_csv(ny_times_url_county, parse_dates=['date']))
data_frame = data_frame.loc[data_frame['state'] == 'Colorado']
data_frame = pd.pivot_table(data_frame, values='deaths', index='date', columns='county', aggfunc=np.sum)
death_by_county = go.Figure()

for col in data_frame.columns:
    death_by_county.add_trace(
        go.Scatter(x=data_frame.index, y=data_frame[col].values, name=col, mode='markers+lines',
                   line=dict(shape='linear'), connectgaps=True)
    )
death_by_county.update_layout(
    title="Deaths by County",
    xaxis_title='Date',
    yaxis_title="# Deceased",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color='grey'
    ))

# -------------------------------------------------------------------------------------------------------------
#  Working with Dash to handle style
app = dash.Dash()
server = app.server

tested_scatter_graph = go.Scatter(x=df['Date'], y=df['Tested'], marker_color='darkSalmon')
new_cases_scatter_graph = go.Scatter(x=df['Date'], y=df['New Cases'], mode='lines+markers', marker_color='darkSalmon',
                                     line_color='CornflowerBlue')
new_deaths_graph = go.Scatter(x=df['Date'], y=df['New Deaths'], mode='lines+markers', marker_color='darkSalmon',
                              line_color='CornflowerBlue')
confirmed_scatter_graph = go.Scatter(x=df['Date'], y=df['Confirmed'], marker_color='darkSalmon')
hospital_scatter_graph = go.Scatter(x=df['Date'], y=df['Hospitalized'], marker_color='darkSalmon')
death_scatter_graph = go.Scatter(x=df['Date'], y=df['Death'], marker_color='darkSalmon')

app.layout = html.Div(
    style={'backgroundColor': 'white'},
    children=[
        html.H1(
            children=
            'Graphing the the effects of COVID-19.',
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
                        'title': '# Deceased',
                        'showgrid': False
                    },
                    'title': 'New Deaths by Day',
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
                        'title': '# Cases',
                        'showgrid': False
                    },
                    'title': 'New Cases by Day',
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
                        'title': '# Tested',
                        'showgrid': False
                    },
                    'title': 'Total Tested',
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
                        'title': '# Confirmed',
                        'showgrid': False
                    },
                    'title': 'Total Confirmed Infections',
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
                        'title': '# Hospitalized',
                        'showgrid': False
                    },
                    'title': 'Total Hospitalized',
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
                        'title': '# Deceased',
                        'showgrid': False
                    },
                    'title': 'Total Deaths',
                    'font': {
                        'color': 'grey'
                    }
                }
            }

        ),
        dcc.Graph(id='times_by_state', figure=total_deaths_nytimes),
        dcc.Graph(id='times_cases', figure=total_cases_nytimes),
        dcc.Graph(id='death_by_county', figure=death_by_county),
        html.Div(
            children='.............................',
            style={'textAlign': 'left', 'color': 'white'
                   }),
        html.Div(
            children='Source: ' + my_git_url,
            style={'textAlign': 'left', 'color': 'grey'
                   }),
        html.Div(
            children='Source: ' + colorado_gov_url,
            style={'textAlign': 'left', 'color': 'grey'
                   }),
        html.Div(
            children='Source: ' + ny_times_url_state,
            style={'textAlign': 'left', 'color': 'grey'
                   }),
        html.Div(
            children='Source: ' + ny_times_url_county,
            style={'textAlign': 'left', 'color': 'grey'
                   })

    ])
if __name__ == '__main__':
    print(welcome_message)
    pdfkit.from_url('http://local.dash.site', 'out.pdf')
    app.run_server(debug=True)
