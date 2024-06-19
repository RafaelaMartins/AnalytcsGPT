import dash
import dash_bootstrap_components as dbc

# Inicialize o aplicativo Dash com um tema Bootstrap para estilos mais bonitos
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Defina o servidor para que ele possa ser usado pelo Flask para produção
server = app.server
