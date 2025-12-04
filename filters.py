import polars as pl
from dash import html, dcc, callback, Input, Output, State, ctx, no_update, ALL
from data import *

filters_html = html.Div(
    id='filters_container',
    className='element_container',
    children=[
        html.Div(
            children=[
                html.P(
                    column,
                    style={'text-align': 'center'}
                ),
                html.Div(
                    className='filters_element_container',
                    children=[
                        html.Button(
                            children=value,
                            className='filters_element_btn',
                            id={
                                "type": "filter_btn",
                                "column": column,
                                "value": value
                            }
                        )
                        for value in unique_filters[column]
                    ]
                )
            ]
        )
        for column in unique_filters
    ]
)

@callback(
    Output('filters_activated', 'data'),
    Input('filters_activated', 'data'),
    Input({"type": "filter_btn", "column" : ALL, "value": ALL}, 'n_clicks')
)

def update(*args):
    
    # Obtener el disparador de la funcion
    triggered = ctx.triggered_id
    
    # Si no se ha disparado la funcion
    if not triggered:
        return no_update
    
    column = triggered['column']
    value = triggered['value']
    
    # Obtener la lista de los filtros activados
    filters_activated = ctx.inputs["filters_activated.data"]
    
    
    # Si el valor se encuentra en la columna significa que esta activado el filtro
    if value in filters_activated[column] :
        filters_activated[column].remove(value)
        print('Se ha desactivado el filtro: ', value)
    else:
        print('Se ha activado el filtro:', value)
        filters_activated[column].append(value)
    
    return filters_activated