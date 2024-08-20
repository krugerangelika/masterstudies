import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

def create_team_schedule_layout():
    return dbc.Container([
        html.H2("Harmonogram Zespołu Medycznego"),
        dbc.Form([
            dbc.Row([
                dbc.Col(dbc.Label("Data")),
                dbc.Col(dbc.Input(id="input-schedule-date", type="date")),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Godzina")),
                dbc.Col(dbc.Input(id="input-schedule-time", type="time")),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Zespół")),
                dbc.Col(dcc.Dropdown(
                    id="input-team",
                    options=[
                        {"label": "Zespół A", "value": "team_a"},
                        {"label": "Zespół B", "value": "team_b"},
                        {"label": "Zespół C", "value": "team_c"}
                    ],
                    value="team_a"
                )),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Lokalizacja")),
                dbc.Col(dbc.Input(id="input-location", type="text", placeholder="Lokalizacja")),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Opis")),
                dbc.Col(dbc.Textarea(id="input-description")),
            ], className="mb-3"),
            dbc.Button("Zapisz Harmonogram", id="submit-schedule-button", color="primary"),
            html.Div(id="schedule-output-state", className="mt-3")
        ], className="mt-5")
    ], className="mt-5")

def create_team_schedule(server):
    app = dash.Dash(
        server=server,
        routes_pathname_prefix='/main-panel/team-schedule/',
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )

    app.layout = create_team_schedule_layout()

    return app
