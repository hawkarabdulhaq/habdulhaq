from dash import html, dcc

# Define the layout for the home page
layout = html.Div([
    # Title and introduction
    html.Div("Welcome to Personalized Python Training", className="title"),
    html.Div("Perfect for beginners looking to learn coding in just one month and deploy their prototype projects.", className="content"),

    # Embedded YouTube video
    html.Div([
        html.H3("Watch the demo video and get to know about the course"),
        html.Iframe(
            src="https://www.youtube.com/embed/G8BC2NIfpAs",
            width="853",
            height="480",
            style={"border": "0"},
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share",
            referrerPolicy="strict-origin-when-cross-origin"
        )
    ], className="video-container"),

    # Course overview section
    html.Div("Course Overview", className="section-title"),
    html.Div([
        html.P("Here’s a quick summary of what we’ll cover:"),
        html.Ul([
            html.Li(html.B("Setting Up Python: "), style={"font-weight": "bold"}, children=[
                "We’ll start by preparing your Python environment, ensuring you’re ready to begin your learning journey with a strong foundation."
            ]),
            html.Li(html.B("Hawkar's Workflow: "), style={"font-weight": "bold"}, children=[
                "I’ll introduce my structured approach to learning Python, focusing on breaking down complex concepts into manageable steps for an efficient learning process."
            ]),
            html.Li(html.B("Applying GitHub for App Creation: "), style={"font-weight": "bold"}, children=[
                "In this module, you'll learn to leverage GitHub to create a small app, setting the stage for your final project. By the end of the week, you’ll be equipped with the skills to develop, manage, and version control your project efficiently, all through GitHub."
            ]),
            html.Li(html.B("Developing Your Final Project: "), style={"font-weight": "bold"}, children=[
                "Over the course of a week, you’ll work on a draft version of your final project, applying core coding concepts in a practical way. This phase will allow you to gather feedback, refine your approach, and ensure your project aligns with your goals."
            ]),
            html.Li(html.B("Finalizing and Launching Your Project: "), style={"font-weight": "bold"}, children=[
                "In the final week, you’ll bring your project to completion. You’ll deploy the app, integrate key features, and showcase it within your community, creating a tangible outcome that reflects your learning journey."
            ]),
        ], className="content")
    ]),

    # Pricing information section
    html.Div("Pricing Options", className="section-title"),
    html.Div([
        html.P([
            html.Span("One-on-One Session: 435,000IQD for a personalized experience", className="highlight"),
            html.Br(),
            html.Span("Group Session (3+ people): 315,000IQD per person (for a group of colleagues or friends)", className="highlight"),
            html.Br(),
            "Choose the option that best fits your needs and learning preferences."
        ], className="content")
    ]),

    # Enrollment button
    html.Div(
        dcc.Link("Enroll in the Course", href="/enrollment", className="button"), 
        style={"marginTop": "20px"}
    )
])
