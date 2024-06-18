import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from layout import layout
import plotly.express as px
# Inicialize o aplicativo Dash com um tema Bootstrap para estilos mais bonitos
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# Use o layout importado do arquivo layout.py
app.layout = layout

@app.callback(
    Output('live-update-text', 'children'),
    [Input('interval-component', 'n_intervals')],
)
def update_layout(n):
    return html.H6(f'Atualizado {n} vezes')

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
