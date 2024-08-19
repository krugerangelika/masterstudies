import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app.utils import get_patients_data, get_patient_by_id, get_latest_updates

def create_main_panel(server):
    app = dash.Dash(
        server=server,
        routes_pathname_prefix='/main-panel/',
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )

    app.layout = html.Div([
        dcc.Location(id="url"),
        html.H1(id="welcome-message"),
        html.Div(id="updates-section", style={'marginTop': '20px'}),
        html.Div(id="patient-list", style={'padding': '20px', 'maxWidth': '1200px', 'margin': 'auto'}),
        html.Div(id="quick-actions", style={'marginTop': '20px'}),
    ])

    # Aktualizacje powitania i przeglądu pacjentów
    @app.callback(
        [Output("welcome-message", "children"),
         Output("updates-section", "children")],
        [Input("url", "pathname")]
    )
    def update_welcome_and_updates(pathname):
        # Załóżmy, że mamy funkcję get_user_info, która zwraca informacje o zalogowanym użytkowniku
        user_info = {"role": "admin", "name": "Admin"}  # Przykładowe dane
        welcome_message = f"Witaj, {user_info['name']}!"

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

        return welcome_message, updates_list

    # Przegląd pacjentów
    @app.callback(
        Output("patient-list", "children"),
        [Input("url", "pathname")]
    )
    def display_patient_list(pathname):
        patients = get_patients_data()
        patient_cards = [
            dbc.Card(
                dbc.CardBody([
                    html.H4(f"{patient['name']}, {patient['age']} lat", className="card-title"),
                    html.P(f"Płeć: {patient['gender']}", className="card-text"),
                    html.P(f"Pokój: {patient['room']} - Oddział: {patient['ward']}", className="card-text"),
                    html.P(f"Stan zdrowia: {patient['health_status']}", className="card-text"),
                    dbc.Button("Zobacz szczegóły", href=f"/main-panel/patient/{patient['id']}", color="primary")
                ]),
                style={'marginBottom': '20px'}
            ) for patient in patients
        ]
        return patient_cards

    # Moduł "Szybkie akcje"
    @app.callback(
        Output("quick-action-output", "children"),
        [Input("add-note-button", "n_clicks"),
         Input("order-test-button", "n_clicks"),
         Input("view-results-button", "n_clicks")],
        State("url", "pathname"),
        prevent_initial_call=True
    )
    def handle_quick_actions(add_note_clicks, order_test_clicks, view_results_clicks, pathname):
        ctx = dash.callback_context
        if not ctx.triggered:
            raise dash.exceptions.PreventUpdate

        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        patient_id = pathname.split('/')[-1]
        patient = get_patient_by_id(patient_id)

        if not patient:
            return html.Div("Nie znaleziono pacjenta.")

        if button_id == "add-note-button":
            return html.Div([
                html.H5(f"Dodaj Notatkę dla: {patient['name']}"),
                dcc.Textarea(id="note-content", placeholder="Wprowadź treść notatki...", style={'width': '100%', 'height': '100px'}),
                dbc.Button("Zapisz Notatkę", id="save-note-button", color="primary", style={'marginTop': '10px'})
            ])
        elif button_id == "order-test-button":
            return html.Div([
                html.H5(f"Zleć Badanie dla: {patient['name']}"),
                dcc.Input(id="test-name", placeholder="Wprowadź nazwę badania", style={'width': '100%'}),
                dbc.Button("Zleć Badanie", id="order-test-submit-button", color="primary", style={'marginTop': '10px'})
            ])
        elif button_id == "view-results-button":
            return html.Div([
                html.H5(f"Wyniki Badań dla: {patient['name']}"),
                dbc.Table([
                    html.Thead(html.Tr([html.Th("Nazwa Badania"), html.Th("Wynik"), html.Th("Data")])),
                    html.Tbody([
                        html.Tr([html.Td("Ciśnienie krwi"), html.Td(patient['blood_pressure']), html.Td("2024-08-14")]),
                        html.Tr([html.Td("Tętno"), html.Td(patient['heart_rate']), html.Td("2024-08-14")]),
                        html.Tr([html.Td("Saturacja"), html.Td(patient['oxygen_saturation']), html.Td("2024-08-14")])
                    ])
                ], bordered=True)
            ])
        return html.Div("Nie znaleziono pacjenta.")

    return app
