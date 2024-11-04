from dash import html

# Define the layout for the learning platform page
layout = html.Div([
    html.H2("Our Learning Platform"),

    html.P("We offer a variety of learning options to suit your needs:", className="content"),

    html.Ul([
        html.Li([
            html.Strong("One-on-One Online Session"),
            html.Ul([
                html.Li("4 weeks of personalized instruction"),
                html.Li("Direct interaction with the instructor"),
                html.Li("Customized learning pace"),
            ])
        ], style={"font-weight": "bold"}),
        html.Li([
            html.Strong("Group Sessions"),
            html.Ul([
                html.Li("Collaborative learning environment"),
                html.Li("Group projects and discussions"),
                html.Li("Ideal for colleagues or friends"),
            ])
        ], style={"font-weight": "bold"}),
        html.Li([
            html.Strong("Self-Paced Online Materials"),
            html.Ul([
                html.Li("Access to video lectures and tutorials"),
                html.Li("Learn at your own pace"),
                html.Li("Flexible scheduling"),
            ])
        ], style={"font-weight": "bold"}),
    ]),

    # Call-to-action
    html.Div(
        html.A("Explore More", href="/enrollment", className="button"),
        style={"marginTop": "20px"}
    )
])
