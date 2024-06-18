from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Search", color="primary", className="ms-2", n_clicks=0
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

card_content = [
    dbc.CardHeader("Média"),
    dbc.CardBody(
        [
            html.H5("127,98", className="card-title"),
        ]
    ),
]


layout = html.Div(style={'color': 'gray'}, children=[
    dbc.Row([
        dbc.Navbar(
            dbc.Container(
                [
                    html.A(
                        dbc.Row(
                            [
                                dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                                dbc.Col(dbc.NavbarBrand("Dashboard Analytics", className="ms-2")),
                            ],
                            align="center",
                            className="g-0 d-flex justify-content-center text-center",
                        ),
                        href="https://plotly.com",
                        style={"textDecoration": "none"},
                        className="d-flex text-center col-md-9 col-lg-12 col-sm-9 justify-content-center"
                    ),
                    dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                    dbc.Collapse(
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True,
                        className="col-sm-2 mr-1",
                    ),
                ]
            ),
            color="dark",
            dark=True,
            className="col-sm-12 col-md-12 col-lg-12",
        )
    ], align="center", className="bg-dark text-center text-white fs-3 mb-6"),
    
    dbc.Container([
        html.Div([
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardHeader("Média"),
                    dbc.CardBody([
                        html.H5("127,98", className="card-title"),
                    ]),
                ], color="primary", inverse=True)),
                dbc.Col(dbc.Card([
                    dbc.CardHeader("Mediana"),
                    dbc.CardBody([
                        html.H5("100,27", className="card-title"),
                    ]),
                ], color="danger", inverse=True)),
                dbc.Col(dbc.Card([
                    dbc.CardHeader("Moda"),
                    dbc.CardBody([
                        html.H5("114,72", className="card-title"),
                    ]),
                ], color="warning", inverse=True)),
            ], className="mb-4 ml-1 mr-1 bg-light"),
        ], className="mt-2"),
        
        dbc.Row([
            dbc.Col(
                dbc.Card([
                    dbc.CardHeader("Tabela dados populacional por continente", className="font-weight-bold text-center bg-dark text-light"),
                    dbc.CardBody([
                        dash_table.DataTable(
                            data=df.to_dict('records'), 
                            page_size=10, 
                            style_table={'overflowX': 'auto'},
                        )
                    ]),
                ], className="d-flex mb-3 mt-3 col-sm-12 col-md-12 col-lg-12"),
            )
        ], className="bg-light d-flex col-sm-12 col-md-12 col-lg-12"),
        
        dbc.Row([
            dbc.Col(
                dbc.Card([
                    dbc.CardHeader("Média expectativa de vida por continente", className="font-weight-bold text-center bg-dark text-light"),
                    dbc.CardBody([
                        dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg')),
                    ]),
                ]),
            )
        ], className="bg-light"),
        
        html.Div([
            dbc.Row([
                dbc.Col(
                    dbc.Card([
                        dbc.CardHeader('Analysis of the restaurant sales',className="font-weight-bold text-center bg-dark text-light"),
                        dbc.CardBody([
                            dcc.Graph(id="graph"),
                        ]),
                        dbc.CardFooter([
                            html.P("Names:"),
                            dcc.Dropdown(
                                id='names',
                                options=[
                                    {'label': 'smoker', 'value': 'smoker'},
                                    {'label': 'day', 'value': 'day'},
                                    {'label': 'time', 'value': 'time'},
                                    {'label': 'sex', 'value': 'sex'},
                                ],
                                value='day', clearable=False
                            ),
                            html.P("Values:"),
                            dcc.Dropdown(
                                id='values',
                                options=[
                                    {'label': 'total_bill', 'value': 'total_bill'},
                                    {'label': 'tip', 'value': 'tip'},
                                    {'label': 'size', 'value': 'size'},
                                ],
                                value='total_bill', clearable=False
                            ),
                        ]),
                    ]),
                )
            ], className="bg-light"),
        ]), 

        dbc.Row([
            dbc.Col(html.Div(id='live-update-text')),
        ], className="bg-light"),
    ]),
    
    dcc.Interval(id='interval-component', interval=1*1000, n_intervals=0)
])
