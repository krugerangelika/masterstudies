import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from flask import session
from app.sidebar import create_sidebar
from app.patient_registration import create_patient_registration_layout
from app.patient_list import PatientList
from app.patient_details import PatientDetails
from app.patient_cards import PatientCards
from app.database import SessionLocal, Patient

def create_main_panel(server):
    app = dash.Dash(
        server=server,
        routes_pathname_prefix='/main-panel/',
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )

    patient_cards = PatientCards()

    app.layout = html.Div(
        [
            dcc.Location(id='url', refresh=False),
            html.Div(id='sidebar', children=create_sidebar(), style={
                "position": "fixed", "top": 0, "left": 0, "bottom": 0, "width": "18rem", "padding": "2rem 1rem", "backgroundColor": "#f8f9fa"
            }),
            html.Div(id='page-content', style={"marginLeft": "18rem", "padding": "2rem 1rem"})
        ]
    )

    @app.callback(
        Output('sidebar', 'style'),
        Output('page-content', 'style'),
        Input('url', 'pathname')
    )
    def toggle_sidebar(pathname):
        if pathname == '/patient-registration/':
            return {"display": "none"}, {"marginLeft": "0", "padding": "2rem 1rem"}
        else:
            return {
                "position": "fixed", "top": 0, "left": 0, "bottom": 0, "width": "18rem", "padding": "2rem 1rem", "backgroundColor": "#f8f9fa"
            }, {"marginLeft": "18rem", "padding": "2rem 1rem"}

    @app.callback(
        Output('page-content', 'children'),
        Input('url', 'pathname')
    )
    def display_page(pathname):
        if pathname == '/main-panel/':
            return html.H1(f"Witaj, {session.get('username', 'User')}!")
        elif pathname == '/main-panel/patient-list/':
            patient_list = PatientList()
            layout = patient_list.create_patient_list_layout()
            patient_list.close_session()
            return layout
        elif pathname.startswith('/main-panel/patient-details/'):
            patient_id = int(pathname.split('/')[-1])
            patient_details = PatientDetails(patient_id)
            layout = patient_details.create_patient_details_layout()
            patient_details.close_session()
            return layout
        elif pathname.startswith('/main-panel/patient-edit/'):
            patient_id = int(pathname.split('/')[-1])
            return patient_cards.create_patient_edit_layout(patient_id)
        elif pathname == '/patient-registration/':
            return create_patient_registration_layout()
        elif pathname == '/main-panel/patient-cards/':
            return patient_cards.create_patient_cards_layout()
        else:
            return html.Div("Strona nie została znaleziona.")

    return app
