from dash import html

# Define the layout for the Learning Platform page
layout = html.Div([
    # Title
    html.Div("Learning Platform", className="title"),
    
    # Image with caption
    html.Img(src="https://i.imgur.com/sLdcUzF.jpg", style={"width": "100%"}),
    html.Div("Canvas: Your Interactive Learning Platform", className="caption"),

    # Platform description with weekly module structure
    html.Div([
        html.P("Our dedicated learning platform is hosted on ", style={"display": "inline"}),
        html.Strong("Canvas"),
        html.P(
            ", designed to guide you through a structured and interactive 5-week program. Each week includes:",
            style={"display": "inline"}
        ),
        html.Ul([
            html.Li(html.Strong("One-on-One Online Session"), style={"font-weight": "bold"}, children=[
                " to kickstart the week, allowing you to discuss your goals and clear any doubts in a personalized setting."
            ]),
            html.Li(html.Strong("Pre-recorded Lectures"), style={"font-weight": "bold"}, children=[
                " covering the core concepts and topics in detail."
            ]),
            html.Li(html.Strong("Explanatory Modules"), style={"font-weight": "bold"}, children=[
                " breaking down complex ideas with clear, digestible explanations."
            ]),
            html.Li(html.Strong("Interactive Discussions"), style={"font-weight": "bold"}, children=[
                " on key topics to deepen your understanding."
            ]),
            html.Li(html.Strong("Assignments"), style={"font-weight": "bold"}, children=[
                " to apply what you’ve learned and receive feedback."
            ]),
        ], className="content"),

        html.P(
            "This interactive platform encourages engagement and ensures you have the support needed to achieve your learning objectives. Stay tuned for access details and further updates!"
        )
    ], className="content"),
])
