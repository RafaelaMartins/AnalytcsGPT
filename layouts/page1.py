from dash import dcc, html

layout = html.Div([
    html.H2('Page 1'),
    dcc.Link('Go to Page 2', href='/page2'),
    # Seu conteúdo de Page 1 aqui
])
