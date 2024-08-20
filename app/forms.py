import dash_bootstrap_components as dbc
from dash import html

def create_patient_registration_form():
    return dbc.Form(
        [
            dbc.FormGroup([
                dbc.Label("Imię"),
                dbc.Input(type="text", placeholder="Wpisz imię")
            ]),
            dbc.FormGroup([
                dbc.Label("Nazwisko"),
                dbc.Input(type="text", placeholder="Wpisz nazwisko")
            ]),
            dbc.FormGroup([
                dbc.Label("Data urodzenia"),
                dbc.Input(type="date")
            ]),
            dbc.FormGroup([
                dbc.Button("Zarejestruj", color="primary")
            ])
        ]
    )
