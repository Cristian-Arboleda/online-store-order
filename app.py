from dash import Dash, html, dcc
from me import *
from filters import filters_html, unique_filters
from theme import theme_html
from graph import graphs

app = Dash()

app.layout = html.Div(
    id='container_main',
    className='theme-dark',
    children=[
        dcc.Store(id='filters_activated', data=unique_filters),
        theme_html,
        me_,
        filters_html,
        *graphs
    ]
)

app.run(port=8061, debug=True)