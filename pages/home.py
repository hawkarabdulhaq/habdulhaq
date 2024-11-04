from dash import html
import dash_bootstrap_components as dbc

# Define the layout for the home page
layout = dbc.Container([
    # Title
    dbc.Row([
        dbc.Col(html.H2("Our Learning Platform", className="text-center mb-4"))
    ]),

    # Description Card
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.P("We offer a variety of learning options to suit your needs.", className="card-text"),
                    html.Ul([
                        html.Li([
                            html.Strong("One-on-One Online Session"),
                            html.Ul([
                                html.Li("4 weeks of personalized instruction"),
                                html.Li("Direct interaction with the instructor"),
                                html.Li("Customized learning pace"),
                            ], className="pl-3")
                        ], style={"font-weight": "bold"}),
                        html.Li([
                            html.Strong("Group Sessions"),
                            html.Ul([
                                html.Li("Collaborative learning environment"),
                                html.Li("Group projects and discussions"),
                                html.Li("Ideal for colleagues or friends"),
                            ], className="pl-3")
                        ], style={"font-weight": "bold"}),
                        html.Li([
                            html.Strong("Self-Paced Online Materials"),
                            html.Ul([
                                html.Li("Access to video lectures and tutorials"),
                                html.Li("Learn at your own pace"),
                                html.Li("Flexible scheduling"),
                            ], className="pl-3")
                        ], style={"font-weight": "bold"}),
                    ])
                ]),
                className="mb-4"
            ),
            width=12,
        )
    ]),

    # Call-to-action Button
    dbc.Row([
        dbc.Col(
            dbc.Button("Explore More", color="primary", href="/enrollment", className="mt-4"),
            width={"size": 6, "offset": 3},
        )
    ])
], fluid=True)
