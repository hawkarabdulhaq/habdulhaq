import os
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from pages import home, testimony, learning_platform, enrollment

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Personalized Python Training"

# Load custom CSS styles
app.css.append_css({"external_url": "/assets/style.css"})

# App layout with sidebar navigation
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # For URL-based routing
    html.Div([
        # Sidebar with Logo and Navigation
        html.Img(src='/assets/logo.jpg', style={'width': '200px'}),
        html.H2("Personalized Python Training"),
        html.Div([
            dcc.Link("Home", href="/", className="nav-link"),
            dcc.Link("Testimonials", href="/testimonials", className="nav-link"),
            dcc.Link("Learning Platform", href="/learning-platform", className="nav-link"),
            dcc.Link("Enrollment", href="/enrollment", className="nav-link"),
        ], style={"display": "flex", "flexDirection": "column", "marginTop": "20px"}),
        
        # Contact Information and Calendly link
        html.Div([
            html.P("Contact:"),
            html.A("connect@habdulhaq.com", href="mailto:connect@habdulhaq.com"),
            html.Br(),
            html.A("Website", href="https://www.habdulhaq.com"),
            html.Br(),
            html.A("Discord Server", href="https://discord.gg/wcypuxhF"),
            html.Br(),
            html.A("Schedule a Demo on Calendly", href="https://calendly.com/hawkar_abdulhaq"),
        ], style={"marginTop": "30px"}),
    ], style={'width': '20%', 'display': 'inline-block', 'verticalAlign': 'top'}),

    # Main content area for dynamic page rendering
    html.Div(id='page-content', style={'width': '75%', 'display': 'inline-block', 'padding': '20px'}),
])

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
    elif pathname == "/enrollment":
        return enrollment.layout
    return home.layout  # Default page for "/"

# Bind to the environment's PORT if defined, otherwise default to 8050 for local testing
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8050))
    app.run_server(host="0.0.0.0", port=port, debug=True)
