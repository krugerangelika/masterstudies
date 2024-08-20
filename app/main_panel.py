import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app.sidebar import create_sidebar
from app.patient_registration import create_patient_registration_layout
from app.patient_visits import create_patient_visits_layout
from app.team_schedule import create_team_schedule_layout
from app.pharmacy_management import create_pharmacy_management_layout  # Dodano import
from app.utils import get_latest_updates, get_patients_data

def create_main_panel(server):
    app = dash.Dash(
        server=server,
        routes_pathname_prefix='/main-panel/',
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )

    app.layout = html.Div(
        [
            dcc.Location(id='url', refresh=False),
            create_sidebar(),
            html.Div(id='page-content', style={"marginLeft": "18rem", "padding": "2rem 1rem"})
        ]
    )

    @app.callback(
        Output('page-content', 'children'),
        Input('url', 'pathname')
    )
    def display_page(pathname):
        if pathname == '/main-panel/':
            return html.Div([
                html.H1("Witaj, Admin!"),
                html.Div(id="updates-section", style={'marginTop': '20px'}),
                html.Div(id="patient-list", style={'padding': '20px', 'maxWidth': '1200px', 'margin': 'auto'}),
                html.Div(id="quick-actions", style={'marginTop': '20px'}),
            ])
        elif pathname == '/main-panel/patient-registration/':
            return create_patient_registration_layout()
        elif pathname == '/main-panel/patient-visits/':
            return create_patient_visits_layout()
        elif pathname == '/main-panel/team-schedule/':
            return create_team_schedule_layout()
        elif pathname == '/main-panel/pharmacy-management/':  # Dodano nową sekcję
            return create_pharmacy_management_layout()
        return html.Div("Strona nie została znaleziona.")

    @app.callback(
        [Output('updates-section', 'children'),
         Output('patient-list', 'children')],
        [Input('url', 'pathname')]
    )
    def update_home_content(pathname):
        if pathname == '/main-panel/':
            updates = get_latest_updates()
            updates_list = [
                dbc.Card(
                    dbc.CardBody([
                        html.H5(update['title'], className="card-title"),
                        html.P(update['content'], className="card-text"),
                        html.Small(f"Data: {update['date']}", className="text-muted")
                    ])
                ) for update in updates
            ]
            patients = get_patients_data()
            patient_cards = [
                dbc.Card(
                    dbc.CardBody([
                        html.H4(f"{patient['name']}, {patient['age']} lat", className="card-title"),
                        html.P(f"Płeć: {patient['gender']}", className="card-text"),
                        html.P(f"Pokój: {patient['room']} - Oddział: {patient['ward']}", className="card-text"),
                        html.P(f"Stan zdrowia: {patient['health_status']}", className="card-text"),
                        dbc.Button("Zarządzaj wizytą", color="primary", href=f"/main-panel/patient-visits/{patient['id']}")
                    ])
                ) for patient in patients
            ]
            return updates_list, patient_cards
        return [], []

    return app
