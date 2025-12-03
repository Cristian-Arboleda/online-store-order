import polars as pl
from dash import html, dcc, callback, Input, Output, State, ctx, no_update

database = pl.read_excel('Online-Store-Orders.xlsx')
database_json = database.to_dicts()

list_years = database['Date'].dt.year().unique().sort()

filter_column = ['Date', 'PaymentMethod', 'OrderStatus', 'CouponCode', 'ReferralSource']

unique_filters = {
    column : database[column].unique()
    if column !=  "Date" else
    database[column].dt.year().unique().sort()
    for column in filter_column
}

print(unique_filters)

html_filters = html.Div(
    id='filters_container',
    className='element_container',
    children=[
        #dcc.Store(id='database', data=database_json),
        
        html.Div(
            className='filters_element_container',
            children=[
                html.Button(
                    children=unique_value
                    #children=f'{unique_filters[column]}'
                )
                for unique_value in unique_filters[column]
            ]
        )
        for column in unique_filters
    ]
)

"""@callback(
    Output('database', 'data'),
    [
        Input(f'{year}_btn', 'n_clicks')
        for year in list_years
    ],
    Input('database', 'data')
)
def years_update(*args):
    
    # Obtener el boton del year seleccionado
    triggered = ctx.triggered_id
    
    if not triggered:
        return no_update
    
    year = triggered.replace('_btn', '')
    
    data = data
    return no_update"""