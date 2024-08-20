import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from sqlalchemy.orm import sessionmaker
from app.database import SessionLocal, Patient

def create_patient_registration_layout():
    return dbc.Container([
        html.H2("Rejestracja Nowego Pacjenta"),
        dbc.Form([
            dbc.Row([
                dbc.Col(dbc.Label("Imię i Nazwisko")),
                dbc.Col(dbc.Input(id="input-name", type="text", placeholder="Jan Kowalski")),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Data Urodzenia")),
                dbc.Col(dbc.Input(id="input-birthdate", type="date")),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Płeć")),
                dbc.Col(dcc.Dropdown(
                    id="input-gender",
                    options=[
                        {"label": "Mężczyzna", "value": "M"},
                        {"label": "Kobieta", "value": "F"}
                    ],
                    value="M",
                    placeholder="Wybierz płeć"
                )),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("PESEL")),
                dbc.Col(dbc.Input(id="input-pesel", type="text", placeholder="12345678901")),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Adres")),
                dbc.Col(dbc.Input(id="input-address", type="text", placeholder="ul. Przykładowa 1, 00-000 Miasto")),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Telefon")),
                dbc.Col(dbc.Input(id="input-phone", type="text", placeholder="+48 123 456 789")),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Email")),
                dbc.Col(dbc.Input(id="input-email", type="email", placeholder="example@domain.com")),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Zdjęcie Karty Zdrowia")),
                dbc.Col(dcc.Upload(
                    id="upload-health-card",
                    children=html.Button('Wybierz plik'),
                    multiple=False
                )),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Oddział Szpitalny")),
                dbc.Col(dcc.Dropdown(
                    id="input-department",
                    options=[
                        {"label": "Anestezjologia i Intensywna Terapii", "value": "Anestezjologia i Intensywna Terapii"},
                        {"label": "Chirurgia Ogólna", "value": "Chirurgia Ogólna"},
                        {"label": "Chirurgia Klatki Piersiowej", "value": "Chirurgia Klatki Piersiowej"},
                        {"label": "Chirurgia Naczyniowa", "value": "Chirurgia Naczyniowa"},
                        {"label": "Chirurgia Onkologiczna", "value": "Chirurgia Onkologiczna"},
                        {"label": "Chirurgia Urazowa", "value": "Chirurgia Urazowa"},
                        {"label": "Dermatologia", "value": "Dermatologia"},
                        {"label": "Ginekologia", "value": "Ginekologia"},
                        {"label": "Ginekologia Onkologiczna", "value": "Ginekologia Onkologiczna"},
                        {"label": "Hematologia", "value": "Hematologia"},
                        {"label": "Internistyczny", "value": "Internistyczny"},
                        {"label": "Kardiologia", "value": "Kardiologia"},
                        {"label": "Kardiologia Interwencyjna", "value": "Kardiologia Interwencyjna"},
                        {"label": "Nefrologii", "value": "Nefrologii"},
                        {"label": "Neurologia", "value": "Neurologia"},
                        {"label": "Neurochirurgia", "value": "Neurochirurgia"},
                        {"label": "Onkologia", "value": "Onkologia"},
                        {"label": "Ortopedia i Traumatologia", "value": "Ortopedia i Traumatologia"},
                        {"label": "Otolaryngologia (Laryngologia)", "value": "Otolaryngologia (Laryngologia)"},
                        {"label": "Pediatria", "value": "Pediatria"},
                        {"label": "Pediatria Onkologiczna", "value": "Pediatria Onkologiczna"},
                        {"label": "Położnictwa", "value": "Położnictwa"},
                        {"label": "Psychiatria", "value": "Psychiatria"},
                        {"label": "Rehabilitacja", "value": "Rehabilitacja"},
                        {"label": "Reumatologia", "value": "Reumatologia"},
                        {"label": "Radiologia", "value": "Radiologia"},
                        {"label": "Urologii", "value": "Urologii"},
                        {"label": "Chirurgia Bariatryczna (Otyłości)", "value": "Chirurgia Bariatryczna (Otyłości)"},
                        {"label": "Medycyna Paliatywna", "value": "Medycyna Paliatywna"},
                        {"label": "Medycyna Ratunkowa", "value": "Medycyna Ratunkowa"},
                        {"label": "Zakaźny", "value": "Zakaźny"},
                        {"label": "Patologia Noworodka", "value": "Patologia Noworodka"},
                        {"label": "Endokrynologia", "value": "Endokrynologia"},
                        {"label": "Medycyna Sportowa", "value": "Medycyna Sportowa"},
                        {"label": "Medycyna Snu", "value": "Medycyna Snu"}
                    ],
                    placeholder="Wybierz oddział"
                )),
            ], className="mb-3"),
            # Nowe pola
            dbc.Row([
                dbc.Col(dbc.Label("Numer Ubezpieczenia Zdrowotnego")),
                dbc.Col(dbc.Input(id="input-insurance-number", type="text", placeholder="Numer ubezpieczenia")),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Grupa Krwi")),
                dbc.Col(dcc.Dropdown(
                    id="input-blood-group",
                    options=[
                        {"label": "A+", "value": "A+"},
                        {"label": "A-", "value": "A-"},
                        {"label": "B+", "value": "B+"},
                        {"label": "B-", "value": "B-"},
                        {"label": "AB+", "value": "AB+"},
                        {"label": "AB-", "value": "AB-"},
                        {"label": "O+", "value": "O+"},
                        {"label": "O-", "value": "O-"}
                    ],
                    placeholder="Wybierz grupę krwi"
                )),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Rodzaj Dokumentu Tożsamości")),
                dbc.Col(dcc.Dropdown(
                    id="input-id-type",
                    options=[
                        {"label": "Dowód Osobisty", "value": "Dowód Osobisty"},
                        {"label": "Paszport", "value": "Paszport"},
                        {"label": "Prawo Jazdy", "value": "Prawo Jazdy"},
                        {"label": "Inny", "value": "Inny"}
                    ],
                    placeholder="Wybierz rodzaj dokumentu"
                )),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Numer Dokumentu Tożsamości")),
                dbc.Col(dbc.Input(id="input-id-number", type="text", placeholder="Numer dokumentu")),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Historia Chorób")),
                dbc.Col(dbc.Textarea(id="input-medical-history", placeholder="Historia chorób pacjenta")),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col(dbc.Label("Alergie")),
                dbc.Col(dbc.Textarea(id="input-allergies", placeholder="Alergie pacjenta")),
            ], className="mb-3"),
            dbc.Button("Zarejestruj Pacjenta", id="submit-button", color="primary", n_clicks=0),
            html.Div(id="output-state", className="mt-3"),
            dbc.Col(dbc.Button("Powrót do Panelu Głównego", href="/main-panel/", color="secondary", n_clicks=0,
                               className="me-2")),
        ], className="mt-5"),
    ], className="mt-5")


def create_patient_registration(server):
    app = dash.Dash(
        server=server,
        routes_pathname_prefix='/patient-registration/',  # Zmiana na właściwą trasę
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )

    app.layout = create_patient_registration_layout()

    @app.callback(
        Output('output-state', 'children'),
        Input('submit-button', 'n_clicks'),
        State('input-name', 'value'),
        State('input-birthdate', 'value'),
        State('input-gender', 'value'),
        State('input-pesel', 'value'),
        State('input-address', 'value'),
        State('input-phone', 'value'),
        State('input-email', 'value'),
        State('input-department', 'value'),
        State('input-insurance-number', 'value'),
        State('input-blood-group', 'value'),
        State('input-id-type', 'value'),
        State('input-id-number', 'value'),
        State('input-medical-history', 'value'),
        State('input-allergies', 'value')
    )
    def register_patient(n_clicks, name, birthdate, gender, pesel, address, phone, email, department, insurance_number,
                         blood_group, id_type, id_number, medical_history, allergies):
        if n_clicks > 0:
            try:
                db = SessionLocal()
                new_patient = Patient(
                    full_name=name,
                    birthdate=birthdate,
                    gender=gender,
                    pesel=pesel,
                    address=address,
                    phone=phone,
                    email=email,
                    department=department,
                    insurance_number=insurance_number,
                    blood_group=blood_group,
                    id_type=id_type,
                    id_number=id_number,
                    medical_history=medical_history,
                    allergies=allergies
                )
                db.add(new_patient)
                db.commit()
                return f'Pacjent {name} został pomyślnie zarejestrowany!'
            except Exception as e:
                return f'Wystąpił błąd: {str(e)}'
        return ''

    return app
