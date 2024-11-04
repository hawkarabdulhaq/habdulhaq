from dash import html, dcc, callback, Input, Output, State
import gspread
from google.oauth2.service_account import Credentials
from dash import dash_table
import dash_bootstrap_components as dbc

# Google Sheets connection function
def connect_to_google_sheet(sheet_name):
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    credentials = Credentials.from_service_account_info(
        # Replace this with actual credential loading in Dash (use config or .env)
        st.secrets["gcp_service_account"], 
        scopes=scope
    )
    client = gspread.authorize(credentials)
    sheet = client.open_by_key(st.secrets["spreadsheet"]["sheet_id"])
    return sheet.worksheet(sheet_name)

# Layout for the enrollment page
layout = html.Div([
    html.Div("Enrollment", className="title"),
    html.Div(
        "If you would like to enroll in the course, please select your preferred training type below and complete the enrollment form...",
        className="content"
    ),

    dcc.Tabs([
        dcc.Tab(label="Individual Training", children=[
            html.Div("Individual Training Enrollment", className="section-title"),
            dbc.Form([
                dbc.Label("Personal Information"),
                dbc.Input(id="name", placeholder="Name", type="text"),
                dbc.Input(id="age", placeholder="Age", type="number", min=0, max=120, step=1),
                dbc.Input(id="job", placeholder="Job", type="text"),
                dbc.Input(id="email", placeholder="Email", type="email"),
                dbc.Input(id="location", placeholder="Location", type="text"),
                dcc.Dropdown(id="gender", options=[
                    {'label': 'Male', 'value': 'Male'},
                    {'label': 'Female', 'value': 'Female'},
                    {'label': 'Other', 'value': 'Other'}
                ], placeholder="Gender"),

                dbc.Label("How did you hear about the course?"),
                dcc.Dropdown(id="course_discovery", options=[
                    {'label': 'Telegram', 'value': 'Telegram'},
                    {'label': 'YouTube', 'value': 'YouTube'},
                    {'label': 'Facebook', 'value': 'Facebook'},
                    {'label': 'Search', 'value': 'Search'},
                    {'label': 'Friend', 'value': 'Friend'}
                ], placeholder="Select one"),

                dbc.Label("Preferred Payment Method"),
                dcc.Dropdown(id="payment_method", options=[
                    {'label': 'FIB', 'value': 'FIB'},
                    {'label': 'Paypal', 'value': 'Paypal'},
                    {'label': 'Revolut', 'value': 'Revolut'}
                ], placeholder="Choose your payment method"),

                dbc.Checkbox(id="individual_agreement", label="I agree to the terms"),
                dbc.Button("Submit Individual Enrollment", id="individual_submit_button", color="primary"),
            ]),
            html.Div(id="individual_enrollment_status")
        ]),

        dcc.Tab(label="Group Training", children=[
            html.Div("Group Training Enrollment", className="section-title"),
            dbc.Form([
                dbc.Label("Personal Information"),
                dbc.Input(id="g_name", placeholder="Name", type="text"),
                dbc.Input(id="g_age", placeholder="Age", type="number", min=0, max=120, step=1),
                dbc.Input(id="g_job", placeholder="Job", type="text"),
                dbc.Input(id="g_email", placeholder="Email", type="email"),
                dbc.Input(id="g_location", placeholder="Location", type="text"),
                dcc.Dropdown(id="g_gender", options=[
                    {'label': 'Male', 'value': 'Male'},
                    {'label': 'Female', 'value': 'Female'},
                    {'label': 'Other', 'value': 'Other'}
                ], placeholder="Gender"),

                dbc.Label("How did you hear about the course?"),
                dcc.Dropdown(id="g_course_discovery", options=[
                    {'label': 'Telegram', 'value': 'Telegram'},
                    {'label': 'YouTube', 'value': 'YouTube'},
                    {'label': 'Facebook', 'value': 'Facebook'},
                    {'label': 'Search', 'value': 'Search'},
                    {'label': 'Friend', 'value': 'Friend'}
                ], placeholder="Select one"),

                dbc.Label("Group Details"),
                dcc.Dropdown(id="group_size", options=[{'label': i, 'value': i} for i in range(3, 7)], placeholder="How many people are in your group?"),
                dbc.Textarea(id="group_names", placeholder="Enter names of all group members (one name per line)"),

                dbc.Label("Preferred Payment Method"),
                dcc.Dropdown(id="g_payment_method", options=[
                    {'label': 'FIB', 'value': 'FIB'},
                    {'label': 'Paypal', 'value': 'Paypal'},
                    {'label': 'Revolut', 'value': 'Revolut'}
                ], placeholder="Choose your payment method"),

                dbc.Checkbox(id="group_representative_agreement", label="I confirm I am representing the group"),
                dbc.Checkbox(id="group_terms_agreement", label="I agree to the terms"),
                dbc.Button("Submit Group Enrollment", id="group_submit_button", color="primary"),
            ]),
            html.Div(id="group_enrollment_status")
        ]),
    ])
])

# Callbacks for form submissions
@callback(
    Output("individual_enrollment_status", "children"),
    Input("individual_submit_button", "n_clicks"),
    State("name", "value"), State("age", "value"), State("job", "value"),
    State("email", "value"), State("location", "value"), State("gender", "value"),
    State("course_discovery", "value"), State("payment_method", "value"),
    State("individual_agreement", "value")
)
def submit_individual_enrollment(n_clicks, name, age, job, email, location, gender, course_discovery, payment_method, agreement):
    if n_clicks:
        if not agreement:
            return "Please agree to the terms to proceed with Individual Training enrollment."
        else:
            sheet = connect_to_google_sheet("one")
            sheet.append_row([name, age, job, email, location, gender, course_discovery, payment_method])
            return "Thank you for your enrollment request! You will receive a bill shortly with payment instructions."

@callback(
    Output("group_enrollment_status", "children"),
    Input("group_submit_button", "n_clicks"),
    State("g_name", "value"), State("g_age", "value"), State("g_job", "value"),
    State("g_email", "value"), State("g_location", "value"), State("g_gender", "value"),
    State("g_course_discovery", "value"), State("group_size", "value"),
    State("group_names", "value"), State("g_payment_method", "value"),
    State("group_representative_agreement", "value"), State("group_terms_agreement", "value")
)
def submit_group_enrollment(n_clicks, name, age, job, email, location, gender, course_discovery, group_size, group_names, payment_method, representative_agreement, terms_agreement):
    if n_clicks:
        if not representative_agreement or not terms_agreement:
            return "Please confirm the terms and representation agreement to proceed with Group Training enrollment."
        elif group_size and not group_names:
            return "Please enter the names of all group members."
        else:
            sheet = connect_to_google_sheet("group")
            sheet.append_row([name, age, job, email, location, gender, course_discovery, group_size, group_names, payment_method])
            return "Thank you for your enrollment request! You will receive a bill shortly with payment instructions."
