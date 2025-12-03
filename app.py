from dash import Dash, html
from me import *
from filters import *
from theme import *


app = Dash()

app.layout = html.Div(
    id='container_main',
    className='theme-dark',
    children=[
        theme_html,
        me_,
        html_filters
    ]
)

app.run(port=8061, debug=True)