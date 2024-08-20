import dash_bootstrap_components as dbc
from dash import html

def create_sidebar():
    return html.Div(
        [
            html.H2("Menu", className="display-4"),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink("Strona Główna", href="/main-panel/", id="home-link", active="exact"),
                    dbc.NavLink("Rejestracja Nowego Pacjenta", href="/main-panel/patient-registration/", id="register-link", active="exact"),
                    dbc.NavLink("Zarządzanie Wizytami Pacjentów", href="/main-panel/patient-visits/", id="visits-link", active="exact"),
                    dbc.NavLink("Harmonogram Zespołu Medycznego", href="/main-panel/team-schedule/", id="graphs-link", active="exact"),
                    dbc.NavLink("Zarządzanie Lekami i Apteką", href="/main-panel/pharmacy-management/",
                                id="pharmacy-management-link"),  # Dodaj nowy link
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style={"position": "fixed", "top": 0, "left": 0, "bottom": 0, "width": "18rem", "padding": "2rem 1rem", "backgroundColor": "#f8f9fa"},
    )
