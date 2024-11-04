import os
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from pages import home, testimony, learning_platform, enrollment, learning  # Import learning module

# Initialize the Dash app with a Bootstrap theme
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Personalized Python Training"

# Sidebar layout
sidebar = dbc.Col(
    [
        html.Img(src='/assets/logo.jpg', style={'width': '100%', 'padding': '10px'}),
        html.H2("Personalized Python Training", className="text-center"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact", className="nav-link"),
                dbc.NavLink("Testimonials", href="/testimonials", active="exact", className="nav-link"),
                dbc.NavLink("Learning Platform", href="/learning-platform", active="exact", className="nav-link"),
                dbc.NavLink("Learning Content", href="/learning-content", active="exact", className="nav-link"),  # New link
                dbc.NavLink("Enrollment", href="/enrollment", active="exact", className="nav-link"),
            ],
            vertical=True,
            pills=True,
            className="mt-4",
        ),
        html.Div([
            html.P("Contact:", className="mt-4"),
            html.A("connect@habdulhaq.com", href="mailto:connect@habdulhaq.com", className="d-block"),
            html.A("Website", href="https://www.habdulhaq.com", className="d-block"),
            html.A("Discord Server", href="https://discord.gg/wcypuxhF", className="d-block"),
            html.A("Schedule a Demo on Calendly", href="https://calendly.com/hawkar_abdulhaq", className="d-block"),
        ], style={"marginTop": "20px"}),
    ],
    width=3,
    style={"backgroundColor": "#f8f9fa", "padding": "20px"},
)

# Main content area
content = dbc.Col(
    html.Div(id="page-content", className="p-4"),
    width=9
)

# App layout with sidebar and content
app.layout = dbc.Container(
    fluid=True,
    children=[
        dcc.Location(id='url', refresh=False),
        dbc.Row([sidebar, content])
    ]
)

# Callback for rendering pages based on URL
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == "/testimonials":
        return testimony.layout
    elif pathname == "/learning-platform":
        return learning_platform.layout
    elif pathname == "/learning-content":  # Route for Learning Content
        return learning.layout
    elif pathname == "/enrollment":
        return enrollment.layout
    return home.layout  # Default page for "/"

# Define the server for gunicorn
server = app.server

# Bind to the environment's PORT if defined, otherwise default to 8050 for local testing
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8050))
    app.run_server(host="0.0.0.0", port=port)
