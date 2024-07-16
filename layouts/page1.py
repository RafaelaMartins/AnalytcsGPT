from dash import dcc, html
import pandas as pd


import dash_bootstrap_components as dbc
from dash import html
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
email_input = html.Div(
    [
        dbc.Label("Email", html_for="example-email"),
        dbc.Input(type="email", id="example-email", placeholder="Enter email"),
        dbc.FormText(
            "Are you on email? You simply have to be these days",
            color="secondary",
        ),
    ],
    className="mb-3",
)

password_input = html.Div(
    [
        dbc.Label("Password", html_for="example-password"),
        dbc.Input(
            type="password",
            id="example-password",
            placeholder="Enter password",
        ),
        dbc.FormText(
            "A password stops mean people taking your stuff", color="secondary"
        ),
    ],
    className="mb-3",
    
)
nav = dbc.Navbar(
            dbc.Container(
                [
                    html.A(
                        dbc.Row(
                            [
                                dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                                dbc.Col(dbc.NavbarBrand("Login Analytics", className="ms-2")),
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
layout = nav,dbc.Row([
                dbc.Col([
                    html.Div([
                        dbc.Card([
                            dbc.CardHeader("Acessar Conta", className="bg-light text-center"),
                            dbc.CardBody([
                                dbc.Container([
                                    dbc.Form([email_input, password_input]),
                                    # html.P("Não possui conta?",dbc.Badge("Cadastre-se", color="warning", className="btn me-1")),
                                    dbc.Button("Login", color="info", className="col-md-12 col-sm-12 col-lg-12 btn btn-block text-white"),
                                ]),
                            ]),dbc.Badge("Cadastre-se", color="dark", className="btn me-1"),
                            
                        ],className="w-100 mb-3 mt-3",), 
                    ]),
                ],className="d-flex justify-content-center"),
            ])

# 
# nav, dbc.Toast([ dbc.Container([
#                 dbc.Form([email_input, password_input])
#             ])
#         ])



# layout = html.Div([
#     html.H2('Page 1'),
#     dcc.Link('Go to Page 2', href='/page2'),
#     # Seu conteúdo de Page 1 aqui
# ])

