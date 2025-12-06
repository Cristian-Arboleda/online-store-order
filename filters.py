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
    Output({"type": "filter_btn", "column": ALL, "value": ALL}, "className"),
    Input('filters_activated', 'data'),
    Input({"type": "filter_btn", "column" : ALL, "value": ALL}, 'n_clicks')
)

def update(*args):
    
    # Obtener la lista de los filtros activados
    filters_activated = ctx.inputs["filters_activated.data"]
    
    # Obtener el boton del filtro presionado
    triggered = ctx.triggered_id
    
    # Si se presiona un boton de filtro
    if triggered:
        column = triggered['column']
        value = triggered['value']
        
        # Si el valor se encuentra en la columna significa que esta activado el filtro
        if value in filters_activated[column] :
            filters_activated[column].remove(value)
            print('Se ha desactivado el filtro: ', value)
        else:
            print('Se ha activado el filtro:', value)
            filters_activated[column].append(value)
    
    # Clases para los botones presionados
    class_activated_filters = 'filters_element_btn filters_element_btn_activated'
    class_deactivated_filters = 'filters_element_btn filters_element_btn_deactivated'
    
    class_filters = []
    for column in unique_filters:
        for value in unique_filters[column]:
            if value in filters_activated[column]:
                class_filters.append(class_activated_filters)
            else:
                class_filters.append(class_deactivated_filters)
    
    return filters_activated, class_filters