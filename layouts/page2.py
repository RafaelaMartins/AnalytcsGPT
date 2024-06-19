from dash import dcc, html

layout = html.Div([
    html.H2('Page 2'),
    dcc.Link('Go to Page 1', href='/page1'),
    # Seu conteúdo de Page 2 aqui
])
