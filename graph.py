from dash import html, callback, Input, Output, State, dcc
import plotly.express as px
import polars as pl
from data import *

graph_totalprice = html.Div(
    className='element_container',
    style={'grid-row': '1 / span 3', 'grid-column': '2 / span 4'},
    children=[
        dcc.Graph(
            id='graph_totalprice',
        )
    ]
)

graphs = [graph_totalprice]


@callback(
    Output('graph_totalprice', 'figure'),
    Input('filters_activated', 'data'),
)

def update_graphics(filters):
    
    # Filtrar la database
    database_filtered = database
    
    for column in filters:
        if column == 'Date':
            database_filtered = database_filtered.filter(
                pl.col(column).dt.year().is_in(filters[column])
            )
        else:
            database_filtered = database_filtered.filter(
                pl.col(column).is_in(filters[column])
            )
    print('database_filtered \n', database_filtered)
    
    database_filtered = database_filtered.sort('Date')
    
    # organizar por mes o year
    
    database_filtered = (
        database_filtered.with_columns(
            pl.col('Date').dt.strftime("%y%m").alias()
        )
    )
    
    # --------------------------------------------------------------------------------------------------------
    # Graficos
    
    fig = px.line(
        database_filtered,
        x='Date',
        y='TotalPrice',
    )
    
    return fig