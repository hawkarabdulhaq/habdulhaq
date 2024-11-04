import os
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from pages import home, testimony, learning_platform, enrollment

# Initialize the Dash app with Bootstrap theme
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Personalized Python Training"

# Sidebar layout
sidebar = dbc.Card(
    [
        dbc.CardImg(src="/assets/logo.jpg", top=True, style={"width": "100%", "padding": "10px"}),
        dbc.CardBody(
            [
                html.H4("Personalized Python Training", className="card-title"),
                html.Hr(),
                dbc.Nav(
                    [
                        dbc.NavLink("Home", href="/", active="exact", className="nav-link"),
                        dbc.NavLink("Testimonials", href="/testimonials", active="exact", className="nav-link"),
                        dbc.NavLink("Learning Platform", href="/learning-platform", active="exact", className="nav-link"),
                        dbc.NavLink("Enrollment", href="/enrollment", active="exact", className="nav-link"),
                    ],
                    vertical=True,
                    pills=True,
                ),
                html.Hr(),
                html.Div(
                    [
                        html.P("Contact:"),
                        html.A("connect@habdulhaq.com", href="mailto:connect@habdulhaq.com"),
                        html.Br(),
                        html.A("Website", href="https://www.habdulhaq.com"),
                        html.Br(),
                        html.A("Discord Server", href="https://discord.gg/wcypuxhF"),
                        html.Br(),
                        html.A("Schedule a Demo on Calendly", href="https://calendly.com/hawkar_abdulhaq"),
                    ],
                    style={"fontSize": "0.9rem"},
                ),
            ]
        ),
    ],
    style={"width": "250px", "marginTop": "20px", "backgroundColor": "#f8f9fa"},
)

# Main content area
content = html.Div(id="page-content", style={"padding": "20px"})

# App layout
app.layout = dbc.Container(
    [
        dcc.Location(id="url", refresh=False),
        dbc.Row(
            [
                dbc.Col(sidebar, md=3),
                dbc.Col(content, md=9),
            ],
            className="g-0",  # no gutter
        ),
    ],
    fluid=True,
)

# Callback for rendering pages based on URL
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/testimonials":
        return testimony.layout
    elif pathname == "/learning-platform":
        return learning_platform.layout
    elif pathname == "/enrollment":
        return enrollment.layout
    return home.layout  # Default page for "/"

# Define the server for gunicorn
server = app.server

# Bind to the environment's PORT if defined, otherwise default to 8050 for local testing
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run_server(host="0.0.0.0", port=port)
