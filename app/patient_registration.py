import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from datetime import datetime

def get_patient_registration_layout():
    return html.Div([
        dcc.Location(id='url', refresh=False),
        dbc.Container([
            html.H1('Rejestracja Pacjentów', style={'textAlign': 'center'}),
            html.Hr(),
            dbc.Row([
                dbc.Col([
                    dbc.Form([
                        # The rest of your form fields go here...
                    ])
                ], width=12)
            ])
        ], fluid=True)
    ])

def create_patient_registration(server):
    app = dash.Dash(
        server=server,
        routes_pathname_prefix='/main-panel/patient-registration/',
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        name='patient_registration_dash'
    )

    # Layout for patient registration page
    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        dbc.Container([
            html.H1('Rejestracja Pacjentów', style={'textAlign': 'center'}),
            html.Hr(),
            dbc.Row([
                dbc.Col([
                    dbc.Form([
                        # Dane Osobowe
                        html.H4('Dane Osobowe'),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Imię"),
                                dbc.Input(type="text", id="first-name", placeholder="Wprowadź imię"),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Nazwisko"),
                                dbc.Input(type="text", id="last-name", placeholder="Wprowadź nazwisko"),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Data Urodzenia"),
                                dbc.Input(type="date", id="dob", placeholder="Wprowadź datę urodzenia"),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Płeć"),
                                dcc.Dropdown(
                                    id="gender",
                                    options=[
                                        {'label': 'Mężczyzna', 'value': 'M'},
                                        {'label': 'Kobieta', 'value': 'F'},
                                        {'label': 'Inna', 'value': 'Other'},
                                        {'label': 'Nieokreślona', 'value': 'Unspecified'}
                                    ],
                                    placeholder="Wybierz płeć"
                                ),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Numer PESEL lub inny identyfikator"),
                                dbc.Input(type="text", id="identifier", placeholder="Wprowadź numer PESEL lub identyfikator"),
                            ], width=12),
                        ], className="mb-3"),

                        # Dane Kontaktowe
                        html.H4('Dane Kontaktowe'),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Adres E-mail"),
                                dbc.Input(type="email", id="email", placeholder="Wprowadź adres e-mail"),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Numer Telefonu"),
                                dbc.Input(type="text", id="phone", placeholder="Wprowadź numer telefonu"),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Ulica i Numer Budynku"),
                                dbc.Input(type="text", id="street-address", placeholder="Wprowadź ulicę i numer budynku"),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Kod Pocztowy"),
                                dbc.Input(type="text", id="postal-code", placeholder="Wprowadź kod pocztowy"),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Miejscowość"),
                                dbc.Input(type="text", id="city", placeholder="Wprowadź miejscowość"),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Województwo/Region"),
                                dbc.Input(type="text", id="region", placeholder="Wprowadź województwo/region"),
                            ], width=12),
                        ], className="mb-3"),

                        # Informacje Medyczne
                        html.H4('Informacje Medyczne'),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Historia Medyczna"),
                                dbc.Textarea(id="medical-history", placeholder="Wprowadź istotne informacje medyczne"),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Choroby Przewlekłe"),
                                dbc.Input(type="text", id="chronic-diseases", placeholder="Wprowadź choroby przewlekłe"),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Alergie"),
                                dbc.Input(type="text", id="allergies", placeholder="Wprowadź alergie"),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Operacje"),
                                dbc.Input(type="text", id="surgeries", placeholder="Wprowadź przeszłe operacje"),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Leki Przyjmowane"),
                                dbc.Input(type="text", id="medications", placeholder="Wprowadź leki przyjmowane"),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Stan Ubezpieczenia"),
                                dbc.Input(type="text", id="insurance-status", placeholder="Wprowadź stan ubezpieczenia"),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Numer Polisy"),
                                dbc.Input(type="text", id="policy-number", placeholder="Wprowadź numer polisy"),
                            ], width=6),
                            dbc.Col([
                                dbc.Label("Nazwa Ubezpieczyciela"),
                                dbc.Input(type="text", id="insurance-provider", placeholder="Wprowadź nazwę ubezpieczyciela"),
                            ], width=6),
                        ], className="mb-3"),

                        # Osoba Kontaktowa w Nagłych Wypadkach
                        html.H4('Osoba Kontaktowa w Nagłych Wypadkach'),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Imię i Nazwisko"),
                                dbc.Input(type="text", id="emergency-contact-name", placeholder="Wprowadź imię i nazwisko"),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Relacja z Pacjentem"),
                                dcc.Dropdown(
                                    id="emergency-contact-relationship",
                                    options=[
                                        {'label': 'Rodzic', 'value': 'Parent'},
                                        {'label': 'Współmałżonek', 'value': 'Spouse'},
                                        {'label': 'Przyjaciel', 'value': 'Friend'},
                                        {'label': 'Inne', 'value': 'Other'}
                                    ],
                                    placeholder="Wybierz relację"
                                ),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Numer Telefonu"),
                                dbc.Input(type="text", id="emergency-contact-phone", placeholder="Wprowadź numer telefonu"),
                            ], width=12),
                        ], className="mb-3"),

                        # Zgody i Oświadczenia
                        html.H4('Zgody i Oświadczenia'),
                        dbc.Row([
                            dbc.Col([
                                dbc.Checklist(
                                    id='data-processing-consent',
                                    options=[{'label': 'Zgoda na przetwarzanie danych osobowych', 'value': 'data-processing'}],
                                    inline=True
                                ),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Checklist(
                                    id='treatment-consent',
                                    options=[{'label': 'Zgoda na leczenie', 'value': 'treatment'}],
                                    inline=True
                                ),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Checklist(
                                    id='research-consent',
                                    options=[{'label': 'Zgoda na wykorzystanie danych do badań', 'value': 'research'}],
                                    inline=True
                                ),
                            ], width=12),
                        ], className="mb-3"),

                        # Preferencje Pacjenta
                        html.H4('Preferencje Pacjenta'),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Preferencje Komunikacyjne"),
                                dcc.Dropdown(
                                    id="communication-preferences",
                                    options=[
                                        {'label': 'E-mail', 'value': 'Email'},
                                        {'label': 'SMS', 'value': 'SMS'},
                                        {'label': 'Telefon', 'value': 'Phone'}
                                    ],
                                    placeholder="Wybierz preferowaną formę komunikacji"
                                ),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Preferencje Czasowe"),
                                dbc.Input(type="text", id="time-preferences", placeholder="Wprowadź preferencje czasowe"),
                            ], width=12),
                        ], className="mb-3"),

                        # Dokumenty i Załączniki
                        html.H4('Dokumenty i Załączniki'),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Wgrywanie Dokumentów"),
                                dcc.Upload(
                                    id='upload-documents',
                                    children=html.Button('Wybierz pliki'),
                                    multiple=True
                                ),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Zdjęcie Pacjenta"),
                                dcc.Upload(
                                    id='upload-photo',
                                    children=html.Button('Wybierz zdjęcie'),
                                    multiple=False
                                ),
                            ], width=12),
                        ], className="mb-3"),

                        # Dane Dodatkowe
                        html.H4('Dane Dodatkowe'),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Numer Identyfikacyjny Pacjenta"),
                                dbc.Input(type="text", id="patient-id", placeholder="Wprowadź numer identyfikacyjny pacjenta"),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Data Rejestracji"),
                                dbc.Input(type="text", id="registration-date", value=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), readonly=True),
                            ], width=12),
                        ], className="mb-3"),

                        # Powiadomienia i Potwierdzenia
                        html.H4('Powiadomienia i Potwierdzenia'),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Preferencje Powiadomień"),
                                dcc.Dropdown(
                                    id="notification-preferences",
                                    options=[
                                        {'label': 'SMS', 'value': 'SMS'},
                                        {'label': 'E-mail', 'value': 'Email'}
                                    ],
                                    placeholder="Wybierz sposób otrzymywania powiadomień"
                                ),
                            ], width=12),
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Button("Zarejestruj", color="primary", id="register-button", n_clicks=0, style={'width': '100%'}),
                            ], width=12),
                        ], className="mb-3"),
                        html.Div(id='registration-message', style={'textAlign': 'center', 'marginTop': '20px'})
                    ], style={'maxWidth': '800px', 'paddingLeft': '15px'})  # Ustawienie wyrównania do lewej
                ], width=12)
            ])
        ], fluid=True)
    ])

    @app.callback(
        Output('registration-message', 'children'),
        Input('register-button', 'n_clicks'),
        State('first-name', 'value'),
        State('last-name', 'value'),
        State('dob', 'value'),
        State('gender', 'value'),
        State('identifier', 'value'),
        State('email', 'value'),
        State('phone', 'value'),
        State('street-address', 'value'),
        State('postal-code', 'value'),
        State('city', 'value'),
        State('region', 'value'),
        State('medical-history', 'value'),
        State('chronic-diseases', 'value'),
        State('allergies', 'value'),
        State('surgeries', 'value'),
        State('medications', 'value'),
        State('insurance-status', 'value'),
        State('policy-number', 'value'),
        State('insurance-provider', 'value'),
        State('emergency-contact-name', 'value'),
        State('emergency-contact-relationship', 'value'),
        State('emergency-contact-phone', 'value'),
        State('data-processing-consent', 'value'),
        State('treatment-consent', 'value'),
        State('research-consent', 'value'),
        State('communication-preferences', 'value'),
        State('time-preferences', 'value'),
        State('patient-id', 'value'),
        prevent_initial_call=True
    )
    def handle_registration(n_clicks, first_name, last_name, dob, gender, identifier, email, phone, street_address, postal_code, city, region,
                            medical_history, chronic_diseases, allergies, surgeries, medications, insurance_status, policy_number, insurance_provider,
                            emergency_contact_name, emergency_contact_relationship, emergency_contact_phone, data_processing_consent,
                            treatment_consent, research_consent, communication_preferences, time_preferences, patient_id):
        if not n_clicks:
            raise PreventUpdate

        # Logika obsługi rejestracji (np. zapis danych do bazy danych)
        registration_success = True  # Możesz tu dodać rzeczywistą logikę

        if registration_success:
            return "Rejestracja zakończona pomyślnie!"
        else:
            return "Wystąpił błąd podczas rejestracji. Proszę spróbować ponownie."

    return app
