from dash import html, callback, Input, Output, State, ctx


theme_html = html.Div(
    id='theme_container',
    className='element_container',
    children=[
        html.Button('Dark', id='dark_btn', className='theme_btn'),
        html.Button('Light', id='light_btn', className='theme_btn')
    ]
)

@callback(
    Output('container_main', 'className'),
    Output('container_main', 'style'),
    Input('dark_btn', 'n_clicks'),
    Input('light_btn', 'n_clicks')
)

def update_theme(dark_btn, light_btn):
    
    triggered = ctx.triggered_id
    
    if triggered == 'dark_btn' or triggered == None:
        theme = 'theme-dark'
        fondo = {'background': 'rgb(21, 17, 40)'}
    
    elif triggered == 'light_btn':
        theme ='theme-light'
        fondo = {'background': 'white'}
    
    print('Theme establecido:', theme)
    
    return theme, fondo