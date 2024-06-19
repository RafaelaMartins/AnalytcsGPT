from dash import dcc, html
from dash.dependencies import Input, Output
from app import app
import plotly.express as px
from layouts import  page1, page2
import layout
# Defina o layout principal com um componente `dcc.Location` para rastrear a URL
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Callback para atualizar o conteúdo da página com base na URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page1':
        return page1.layout
    elif pathname == '/page2':
        return page2.layout
    else:
        return layout.layout  # página inicial ou layout de erro 404

@app.callback(
    Output('graph', 'figure'),
    [Input('names', 'value'), Input('values', 'value')]
)
def update_graph(names, values):
    teste = px.data.tips()  # replace with your own data source
    fig = px.pie(teste, values=values, names=names, hole=.3)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
