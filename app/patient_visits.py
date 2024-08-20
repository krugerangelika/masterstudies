import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

def create_patient_visits_layout():
    return dbc.Container([
        html.H2("Zarządzanie Wizytami Pacjentów"),
        dbc.Form([
            dbc.Row([
                dbc.Col(dbc.Label("Imię i Nazwisko Pacjenta")),
                dbc.Col(dbc.Input(id="input-visit-patient-name", type="text")),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Data Wizyty")),
                dbc.Col(dbc.Input(id="input-visit-date", type="date")),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Godzina Wizyty")),
                dbc.Col(dbc.Input(id="input-visit-time", type="time")),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Powód Wizyty")),
                dbc.Col(dbc.Input(id="input-visit-reason", type="text")),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Dodatkowe Uwagi")),
                dbc.Col(dbc.Textarea(id="input-visit-notes")),
            ], className="mb-3"),
            dbc.Button("Zapisz Wizytę", id="submit-visit-button", color="primary"),
            html.Div(id="visit-output-state", className="mt-3")
        ], className="mt-5")
    ], className="mt-5")

def create_patient_visits(server):
    app = dash.Dash(
        server=server,
        routes_pathname_prefix='/main-panel/patient-visits/',
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )

    app.layout = create_patient_visits_layout()

    return app
