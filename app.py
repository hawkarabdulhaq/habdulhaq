from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc  # Optional: for Bootstrap styling
from pages import home, testimony, learning_platform, enrollment

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Personalized Python Training"

# Load custom CSS styles
app.css.append_css({"external_url": "/assets/style.css"})

# App layout with sidebar navigation
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # For routing
    html.Div([
        # Sidebar with Logo and Navigation
        html.Img(src='/assets/logo.jpg', style={'width': '200px'}),
        html.H2("Personalized Python Training"),
        html.Button("Home", id="home-button", n_clicks=0),
        html.Button("Testimonials", id="testimonials-button", n_clicks=0),
        html.Button("Learning Platform", id="learning-platform-button", n_clicks=0),
        html.Button("Enrollment", id="enrollment-button", n_clicks=0),
        # Contact and Calendly Info
        html.Div([
            html.P("Contact:"),
            html.A("connect@habdulhaq.com", href="mailto:connect@habdulhaq.com"),
            html.Br(),
            html.A("Website", href="https://www.habdulhaq.com"),
            html.Br(),
            html.A("Discord Server", href="https://discord.gg/wcypuxhF"),
            html.Br(),
            html.A("Schedule a Demo on Calendly", href="https://calendly.com/hawkar_abdulhaq"),
        ]),
    ], style={'width': '20%', 'display': 'inline-block', 'vertical-align': 'top'}),

    # Main content area for pages
    html.Div(id='page-content', style={'width': '75%', 'display': 'inline-block'}),
])

# Callbacks for page navigation
@app.callback(
    Output('page-content', 'children'),
    [Input('home-button', 'n_clicks'),
     Input('testimonials-button', 'n_clicks'),
     Input('learning-platform-button', 'n_clicks'),
     Input('enrollment-button', 'n_clicks')]
)
def display_page(home_clicks, testimonials_clicks, learning_platform_clicks, enrollment_clicks):
    if home_clicks:
        return home.layout
    elif testimonials_clicks:
        return testimony.layout
    elif learning_platform_clicks:
        return learning_platform.layout
    elif enrollment_clicks:
        return enrollment.layout
    return home.layout  # Default page

if __name__ == '__main__':
    app.run_server(debug=True)
