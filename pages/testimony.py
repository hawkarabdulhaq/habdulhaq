from dash import html

# Define the layout for the Testimonials page
layout = html.Div([
    # Title
    html.Div("Participant Testimonials", className="title"),

    # Introductory text
    html.Div(
        "These testimonials were gathered from participants who have completed the course. Each story reflects their unique journey, goals, and achievements in mastering Python and applying it to their personal or professional projects.",
        className="content"
    ),

    # Testimonial from Hakari Jalal Mohammed
    html.Details([
        html.Summary("Hakari Jalal Mohammed, Bibani"),
        html.Blockquote(
            "\"I joined this course to deepen my understanding and practical skills in developing web applications, especially to create tools that enhance learning and make quality educational resources more accessible. The hands-on projects were the most impactful, allowing me to apply my learning in real-time and engage with Dr. Hawkar, who fostered a supportive learning environment. A memorable experience was integrating AI into coding, sparking my interest in using AI for data analysis. I even developed a web application to assist students with chemistry calculations, which received positive feedback from users! This course has expanded my skill set and motivated me to pursue more projects in technology and education.\""
        ),
        html.P([
            html.Strong("LinkedIn: "),
            html.A("Hakari-Bibani", href="https://www.linkedin.com/in/hakary-bibani-796779334", target="_blank"),
            html.Span("  |  "),
            html.Strong("GitHub: "),
            html.A("Hakari-Bibani", href="https://github.com/Hakari-Bibani", target="_blank")
        ])
    ], className="testimonial"),

    # Testimonial from Akam Namq Abdulkareem
    html.Details([
        html.Summary("Akam Namq Abdulkareem"),
        html.Blockquote(
            "\"Taking this course was initially a personal hobby, but I have dreams of using these skills in finance and academics. Writing my first script was an exciting milestone. I faced challenges, like connecting Google Drive with Colab, but I overcame them by practicing. I plan to use these skills to build financial applications in the future. I would recommend this course to others, especially if they already have a solid background in computer knowledge.\""
        ),
        html.P([
            html.Strong("GitHub: "),
            html.A("akampython (to be updated soon)", href="https://github.com/akampython", target="_blank")
        ])
    ], className="testimonial"),

    # Testimonial from Haval Hassan Ali
    html.Details([
        html.Summary("Haval Hassan Ali"),
        html.Blockquote(
            "\"I wanted to acquire a valuable skill, and this course certainly delivered. Completing assignments was especially impactful, providing practical, hands-on experience. I faced challenges in deploying scripts due to setup and troubleshooting issues, but Dr. Hawkar’s guidance was invaluable. He suggested alternative tools that made the process much smoother, helping me complete deployment successfully. I’m now working on a project I hope to finish soon and plan to use these skills in a pharmacy-related project. I highly recommend this course for its practical approach and encourage future participants to stay engaged and seek support when needed.\""
        ),
        html.P([
            html.Strong("LinkedIn: "),
            html.A("Haval Ali", href="https://www.linkedin.com/in/haval-ali-72308a19b/", target="_blank")
        ])
    ], className="testimonial"),

    # Embedded external HTML content
    html.Div([
        html.H3("Course Participants"),
        html.Iframe(
            src="https://habdulhaq87.github.io/python_training/",
            width="100%",
            height="500px",
            style={"border": "none"}
        )
    ], style={"margin-top": "40px"})
])
