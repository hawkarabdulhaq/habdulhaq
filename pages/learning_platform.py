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
            html.Li(
                children=[
                    html.Strong("One-on-One Online Session"),
                    " to kickstart the week, allowing you to discuss your goals and clear any doubts in a personalized setting."
                ],
                style={"font-weight": "bold"}
            ),
            html.Li(
                children=[
                    html.Strong("Pre-recorded Lectures"),
                    " covering the core concepts and topics in detail."
                ],
                style={"font-weight": "bold"}
            ),
            html.Li(
                children=[
                    html.Strong("Explanatory Modules"),
                    " breaking down complex ideas with clear, digestible explanations."
                ],
                style={"font-weight": "bold"}
            ),
            html.Li(
                children=[
                    html.Strong("Interactive Discussions"),
                    " on key topics to deepen your understanding."
                ],
                style={"font-weight": "bold"}
            ),
            html.Li(
                children=[
                    html.Strong("Assignments"),
                    " to apply what you’ve learned and receive feedback."
                ],
                style={"font-weight": "bold"}
            ),
        ], className="content"),

        html.P(
            "This interactive platform encourages engagement and ensures you have the support needed to achieve your learning objectives. Stay tuned for access details and further updates!"
        )
    ], className="content"),
])
